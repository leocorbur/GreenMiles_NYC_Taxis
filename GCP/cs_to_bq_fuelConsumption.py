from pyspark.sql import SparkSession, Window
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import col, monotonically_increasing_id, desc, row_number

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

# DataFrame para almacenar datos combinados
df_combinado = spark.createDataFrame([], schema=schema)

# Iterar sobre cada archivo
for archivo in gcs_path_input:
    ruta_archivo = archivo
    
    # Leer datos del archivo
    df_temp = spark.read.csv(ruta_archivo, schema=schema, header=True)
    
    # Filtrar y retirar las filas que no son necesarias
    df_temp = df_temp.filter((df_temp["Model10"] != "Year"))
    
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


spark.stop()
