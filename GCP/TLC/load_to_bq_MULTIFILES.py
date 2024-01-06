from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, LongType

# Configura tu SparkSession
spark = SparkSession.builder.appName("load_to_bq").getOrCreate()

# Evita que se genere _success
spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")

years = ["2020", "2021", "2022", "2023"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for year in years:
    for month in months:
        # Define la ruta del archivo Parquet en Google Cloud Storage
        gcs_path_input = f"gs://files_intermediate/parquet/intermediate_fhvhv_tripdata_{year}-{month}_step2.parquet"
        
        try:
            # Define el esquema para las columnas
            custom_schema = StructType([
                StructField("hvfhs_license_num", StringType(), True),
                StructField("request_datetime", TimestampType(), True),
                StructField("pickup_datetime", TimestampType(), True),
                StructField("dropoff_datetime", TimestampType(), True),
                StructField("PULocationID", LongType(), True),
                StructField("DOLocationID", LongType(), True),
                StructField("trip_miles", DoubleType(), True),
                StructField("trip_time", LongType(), True),
                StructField("base_passenger_fare", DoubleType(), True)
            ])

            # Lee el archivo Parquet en un DataFrame de Spark con el esquema personalizado
            df = spark.read.schema(custom_schema).parquet(gcs_path_input)

            # Configura las opciones para BigQuery
            bigquery_project = "spheric-base-407402"
            bigquery_dataset = "nyc_taxis"
            bigquery_table = "tlc"

            # Escribe el DataFrame en BigQuery
            df.write.format("bigquery") \
                .option("temporaryGcsBucket", "files_intermediate") \
                .option("table", f"{bigquery_project}:{bigquery_dataset}.{bigquery_table}") \
                .mode("append") \
                .save()
        except:
            print(f"El archivo {gcs_path_input} no existe. Se omite el procesamiento para este mes.")

# Detén la sesión de Spark
spark.stop()