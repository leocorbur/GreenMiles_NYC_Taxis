# Documentación Técnica - Informe Power BI con BigQuery #

Este documento proporciona información técnica sobre la creación de un informe en Power BI que utiliza BigQuery como origen de datos. El objetivo del informe es analizar y visualizar datos relevantes para proporcionar una base sólida en la toma de decisiones, considerando para ello las variables viajes, tiemppo de espera, demanda, ambiente, autos e ingresos.

## Conexión a BigQuery ##

Se utilizaron credenciales de Google Cloud para la conexión a BigQuery. se debe tener permisos adecuados para acceder al conjunto de datos utilizado.

Proyecto y Conjunto de Datos:

El informe se conecta al proyecto "GreenMiles NYC Taxis" y utiliza el conjunto de datos "spheric-base-407402".

Se implementó la siguiente consulta en bigquery para obtener datos específicos:

```
01

   SELECT
   taxizone.Zone AS Zone,
   COUNT(*) AS numero_de_viajes,
   AVG(trip_miles) AS trip_miles,
   AVG(base_passenger_fare) AS base_passenger_fare
FROM
  `spheric-base-407402.nyc_taxis.tlc` AS tlc
  INNER JOIN `spheric-base-407402.nyc_taxis.taxizone` AS taxizone
  ON tlc.PULocationID = taxizone.LocationID
GROUP BY
  taxizone.Zone;

02

WITH MonthlyTrips AS (
  SELECT
    EXTRACT(YEAR FROM TIMESTAMP(pickup_datetime)) AS year,
    EXTRACT(MONTH FROM TIMESTAMP(pickup_datetime)) AS month,
    COUNT(*) AS num_trips
  FROM
    `spheric-base-407402.nyc_taxis.tlc`
  GROUP BY
    year, month)

SELECT
  year,
  month,
  num_trips,
  LAG(num_trips) OVER (ORDER BY year, month) AS prev_month_trips,
  ROUND((num_trips - LAG(num_trips) OVER (ORDER BY year, month)) / LAG(num_trips) OVER (ORDER BY year, month) * 100, 2) AS percent_difference
FROM
  MonthlyTrips
ORDER BY
  year, month;

02

SELECT
  EXTRACT(DAYOFWEEK FROM TIMESTAMP(pickup_datetime)) AS day_of_week,
  EXTRACT(HOUR FROM TIMESTAMP(pickup_datetime)) AS hour_of_day,
  AVG(EXTRACT(SECOND FROM TIMESTAMP(pickup_datetime) - TIMESTAMP(request_datetime))) AS avg_waiting_time
FROM
  `spheric-base-407402.nyc_taxis.tlc`
GROUP BY
  day_of_week, hour_of_day
ORDER BY
  day_of_week, hour_of_day;

03
SELECT 
  EXTRACT(YEAR FROM TIMESTAMP(date)) AS year,
  EXTRACT(MONTH FROM TIMESTAMP(date)) AS month,
  ROUND(AVG(apparent_temperature), 2) AS avg_apparent_temperature,
  ROUND(AVG(rain), 2) AS avg_rain,
  ROUND(AVG(snowfall), 2) AS avg_snowfall
FROM 
 `spheric-base-407402.nyc_taxis.weather`
GROUP BY 
  year, month
ORDER BY 
  year, month;

  04
  WITH base_passenger_fare AS (
  SELECT
    EXTRACT(YEAR FROM TIMESTAMP(pickup_datetime)) AS year,
    EXTRACT(MONTH FROM TIMESTAMP(pickup_datetime)) AS month,
    SUM(base_passenger_fare) AS sum_passengers
  FROM
    `spheric-base-407402.nyc_taxis.tlc`
  GROUP BY
    year, month
)

SELECT
  year,
  month,
  sum_passengers,
  LAG(sum_passengers) OVER (ORDER BY year, month) AS prev_month_passengers,
  ROUND((sum_passengers - LAG(sum_passengers) OVER (ORDER BY year, month)) / LAG(sum_passengers) OVER (ORDER BY year, month) * 100, 2) AS percent_difference_passengers
FROM
  base_passenger_fare
ORDER BY
  year, month;

  05
SELECT
   taxizone.borough AS borough,
  COUNT(*) AS numero_de_viajes,
  AVG (trip_miles) AS trip_miles,
  AVG (base_passenger_fare) AS base_passenger_fare
FROM
  `spheric-base-407402.nyc_taxis.tlc` AS tlc
INNER JOIN
  `spheric-base-407402.nyc_taxis.taxizone` AS taxizone
ON
tlc.PULocationID = taxizone.LocationID
GROUP BY
  taxizone.borough;

06
SELECT
   taxizone.Zone AS Zone,
  COUNT(*) AS numero_de_viajes,
  AVG (trip_miles) AS trip_miles,
  AVG (base_passenger_fare) AS base_passenger_fare
FROM
  `spheric-base-407402.nyc_taxis.tlc` AS tlc
INNER JOIN
  `spheric-base-407402.nyc_taxis.taxizone` AS taxizone
ON
tlc.PULocationID = taxizone.LocationID
GROUP BY
  taxizone.Zone;
```   
## Modelado de Datos en Power BI ##
Relaciones:

Se establecieron relaciones entre las tablas para facilitar el análisis de datos.

## Modelado de Datos en Power BI ##
Relaciones:

Se establecieron relaciones entre las tablas para facilitar el análisis de datos.
<p align="center"><img src=./src/EntidadRelacion.jpeg></p>


## Visualizaciones y Páginas ##
Visualizaciones:

Se utilizaron diversas visualizaciones, como gráficos de barras, tablas dinámicas y mapas, para representar los datos de manera efectiva.
Páginas:

Se crearon páginas específicas para organizar visualizaciones según categorías y temas.

1. Viajes y tiempo e espera 
<p align="center"><img src=./src/viajes.png></p>

2. Demanda
<p align="center"><img src=./src/demanda.png></p>