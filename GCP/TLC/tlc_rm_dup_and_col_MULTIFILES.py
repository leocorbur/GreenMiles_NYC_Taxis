from pyspark.sql import SparkSession

# Configura tu SparkSession
spark = SparkSession.builder.appName("remove_duplicates").getOrCreate()

# Evita que se genere _success
spark.conf.set("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false")

years = ["2020", "2021", "2022", "2023"]
months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

for year in years:
    for month in months:
        # Define la ruta del archivo Parquet en Google Cloud Storage
        gcs_path_input = f"gs://files_raw/parquet/fhvhv_tripdata_{year}-{month}.parquet"
        gcs_path_output = f"gs://files_intermediate/parquet/intermediate_fhvhv_tripdata_{year}-{month}.parquet"

        try:
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
                "base_passenger_fare"
            ]

            df = df.select(*selected_columns)

            # Guarda el DataFrame sin duplicados como un nuevo archivo Parquet en GCS
            df.coalesce(1).write.parquet(gcs_path_output, mode="overwrite")
        except:
            print(f"El archivo {gcs_path_input} no existe. Se omite el procesamiento para este mes.")

# Detén la sesión de Spark
spark.stop()