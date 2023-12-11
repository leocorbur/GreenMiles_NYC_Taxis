# Diccionarios de Datos

Este DICCIONARIO proporciona una descripción detallada de los diccionarios de datos utilizados en [GreenMiles_NYC_Taxis]. Cada sección a continuación se centra en un diccionario de datos específico, detallando las claves, tipos de datos y cualquier información relevante. Utiliza esta guía para comprender la estructura y el significado de los datos dentro del proyecto.

## Índice

- [Diccionarios de Datos](#diccionarios-de-datos)
  - [Índice](#índice)
  - [Diccionario de High Volume FHV Trip Records](#diccionario-de-high-volume-fhv-trip-records)
    - [Estructura del Diccionario](#estructura-del-diccionario)
  - [Diccionario de Datos Clima : Open - Meteo](#diccionario-de-datos-clima--open---meteo)
    - [Estructura del Diccionario](#estructura-del-diccionario-1)
  - [Diccionario de Datos Contaminación - Open Weather](#diccionario-de-datos-contaminación---open-weather)
    - [Estructura del Diccionario](#estructura-del-diccionario-2)
  - [Diccionario de Datos Air Quality and Health Impacts](#diccionario-de-datos-air-quality-and-ealth-impacts)
    - [Estructura del Diccionario](#estructura-del-diccionario)


## Diccionario de High Volume FHV Trip Records

This data dictionary describes High Volume FHV trip data. Each row represents a single trip in an FHV dispatched by one of NYC’s licensed High Volume FHV bases. On August 14, 2018, Mayor de Blasio signed Local Law 149 of 2018, creating a new license category for TLC-licensed FHV businesses that currently dispatch or plan to dispatch more than 10,000 FHV trips in New York City per day under a single brand, trade, or operating name, referred to as High-Volume For-Hire Services (HVFHS). This law went into effect on Feb 1, 2019. </br>

For a dictionary describing yellow and green taxi data, or a map of the TLC Taxi Zones, please visit [NYC TLC Trip Record Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml).

### Estructura del Diccionario
| Field Name                    | Description                                                                                           |
|-------------------------------|-------------------------------------------------------------------------------------------------------|
| hvfhs_license_num              | The TLC license number of the HVFHS base or business As of September 2019, the HVFHS licensees are the  following:                                                                            
|                               | • HV0002: Juno                                                                                       |
|                               | • HV0003: Uber                                                                                       |
|                               | • HV0004: Via                                                                                        |
|                               | • HV0005: Lyft                                                                                       |
| dispatching_base_num           | The TLC Base License Number of the base that dispatched the trip                                         |
| originating_base_num           | The TLC Base License Number of the base that originated the trip                                         |
| request_datetime               | The date and time the trip was requested                                                               |
| on_scene_datetime               | The date and time the trip was arrived at the scene                                                               |
| pickup_datetime               | The date and time of the trip pick-up                                                                 |
| dropoff_datetime               | The date and time of the trip drop-off                                                                |
| PULocationID                  | TLC Taxi Zone in which the trip began                                                                 |
| DOLocationID                  | TLC Taxi Zone in which the trip ended                                                                 |
| trip_miles                     | Total miles for passenger trip                                                                        |
| trip_time                      | Total time in seconds for passenger trip                                                              |
| base_passenger_fare            | Base passenger fare before tolls, tips, taxes, and fees                                                |
| tolls                         | Total amount of all tolls paid in trip                                                                |
| bcf                           | Total amount collected in trip for Black Car Fund                                                     |
| sales_tax                     | Total amount collected in trip for NYS sales tax                                                      |
| congestion_surcharge           | Total amount collected in trip for NYS congestion surcharge                                            |
| airport_fee                    | $2.50 for both drop off and pick up at LaGuardia, Newark, and John F. Kennedy airports                  |
| tips                          | Total amount of tips received from passenger                                                           |
| driver_pay                    | Total driver pay (not including tolls or tips and net of commission, surcharges, or taxes)              |
| shared_request_flag            | Did the passenger agree to a shared/pooled ride, regardless of whether they were matched? (Y/N)          |
| shared_match_flag              | Did the passenger share the vehicle with another passenger who booked separately at any point during the trip? (Y/N) |
| access_a_ride_flag    | Was the trip administered on behalf of the Metropolitan Transportation Authority (MTA)? (Y/N)          |
| wav_request_flag      | Did the passenger request a wheelchair-accessible vehicle (WAV)? (Y/N)                               |
| wav_match_flag        | Did the trip occur in a wheelchair-accessible vehicle (WAV)? (Y/N)                                     |

## Diccionario de Datos Clima : Open - Meteo

Este documento aborda las variables climáticas relevantes que afectan el transporte de vehículos en la ciudad de Nueva York.
</br></br>
Las coordenadas geográficas de Nueva York son las siguientes:
- Latitud: 40.714°
- Longitud: -74.006°

Puedes obtener más información sobre estas coordenadas [aquí](https://www.geodatos.net/coordenadas/estados-unidos/nueva-york).
</br></br>
Fechas:

- start_date: 2020-01-01
- end_date: 2023-12-05

### Estructura del Diccionario

| Variable                              | Valid time            | Unit         | Description                                                                                                              |
|---------------------------------------|-----------------------|--------------|--------------------------------------------------------------------------------------------------------------------------|
| temperature_2m                        | Instant               | °C (°F)      | Air temperature at 2 meters above ground                                                                                 |
| relative_humidity_2m                  | Instant               | %            | Relative humidity at 2 meters above ground                                                                              |
| apparent_temperature                  | Instant               | °C (°F)      | Apparent temperature is the perceived feels-like temperature combining wind chill factor, relative humidity, and solar radiation |
| precipitation                         | Preceding hour sum    | mm (inch)    | Total precipitation (rain, showers, snow) sum of the preceding hour. Data is stored with a 0.1 mm precision. If precipitation data is summed up to monthly sums, there might be small inconsistencies with the total precipitation amount. |
| rain                                  | Preceding hour sum    | mm (inch)    | Only liquid precipitation of the preceding hour including local showers and rain from large scale systems.             |
| snowfall                              | Preceding hour sum    | cm (inch)    | Snowfall amount of the preceding hour in centimeters. For the water equivalent in millimeter, divide by 7. E.g. 7 cm snow = 10 mm precipitation water equivalent |
| snow_depth                            | Instant               | meters       | Snow depth on the ground. Snow depth in ERA5-Land tends to be overestimated. As the spatial resolution for snow depth is limited, please use it with care. |
| cloud_cover_low                       | Instant               | %            | Low level clouds and fog up to 2 km altitude                                                                            |
| wind_speed_10m                        | Instant               | km/h (mph, m/s, knots) | Wind speed at 10 or 100 meters above ground. Wind speed on 10 meters is the standard level.                         |
| wind_gusts_10m                        | Instant               | km/h (mph, m/s, knots) | Gusts at 10 meters above ground of the indicated hour. Wind gusts in CERRA are defined as the maximum wind gusts of the preceding hour. Please consult the ECMWF IFS documentation for more information on how wind gusts are parameterized in weather models. |



## Diccionario de Datos Contaminación - Open Weather

Este documento aborda las variables climáticas relevantes que afectan el transporte de vehículos en la ciudad de Nueva York.
</br></br>
Las coordenadas geográficas de Nueva York son las siguientes:
- **Latitud:** 40.714°
- **Longitud:** -74.006°

Puedes obtener más información sobre estas coordenadas [aquí](https://www.geodatos.net/coordenadas/estados-unidos/nueva-york).
</br></br>
Fechas:
- start_date: 2020-11-27
- end_date: 2023-12-05

### Estructura del Diccionario

- **coord:** Coordinates from the specified location (latitude, longitude)
- **list**
  - **dt:** Date and time, Unix, UTC
- **main**
  - **main.aqi:** Air Quality Index. Possible values: 1, 2, 3, 4, 5. Where 1 = Good, 2 = Fair, 3 = Moderate, 4 = Poor, 5 = Very Poor. If you want to recalculate Air Quality indexes according UK, Europe, USA and Mainland China scales please use "Air Pollution Index levels scale" page
- **components**
  - **components.co:** Concentration of CO (Carbon monoxide), μg/m3
  - **components.no:** Concentration of NO (Nitrogen monoxide), μg/m3
  - **components.no2:** Concentration of NO2 (Nitrogen dioxide), μg/m3
  - **components.pm2_5:** Concentration of PM2.5 (Fine particles matter), μg/m3
  - **components.pm10:** Concentration of PM10 (Coarse particulate matter), μg/m3

## Diccionario de Datos Diccionario de Air Quality and Health Impacts

The NYC Environment & Health Data Portal shows how environments affect health, by publishing data and information that explain the connection.  This dataset includes neighborhood averages of different air pollutants, estimates of emissions from buildings, traffic volumes and health impacts of air pollution.  To explore this data alongside other NYC Environment and Health indicators,   [go to](http://nyc.gov/health/environmentdata)


### Estructura del Diccionario
| Column Name                                          | Column Description                                                 |
|---------------------------------------------------------------------------------------------------------------------------|
| unique_id	                                           | Unique record identifier                                           |
| indicator_id	                                       | Identifier of the type of measured value across time and space     |
| name	                                               | Name of the indicator                                              |
| measure	                                             | How the indicator is measured                                      |
| measure_info	                                       | Information (such as units) about the measure                      |
| geo_type_name	                                       | Geography type                                                     |
| geo_place_name	                                     | Neighborhood name                                                  |
| data_value	                                         | The actual data value for this indicator, measure, place, and time |
| Stations	                                           | Winter, Summer                                                     |
| Final Date                                           | Year

 
