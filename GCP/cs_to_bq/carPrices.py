from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import col
from pyspark.sql import functions as F
from datetime import datetime

# Tiempo de Ejecución
start_time = datetime.now()

# Crear una sesión de Spark
spark = SparkSession.builder.appName("Car Prices").getOrCreate()


# Ruta del archivo CSV
gcs_path_input = "gs://files_raw/csv/carPrices.csv"

# Registro
file_name = "carPrices"
file_format = "csv"

# Leer el archivo CSV en un DataFrame de PySpark
df_spark = spark.read.csv(gcs_path_input, header=True, inferSchema=True, ignoreLeadingWhiteSpace=True)

# Registro
initial_record_count = df_spark.count()
initial_column_count = len(df_spark.columns)
null_values_count = list(df_spark.select([F.sum(col(c).isNull().cast("int")).alias(c) for c in df_spark.columns]).collect()[0].asDict().values())
duplicate_records_count = df_spark.count() - df_spark.dropDuplicates().count()
final_record_count = df_spark.count()
final_column_count = len(df_spark.columns)


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


# Detener la sesión de Spark (es importante hacer esto al final del script)
spark.stop()