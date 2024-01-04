
""" 
  High Volume For-Hire Vehicle Trip Records
  Descarga de archivos Parquet del año 2020 al 2023
"""

base_url="https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"
bucket="gs://raw_files/parquet/"

# Bucle para descargar archivos desde 2020-01 hasta 2023-10
for year in {2020..2023}; do
  for month in {01..12}; do
    link="${base_url}${year}-${month}.parquet"
    
    # Descargar, copiar a Cloud Storage y eliminar archivo de la VM
    curl -LJO "$link"
    gsutil cp "fhvhv_tripdata_${year}-${month}.parquet" "$bucket"
    rm "fhvhv_tripdata_${year}-${month}.parquet"
  done
done


""" 
  Fuel consumption ratings
  Decargar de archivos CSV del año 2020 al 2023
"""

base_url="https://natural-resources.canada.ca/sites/nrcan/files/oee/files/csv/MY"
bucket="gs://raw_files/csv/"

# Bucle para descargar archivos desde 2020 hasta 2023
for year in {2020..2023}; do
  link="${base_url}${year}%20Fuel%20Consumption%20Ratings.csv"
  
  # Descargar, copiar a Cloud Storage y eliminar archivo de la VM
  curl -LJO "$link"
  gsutil cp "MY${year}%20Fuel%20Consumption%20Ratings.csv" "$bucket"
  rm "MY${year}%20Fuel%20Consumption%20Ratings.csv"
done
