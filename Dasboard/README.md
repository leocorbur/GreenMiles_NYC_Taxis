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
<p align="center"><img src=./src/EntidadRelacion.jpeg></p>


## Visualizaciones y Páginas ##
Visualizaciones:

Se utilizaron diversas visualizaciones, como gráficos de barras, tablas dinámicas y mapas, para representar los datos de manera efectiva.
Páginas:

Se crearon páginas específicas para organizar visualizaciones según categorías y temas.

1. Viajes – Tiempo de Espera: 

En los dashboards se visualizan la cantidad de viajes por año y cual es el tiempo de espera medido en segundos del cliente por cada viaje. Se puede filtrar por año, mes y dia. También vamos a poder ver el promedio de tiempo de cada viaje medido en segundos, el total de millas de los viajes y el promedio de millas por cada viaje.
Además, tenemos 2 KPI, que son indicadores de rendimiento, que nos permiten analizar si se llego al objetivo planteado en un determinado tiempo. En este caso tenemos el tiempo de espera del cliente medido en segundos, donde el objetivo es 300 segundos, cuando el valor supere dicho monto, se verá en rojo y por lo tanto no se llega al objetivo y de caso contrario en color verde. De forma similar funciona el KPI de cantidad de viajes con respecto al mes anterior, donde el objetivo es incrementar un 2% mensual, pasado dicho objetivo, el resultado se verá en verde, caso contrario de color rojo.

<p align="center"><img src=./src/viajes.png></p>

2. Demanda: 

En los dashboards se pueden visualizar la cantidad de viajes realizado en los 5 Borough más importantes de Nueva York. Se puede observar también, un mapa de los Borough, donde el color verde más oscuro muestra mayor cantidad de viajes, a su vez se puede filtrar por cada uno de los Borough y ver cuáles son las zonas con mayores demandas de viajes. Además indicadores de la cantidad de viajes, promedio de millas por viajes y el promedio de ingresos por viajes.
<p align="center"><img src=./src/demanda.png></p>

3. Ambiente:

En los siguientes gráficos se pueden ver cuáles fueron los promedio de las temperaturas en grados centígrados, el total de lluvias en milímetros y el total de nevades en centímetros, a su vez para dichos gráficos existen los filtros por año para ver la evolución y las tarjetas indicadores con los valores mencionados. 
También podemos ver en el gráfico de barras, la comparación de la emisión de C02 entre los autos eléctricos y autos a combustión, una tabla comparativa con dichos valores por año y el porcentaje de emisiones de C02 de los autos a combustión sobre los eléctricos.
<p align="center"><img src=./src/ambiente.png></p>

4. Autos:

En los siguientes dashboards se puede observar una comparación entre los precios de los autos eléctricos y autos a combustión. Se pueden filtrar por autos eléctricos y a combustión y por Marca. Vamos a visualizar los modelos más económicos. A su vez vamos a ver los gráficos de los promedios de emisión que producen cada marca y el promedio de los precios de los vehículos por marca.
<p align="center"><img src=./src/autos.png></p>

5. Ingresos:

En los dashboards vamos a ver el total de ingresos por año y el promedio de ingresos por viaje por mes. Dicha información la podemos filtrar por año y por mes, viendo los datos obtenidos en los indicadores correspondientes. A su vez, aquí también tenemos otro KPI, que nos va a medir la variación de los ingresos de un mes con respecto al anterior, siendo el objetivo mensual del 2%, por lo que por encima de dicho valor, se va observar el resultado con color verde y de forma contraria en color rojo.

También aquí vamos a ver una comparación que se obtuvo de unos de los modelos de Machine Learning para el mes de Octubre del 2023. Donde podemos ver el total de viajes predichos por el modelo, los viajes reales para el mismo periodo, la diferencia y el respectivo porcentaje.
<p align="center"><img src=./src/ingresos.png></p>
