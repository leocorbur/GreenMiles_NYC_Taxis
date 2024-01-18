from pyspark.sql import SparkSession, Window, Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, monotonically_increasing_id, desc, row_number
from pyspark.sql import functions as F
from datetime import datetime

# Tiempo de Ejecución
start_time = datetime.now()

# Crear una sesión de Spark
spark = SparkSession.builder.appName("FuelConsumption").getOrCreate()

# Definir el esquema manualmente
schema = StructType([
    StructField("Model10", StringType(), True),
    StructField("Make", StringType(), True),
    StructField("Model12", StringType(), True),
    StructField("Vehicle Class", StringType(), True),
    StructField("Engine Size", StringType(), True),
    StructField("Cylinders", StringType(), True),
    StructField("Transmission", StringType(), True),
    StructField("Fuel", StringType(), True),
    StructField("Fuel Consumption", StringType(), True),
    StructField("_c9", StringType(), True),
    StructField("_c10", StringType(), True),
    StructField("_c11", StringType(), True),
    StructField("CO2 Emissions", StringType(), True),
    StructField("CO2", StringType(), True),
    StructField("Smog", StringType(), True)  
])


# Lista de archivos
gcs_path_input = ["gs://files_raw/csv/fuelConsumption_2020.csv", 
                  "gs://files_raw/csv/fuelConsumption_2021.csv", 
                  "gs://files_raw/csv/fuelConsumption_2022.csv", 
                  "gs://files_raw/csv/fuelConsumption_2023.csv"]

# Registro
file_name = "fuelConsumption files"
file_format = "csv"
initial_record_count = 0
null_values_count = []
duplicate_records_count = 0

# DataFrame para almacenar datos combinados
df_combinado = spark.createDataFrame([], schema=schema)

# Iterar sobre cada archivo
for archivo in gcs_path_input:

    ruta_archivo = archivo
    
    # Leer datos del archivo
    df_temp = spark.read.csv(ruta_archivo, schema=schema, header=True)
    
    # Registro
    initial_record_count += df_temp.count()
    initial_column_count = len(df_temp.columns)

    # Filtrar y retirar las filas que no son necesarias
    df_temp = df_temp.filter((df_temp["Model10"] != "Year"))

    # Registro
    null_values_count += list(df_temp.select([F.sum(col(c).isNull().cast("int")).alias(c) for c in df_temp.columns]).collect()[0].asDict().values())
    duplicate_records_count += df_temp.count() - df_temp.dropDuplicates().count
    
    # Eliminar filas con todas las entradas nulas
    df_temp = df_temp.na.drop(how='all')
    
    # Agregar índices usando row_number()
    windowSpec = Window.orderBy("Smog")
    df_temp = df_temp.withColumn("Index", row_number().over(windowSpec))
    
    # Filtrar y retirar las filas que no son necesarias
    df_temp = df_temp.filter((df_temp["Index"] > 8))
    
    # Seleccionar las columnas deseadas y reorganizarlas
    columnas_seleccionadas = ["Model10","Make", "Model12", "Vehicle Class", "Engine Size", "Cylinders",
                              "Transmission", "Fuel", "Fuel Consumption", "_c9", "_c10",
                               "_c11", "CO2 Emissions", "CO2", "Smog" ]
    df_temp = df_temp.select(columnas_seleccionadas)
    
    # Reemplazar NaN o null con 0 en todas las columnas
    df_temp = df_temp.fillna(0)
    
   
    
    # Unir los DataFrames
    df_combinado = df_combinado.union(df_temp)

# Registro
final_record_count = df_combinado.count()
final_column_count = len(df_combinado.columns)

 # Cambiar los tipos de datos
for columna in ["Engine Size", "Fuel Consumption", "_c9", "_c10"]:
    df_combinado = df_combinado.withColumn(columna, col(columna).cast("decimal(10,2)"))

for columna in ["Model10","Cylinders", "CO2 Emissions", "CO2","_c11", "Smog"]:
    df_combinado = df_combinado.withColumn(columna, col(columna).cast("integer"))



df_combinado = df_combinado.coalesce(1)

# Cambiar el nombre de las columnas
nuevos_nombres = {
    "Model10": "Year",
    "Model12": "Model",
    "_c9": "Fuel_Con_Hwy",
    "_c10": "Fuel_Con_Comb",
    "_c11": "Fuel_Con_Comb_Mpg"
}

for columna_antigua, nuevo_nombre in nuevos_nombres.items():
    df_combinado = df_combinado.withColumnRenamed(columna_antigua, nuevo_nombre)

# Configura las opciones para BigQuery
bigquery_project = "spheric-base-407402"
bigquery_dataset = "nyc_taxis"
bigquery_table = "fuelConsumption"

# Escribe el DataFrame en BigQuery
df_combinado.write.format("bigquery") \
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

spark.stop()
