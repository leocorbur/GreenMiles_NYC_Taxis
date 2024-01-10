from pyspark.sql import SparkSession

# Crear una sesión de Spark
spark = SparkSession.builder.appName("Car Prices").getOrCreate()


# Ruta del archivo CSV
gcs_path_input = "gs://files_raw/csv/carPrices.csv"

# Leer el archivo CSV en un DataFrame de PySpark
df_spark = spark.read.csv(gcs_path_input, header=True, inferSchema=True, ignoreLeadingWhiteSpace=True)


# Configura las opciones para BigQuery
bigquery_project = "spheric-base-407402"
bigquery_dataset = "nyc_taxis"
bigquery_table = "carPrice"

# Escribe el DataFrame en BigQuery
df_spark.write.format("bigquery") \
.option("temporaryGcsBucket", "files_intermediate") \
.option("table", f"{bigquery_project}:{bigquery_dataset}.{bigquery_table}") \
.mode("overwrite") \
.save()

# Detener la sesión de Spark (es importante hacer esto al final del script)
spark.stop()