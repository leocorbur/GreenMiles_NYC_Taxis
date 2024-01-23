En este archivo se encuentran las conclusiones obtenidas a partir del EDA del archivo
HVFHV de TLC. Se analizaron datasets del periodo 2020-2022.

<!-- omit in toc -->
## Tabla de contenidos 
- [Información general](#información-general)
- [Resumen de columnas](#resumen-de-columnas)
- [Recomendaciones](#recomendaciones)
- [Columnas](#columnas)
  - [hvfhs\_license\_num](#hvfhs_license_num)
  - [dispatching\_base\_num](#dispatching_base_num)
  - [originating\_base\_num](#originating_base_num)
  - [request\_datetime](#request_datetime)
  - [on\_scene\_datetime](#on_scene_datetime)
  - [pickup\_datetime](#pickup_datetime)
  - [dropoff\_datetime](#dropoff_datetime)
  - [PULocationID](#pulocationid)
  - [DOLocationID](#dolocationid)
  - [trip\_miles](#trip_miles)
  - [trip\_time](#trip_time)
  - [base\_passenger\_fare](#base_passenger_fare)
  - [tolls](#tolls)
  - [bcf](#bcf)
  - [sales\_tax](#sales_tax)
  - [congestion\_surcharge](#congestion_surcharge)
  - [airport\_fee](#airport_fee)
  - [tips](#tips)
  - [driver\_pay](#driver_pay)
  - [shared\_request\_flag](#shared_request_flag)
  - [shared\_match\_flag](#shared_match_flag)
  - [access\_a\_ride\_flag](#access_a_ride_flag)
  - [wav\_request\_flag](#wav_request_flag)
  - [wav\_match\_flag](#wav_match_flag)


## Información general
| Periodo | Registros | Duplicados |
|---------|-----------|------------|
|2020-01  | 20,569,368| 216        |
|2020-02  | 21,725,100| 0          |
|2020-03  | 13,392,928| 0          |
|2020-04  | 4,312,909 | 0          |
|2020-05  | 6,089,999 | 0          |
|2020-06  | 7,555,193 | 419        |
|2020-07  | 9,958,454 | 449        |
|2020-08  | 11,096,852 | 814       |
|2020-09  | 12,106,669 | 1258      |
|2020-10  | 13,268,411 | 1441      |
|2020-11  | 11,596,865 | 0         |
|2020-12  | 11,637,123 | 0         |
|2021-01  | 11,908,468 | 26        |
|2021-02  | 11,613,942 | 0         |
|2021-03  | 14,227,393 | 0         |
|2021-04  | 14,111,371 | 25        |
|2021-05  | 14,719,171 | 510       |
|2021-06  | 14,961,892 | 0         |
|2021-07  | 15,027,174 | 0         |
|2021-08  | 14,499,696 | 0         |
|2021-09  | 14,886,055 | 0         |
|2021-10  | 16,545,356 | 0         |
|2021-11  | 16,041,639 | 0         |
|2021-12  | 16,054,495 | 0         |
|2022-01  | 14,751,591 | 0         |
|2022-02  | 16,019,283 | 0         |
|2022-03  | 18,453,548 | 0         |
|2022-04  | 17,752,561 | 0         |
|2022-05  | 18,157,335 | 1872      |
|2022-06  | 17,780,075 | 0         |
|2022-07  | 17,464,619 | 0         |
|2022-08  | 17,185,687 | 0         |
|2022-09  | 17,793,551 | 0         |
|2022-10  | 19,306,090 | 0         |
|2022-11  | 18,085,896 | 0         |
|2022-12  | 19,665,847 | 0         |

## Resumen de columnas
* hvfhs_license_num: Es la licencia de TLC (Uber, Lyft).
* dispatching_base_num: Es la licencia TLC de la base que despacha el viaje.
* originating_base_num: Es la licencia TLC de la base donde se origina el viaje.
* request_datetime: Es la fecha y hora en la que se solicitó el viaje.
* on_scene_datetime: Es la fecha y hora en la que el vehículo llega al lugar.
* pickup_datetime: Es la fecha y hora en que se recoge al pasajero (inicio del viaje).
* dropoff_datetime: Es la fecha y hora en que el pasajero abandona el vehículo (fin del viaje).
* PULocationID: Es la zona de taxi TLC donde inició el viaje.
* DOLocationID: Es la zona de taxi TLC donde culminó el viaje.
* trip_miles: Es el número de millas recorridas.
* trip_time: Es el tiempo en segundos que dura el viaje.
* base_passenger_fare: Es la tarifa base, antes de peajes, propinas, tasas e impuestos.
* tolls: Monto total pagado en peajes.
* bcf: Monto total pagado al Black Car Fund (aseguradora).
* sales_tax: Monto total pagado al Estado de Nueva York por impuestos.
* congestion_surcharge: Pago adicional pagado al Estado de Nueva York por congestión.
* airport_fee: Pago adicional por pickup y dropoff en los aeropuertos LaGuardia, Newark y John F. Kennedy.
* tips: Monto pagado en propinas.
* driver_pay: Pago total al conductor.
* shared_request_flag: Si el pasajero aceptó o no compartir el viaje.
* shared_match_flag: Si el pasajero compartió o no el viaje.
* access_a_ride_flag: Si el viaje fue administrado por la Autoridad Metropolitana de Transporte.
* wav_request_flag: Si el usuario solicitó un vehículo accesible para silla de ruedas.
* wav_match_flag: Si el viaje sucedió en un vehículo accesible para silla de ruedas.

## Recomendaciones
Se recomienda trabajar con las siguientes columnas:
* hvfhs_license_num
* request_datetime
* pickup_datetime
* dropoff_datetime
* PULocationID
* DOLocationID
* trip_miles (investigar outliers)
* trip_time (investigar outliers o generar la columna a partir de la diferencia entre pickup_datetime y dropoff_datetime)
* base_passenger_fare (investigar outliers)

## Columnas

### hvfhs_license_num
* Es la licencia de TLC:
  * HV0002 (Juno): deja de operar en noviembre 2019 tras firmar una alianza con Lyft. 
  * HV0003 (Uber): maneja mas del 70% de los viajes.
  * HV0004 (Via): maneja menos del 1% de los viajes y operó hasta octubre del 2021.
  * HV0005 (Lyft): maneja 25-30% de los viajes.
* Es de tipo object.
* No contiene nulos.

### dispatching_base_num
* Es la licencia TLC de la base que despacha el viaje (p.e.: B02395).
* Cada base está asociada con una compañía distinta (Uber, Lyft).
* Es de tipo object.
* No presenta valores nulos.

### originating_base_num
* Es la licencia TLC de la base donde se origina el viaje (p.e.: B02395).
* Cada base está asociada con una compañía distinta (Uber, Lyft).
* Es de tipo object.
* Presenta 26-32% de valores nulos.

### request_datetime
* Es la fecha y hora en la que se solicitó el viaje.
* Es de tipo datetime.
* El promedio de nulos es cercano a 0.
* Hay superposiciones entre los meses.

### on_scene_datetime
* Es la fecha y hora en la que el vehículo llega al lugar.
* Es de tipo datetime.
* Presenta 26-32% de valores nulos.
* Hay superposiciones entre los meses.

### pickup_datetime
* Es la fecha y hora en que se recoge al pasajero (inicio del viaje).
* Es de tipo datetime.
* No presenta valores nulos.
* No presenta superposiciones entre meses.

### dropoff_datetime
* Es la fecha y hora en que el pasajero abandona el vehículo (fin del viaje).
* Es de tipo datetime.
* No presenta valores nulos.
* Hay superposiciones entre los meses.

### PULocationID
* Es la zona de taxi TLC donde inició el viaje.
* Es de tipo integer.
* Toma valores entre 1 y 265.
* No presenta valores nulos.

### DOLocationID
* Es la zona de taxi TLC donde culminó el viaje.
* Es de tipo integer.
* Toma valores entre 1 y 265.
* No presenta valores nulos.

### trip_miles
* Es el número de millas recorridas.
* Es de tipo float.
* No presenta valores nulos.
* Presenta valores de 0 que podrían ser errores.
* Presenta numerosos outliers según el método IQR.

### trip_time
* Es el tiempo en segundos que dura el viaje.
* Es de tipo int.
* No presenta valores nulos.
* No siempre coincide con la diferencia entre pickup_time y dropoff_time.
* Presenta valores de 0 que podrían ser errores.
* Presenta numerosos outliers según el método IQR.

### base_passenger_fare
* Es la tarifa base, antes de peajes, propinas, tasas e impuestos.
* Es de tipo float.
* No presenta valores nulos.
* Presenta valores negativos y outliers según el método IQR.

### tolls
* Monto total pagado en peajes.
* Es de tipo float.
* No presenta valores nulos.
* Presenta outliers según el método IQR.

### bcf
* Monto total pagado al Black Car Fund (aseguradora).
* Es de tipo float.
* No presenta valores nulos.
* Presenta outliers según el método IQR.

### sales_tax
* Monto total pagado al Estado de Nueva York por impuestos.
* Es de tipo float.
* No presenta valores nulos.
* Presenta outliers según el método IQR.

### congestion_surcharge
* Pago adicional pagado al Estado de Nueva York por congestión.
* Es de tipo float.
* No presenta valores nulos.
* Presenta outliers según el método IQR pero no están tan lejos de la distribución.

### airport_fee
* Pago adicional por pickup y dropoff en los aeropuertos LaGuardia, Newark y John F. Kennedy.
* Es de tipo float.
* Hay meses donde el promedio de nulos es superior al 99%.
* Presenta outliers según el método IQR.

### tips
* Monto pagado en propinas.
* Es de tipo float.
* No presenta valores nulos.
* Presenta outliers según el método IQR.

### driver_pay
* Pago total al conductor.
* Es de tipo float.
* No presenta valores nulos.
* Presenta valores negativos y outliers según el método IQR.

### shared_request_flag
* Si el pasajero aceptó o no compartir el viaje.
* Es de tipo object ("N"/"Y").
* No presenta valores nulos.
* En general, menos del 10% de los pasajeros solicita compartir viaje.

### shared_match_flag
* Si el pasajero compartió o no el viaje.
* Es de tipo object ("N"/"Y").
* No presenta valores nulos.
* Menos del 1% de los pasajeros compartieron viaje.

### access_a_ride_flag
* Si el viaje fue administrado por la Autoridad Metropolitana de Transporte.
* Es de tipo object ("N"/"Y").
* No presenta valores nulos.
* Presenta outliers (strings vacios)

### wav_request_flag
* Si el usuario solicitó un vehículo accesible para silla de ruedas.
* Es de tipo object ("N"/"Y").
* No presenta valores nulos.
* Menos del 1% de los usuarios solicitaron vehiculos accesibles.

### wav_match_flag
* Si el viaje sucedió en un vehículo accesible para silla de ruedas.
* Es de tipo object ("N"/"Y").
* No presenta valores nulos.
* No mas del 6% de los viajes se realizaron en vehículos accesibles.