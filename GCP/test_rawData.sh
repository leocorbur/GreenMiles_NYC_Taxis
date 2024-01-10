
"""
  Decarga de archivos CSV precio de carros
"""

curl -LJO "https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/datasets/carPrices.csv"
gsutil cp carPrices.csv gs://files_raw/csv/
rm carPrices.csv