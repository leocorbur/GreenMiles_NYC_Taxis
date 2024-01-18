from pyspark.sql import SparkSession, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import explode, col, from_unixtime, to_timestamp, hour
from google.cloud import storage
from pyspark.sql import functions as F
from datetime import datetime

# Tiempo de Ejecución
start_time = datetime.now()

# Crear una sesión de Spark
spark = SparkSession.builder.appName("Weather").getOrCreate()

# Ruta del archivo CSV
gcs_path_input = f"gs://files_raw/csv/open-meteo-40.74N74.04W37m.csv"

# Verifica si el archivo existe antes de intentar leerlo con Spark
client = storage.Client()
bucket_name = "files_raw"  
blob_name = f"csv/open-meteo-40.74N74.04W37m.csv"
blob = client.bucket(bucket_name).get_blob(blob_name)

if blob is not None and blob.exists():
    # Registro
    file_name = "weather"
    file_format = "csv"

    # Definir el esquema manualmente
    schema = StructType([
        StructField("time", StringType(), True),
        StructField("relative_humidity_2m", DoubleType(), True),
        StructField("apparent_temperature", DoubleType(), True),
        StructField("rain", DoubleType(), True),
        StructField("snowfall", DoubleType(), True),
        StructField("snow_depth", DoubleType(), True),
        StructField("cloud_cover_low", DoubleType(), True),
        StructField("wind_speed_10m", DoubleType(), True),
        StructField("wind_gusts_10m", DoubleType(), True)
    ])


    # Leer el archivo CSV en un DataFrame de PySpark
    df_spark = spark.read.csv(gcs_path_input, header=True, schema=schema, ignoreLeadingWhiteSpace=True)

    # Registro
    initial_record_count = df_spark.count()
    initial_column_count = len(df_spark.columns)
    null_values_count = list(df_spark.select([F.sum(col(c).isNull().cast("int")).alias(c) for c in df_spark.columns]).collect()[0].asDict().values())
    duplicate_records_count = df_spark.count() - df_spark.dropDuplicates().count()

    # Filtrar las filas donde "time" no es igual a "time" y tampoco es igual a 40.738136
    df_spark = df_spark.filter((df_spark["time"] != "40.738136") & (df_spark["time"] != "time"))

    # Convertir la columna "time" a timestamp
    df_spark = df_spark.withColumn("datetime", to_timestamp("time", "yyyy-MM-dd'T'HH:mm"))

    # Extraer la fecha y la hora directamente usando la función hour
    df_spark = df_spark.withColumn("date", df_spark["datetime"].cast("date"))
    df_spark = df_spark.withColumn("hour_of_day", hour(df_spark["datetime"]))

    # Seleccionar las columnas deseadas y reorganizarlas
    columnas_seleccionadas = ["date", "hour_of_day", "relative_humidity_2m", "apparent_temperature", "rain", "snowfall", "snow_depth", "cloud_cover_low", "wind_speed_10m", "wind_gusts_10m"]
    df_spark = df_spark.select(columnas_seleccionadas)

    # Registro
    final_record_count = df_spark.count()
    final_column_count = len(df_spark.columns)
    

    # Configura las opciones para BigQuery
    bigquery_project = "spheric-base-407402"
    bigquery_dataset = "nyc_taxis"
    bigquery_table = "weather"

    # Escribe el DataFrame en BigQuery
    df_spark.write.format("bigquery") \
    .option("temporaryGcsBucket", "files_intermediate") \
    .option("table", f"{bigquery_project}:{bigquery_dataset}.{bigquery_table}") \
    .mode("overwrite") \
    .save()

    end_time = datetime.now()
    execution_time = end_time - start_time
    execution_time_seconds = execution_time.total_seconds()
    execution_date = start_time.date()

    registro = [file_name, file_format, initial_record_count, final_record_count,
            initial_column_count, final_column_count, sum(null_values_count),
             duplicate_records_count, execution_time_seconds, execution_date ]
    
    # Crear DataFrame de Spark a partir de la lista registro
    registro_df = spark.createDataFrame([Row(*registro)], ["file_name", "file_format", "initial_record_count", 
                                                      "final_record_count", "initial_column_count", 
                                                      "final_column_count", "null_values_sum", 
                                                      "duplicate_records_count", "execution_time_seconds", 
                                                      "execution_date"])
    
    # Cambiar los tipos de datos en el DataFrame de registro
    registro_df = registro_df.withColumn("null_values_sum", col("null_values_sum").cast("integer"))

    # Tabla de Auditoria
    bigquery_project = "spheric-base-407402"
    bigquery_dataset = "nyc_taxis"
    bigquery_table = "Auditoria"

    registro_df.write.format("bigquery") \
    .option("temporaryGcsBucket", "files_intermediate") \
    .option("table", f"{bigquery_project}:{bigquery_dataset}.{bigquery_table}") \
    .mode("append") \
    .save()

else: 
    print(f"El archivo {gcs_path_input} no existe.")

# Detener la sesión de Spark (es importante hacer esto al final del script)
spark.stop()
