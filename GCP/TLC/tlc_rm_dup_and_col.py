from pyspark.sql import SparkSession
from google.cloud import storage

# Configura tu SparkSession
spark = SparkSession.builder.appName("remove_duplicates").getOrCreate()

# Define la ruta del archivo Parquet en Google Cloud Storage
gcs_path_input = "gs://files_raw/fhvhv_tripdata_2020-01.parquet"
gcs_path_output = "gs://files_intermediate/intermediate_fhvhv_tripdata_2020-01.parquet"

# Lee el archivo Parquet en un DataFrame de Spark
df = spark.read.parquet(gcs_path_input)

# Elimina duplicados basados en todas las columnas
df = df.dropDuplicates()

# Selecciona las columnas específicas
selected_columns = [
    "hvfhs_license_num",
    "request_datetime",
    "pickup_datetime",
    "dropoff_datetime",
    "PULocationID",
    "DOLocationID",
    "trip_miles",
    "trip_time",
    "base_passenger_fare"]

df = df.select(*selected_columns)

# Guarda el DataFrame sin duplicados como un nuevo archivo Parquet en GCS
df.coalesce(1).write.parquet(gcs_path_output, mode="overwrite")

# Elimina el archivo _SUCCESS desde el bucket de GCS
gcs_bucket_name = "files_intermediate"
gcs_success_path = f"gs://{gcs_bucket_name}/intermediate_fhvhv_tripdata_2020-01.parquet/_SUCCESS"

client = storage.Client()
bucket = client.get_bucket(gcs_bucket_name)
blob = bucket.blob("intermediate_fhvhv_tripdata_2020-01.parquet/_SUCCESS")
blob.delete()

# Detén la sesión de Spark
spark.stop()