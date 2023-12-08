# Diccionarios de Datos

Este DICCIONARIO proporciona una descripción detallada de los diccionarios de datos utilizados en [GreenMiles_NYC_Taxis]. Cada sección a continuación se centra en un diccionario de datos específico, detallando las claves, tipos de datos y cualquier información relevante. Utiliza esta guía para comprender la estructura y el significado de los datos dentro del proyecto.

## Índice

- [Diccionarios de Datos](#diccionarios-de-datos)
  - [Índice](#índice)
  - [Diccionario de Datos Clima : Open - Meteo](#diccionario-de-datos-clima--open---meteo)
    - [Estructura del Diccionario](#estructura-del-diccionario)
  - [Diccionario de Datos Contaminación - Open Weather](#diccionario-de-datos-contaminación---open-weather)
    - [Estructura del Diccionario](#estructura-del-diccionario-1)

   
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