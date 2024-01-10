""" 
  High Volume For-Hire Vehicle Trip Records
  Descarga de archivos Parquet del año 2020 al 2023
"""
base_url="https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_"
bucket="gs://files_raw/parquet/"

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
bucket="gs://files_raw/csv/"

# Bucle para descargar archivos desde 2020 hasta 2023
for year in {2020..2023}; do
  link="${base_url}${year}%20Fuel%20Consumption%20Ratings.csv"
  
  # Descargar, copiar a Cloud Storage y eliminar archivo de la VM
  curl -LJO "$link"
  gsutil cp "MY${year}%20Fuel%20Consumption%20Ratings.csv" "$bucket"
  gsutil mv "${bucket}MY${year}%20Fuel%20Consumption%20Ratings.csv" "${bucket}fuelConsumption_${year}.csv"
  rm "MY${year}%20Fuel%20Consumption%20Ratings.csv"
done



""" 
  Weather - Open Meteo
  Decargar archivos CSV del año 2020 al 2023
"""
# Descargar, copiar a Cloud Storage y eliminar archivo de la VM
curl -LJO "https://archive-api.open-meteo.com/v1/archive?latitude=40.714&longitude=-74.006&start_date=2020-01-01&end_date=2023-12-31&hourly=relative_humidity_2m,apparent_temperature,rain,snowfall,snow_depth,cloud_cover_low,wind_speed_10m,wind_gusts_10m&timezone=America%2FNew_York&format=csv"
gsutil cp open-meteo-40.74N74.04W37m.csv gs://files_raw/csv/ 
rm open-meteo-40.74N74.04W37m.csv



""" 
  airPollution - Open Meteo
  Decargar archivos JSON del año 2020 al 2023
"""
  # Descargar, copiar a Cloud Storage y eliminar archivo de la VM
curl -LJO "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=40.714&lon=-74.006&start=1606453200&end=1703998800&appid=32ac2c365a2bebaea6273988ff6c9db6"
gsutil cp 'history?lat=40.714&lon=-74.006&start=1606453200&end=1703998800&appid=32ac2c365a2bebaea6273988ff6c9db6' gs://files_raw/json/ 
gsutil mv gs://files_raw/json/'history?lat=40.714&lon=-74.006&start=1606453200&end=1703998800&appid=32ac2c365a2bebaea6273988ff6c9db6' gs://files_raw/json/airPollution.json
rm 'history?lat=40.714&lon=-74.006&start=1606453200&end=1703998800&appid=32ac2c365a2bebaea6273988ff6c9db6'


"""
  Decargar de archivos CSV carros electricos Alternative Fuel Vehicles US
"""

# Descargar, copiar a Cloud Storage y eliminar archivo de la VM
curl -LJO "https://drive.google.com/uc?export=download&id=17H43adHQUi0AEUUQUOkOfO45IOVJId9H"
gsutil cp 'Alternative Fuel Vehicles US.csv' gs://files_raw/csv/
rm 'Alternative Fuel Vehicles US.csv'

"""
  Decarga de archivos CSV precio de carros
"""

curl -LJO "https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/datasets/carPrices.csv"
gsutil cp carPrices.csv gs://files_raw/csv/
rm carPrices.csv