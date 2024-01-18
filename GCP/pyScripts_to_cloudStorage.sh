"""
  Decarga de scripts de python
"""
url_base='https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/cs_to_bq/'
files=(
  "tlc.py" \
  "airPollution.py" \
  "weather.py" \
  "altFuelVehicles.py" \
  "fuelConsumption.py" \
  "carPrices.py"
)

for file in "${files[@]}"; do
    curl -LJO "${url_base}${file}" &&
    gsutil cp "$file" gs://jobs_dataproc/ &&
    rm "$file"
done


