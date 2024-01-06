from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, LongType
from google.cloud import storage

# Configura tu SparkSession
spark = SparkSession.builder.appName("remove_nulls_with_schema").getOrCreate()

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

# Define la ruta del archivo Parquet en Google Cloud Storage
gcs_path_input = "gs://files_intermediate/intermediate_fhvhv_tripdata_2020-01.parquet/"
gcs_path_output = "gs://files_intermediate/intermediate_fhvhv_tripdata_2020-01_step2.parquet/"

# Lee el archivo Parquet en un DataFrame de Spark con el esquema personalizado
df = spark.read.schema(custom_schema).parquet(gcs_path_input)

# Realiza la limpieza de valores nulos
df = df.na.drop()

# Guarda el DataFrame limpio y seleccionado como un nuevo archivo Parquet en GCS
df.coalesce(1).write.parquet(gcs_path_output, mode="overwrite")

# Elimina el archivo _SUCCESS desde el bucket de GCS
gcs_bucket_name = "files_intermediate"
gcs_success_path = f"gs://{gcs_bucket_name}/intermediate_fhvhv_tripdata_2020-01_step2.parquet/_SUCCESS"

client = storage.Client()
bucket = client.get_bucket(gcs_bucket_name)
blob = bucket.blob("intermediate_fhvhv_tripdata_2020-01_step2.parquet/_SUCCESS")
blob.delete()

# Detén la sesión de Spark
spark.stop()