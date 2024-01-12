"""
  Decarga de scripts de python
"""
url_base='https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/'
files=(
  "tlc_rm_dup_and_col_MULTIFILES.py" \
  "tlc_rm_nan_MULTIFILES.py" \
  "load_to_bq_MULTIFILES.py" \
  "cs_to_bigquery_airPollution.py" \
  "cs_to_bigquery_weather.py" \
  "cs_to_bq_altFuelVehicles.py" \
  "cs_to_bq_fuelConsumption.py" \
  "cs_to_bigquery_carPrices.py"
)

for file in "${files[@]}"; do
    curl -LJO "${url_base}${file}" &&
    gsutil cp "$file" gs://jobs_dataproc/ &&
    rm "$file"
done


