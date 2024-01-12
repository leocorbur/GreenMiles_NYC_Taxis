from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import explode, col, when, count
from google.cloud import storage

# Crear una sesión de Spark
spark = SparkSession.builder.appName("Alternative Fuel Vehicles").getOrCreate()


# Ruta del archivo CSV
gcs_path_input = "gs://files_raw/csv/Alternative Fuel Vehicles US.csv"

# Verifica si el archivo existe antes de intentar leerlo con Spark
client = storage.Client()
bucket_name = "files_raw"  
blob_name = f"csv/Alternative Fuel Vehicles US.csv"
blob = client.bucket(bucket_name).get_blob(blob_name)

if blob is not None and blob.exists():
    # Leer el archivo CSV en un DataFrame de PySpark
    df_spark = spark.read.csv(gcs_path_input, header=True, inferSchema=True, ignoreLeadingWhiteSpace=True)

    selected_columns = ["Category", "Model", "Model Year", "Manufacturer", "Fuel", "All-Electric Range", 
                        "Alternative Fuel Economy Combined","Conventional Fuel Economy Combined",
                        "Transmission Type", "Engine Size"]
    df_spark = df_spark.select(*selected_columns)

    # Reemplazar 'Manual|Automatic' con 'Automatic|Manual'
    df_spark = df_spark.withColumn(
        'Transmission Type',
        when(col('Transmission Type') == 'Manual|Automatic', 'Automatic|Manual').otherwise(col('Transmission Type'))
    )

    # Reemplazar valores nulos con 'Manual'
    df_spark = df_spark.withColumn(
        'Transmission Type',
        when(col('Transmission Type').isNull(), 'Manual').otherwise(col('Transmission Type'))
    )

    # Reemplazar 'Auto' con 'Automatic'
    df_spark = df_spark.withColumn(
        'Transmission Type',
        when(col('Transmission Type') == 'Auto', 'Automatic').otherwise(col('Transmission Type'))
    )

    # Reemplazar valores nulos con 'Manual'
    df_spark = df_spark.withColumn(
        'Transmission Type',
        when(col('Transmission Type').isNull(), 'Manual').otherwise(col('Transmission Type'))
    )

    # Seleccionar las columnas por las que deseas eliminar duplicados
    subset_columns = ['Category', 'Model', 'Model Year', 'Manufacturer', 'Fuel']

    # Eliminar duplicados basados en las columnas seleccionadas
    df_spark = df_spark.dropDuplicates(subset=subset_columns)

    # Eliminar filas con todos los valores nulos o vacíos
    df_spark = df_spark.dropna(how='all')

    # Reemplazar valores nulos por "Sin Dato" en las columnas de tipo string
    columns_string = ['Category', 'Model', 'Manufacturer', 'Fuel', 'Transmission Type', 'Engine Size']
    for column in columns_string:
        df_spark = df_spark.withColumn(column, when(col(column).isNull(), "Sin Dato").otherwise(col(column)))

    # Reemplazar valores nulos por 0 en las columnas de tipo integer y double
    columns_numeric = ['Model Year', 'All-Electric Range', 'Alternative Fuel Economy Combined', 'Conventional Fuel Economy Combined']
    for column in columns_numeric:
        df_spark = df_spark.withColumn(column, when(col(column).isNull(), 0).otherwise(col(column)))

    # Configura las opciones para BigQuery
    bigquery_project = "spheric-base-407402"
    bigquery_dataset = "nyc_taxis"
    bigquery_table = "altFuelVehicles"

    # Escribe el DataFrame en BigQuery
    df_spark.write.format("bigquery") \
    .option("temporaryGcsBucket", "files_intermediate") \
    .option("table", f"{bigquery_project}:{bigquery_dataset}.{bigquery_table}") \
    .mode("overwrite") \
    .save()

else:
    print(f"El archivo {gcs_path_input} no existe.")

# Detener la sesión de Spark (es importante hacer esto al final del script)
spark.stop()