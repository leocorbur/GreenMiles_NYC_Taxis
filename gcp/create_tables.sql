CREATE TABLE IF NOT EXISTS `nyc_taxis.airPollution` (
  `date` DATE,
  `hour_of_day` INT64,
  `aqi` INT64,
  `co` FLOAT64,
  `no` FLOAT64,
  `no2` FLOAT64,
  `pm2_5` FLOAT64,
  `pm10` FLOAT64
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.altFuelVehicles` (
    `Category` STRING,
    `Model` STRING,
    `Model Year` INT64,
    `Manufacturer` STRING,
    `Fuel` STRING,
    `All Electric Range` INT64,
    `Alternative Fuel Economy Combined` FLOAT64,
    `Conventional Fuel Economy Combined` FLOAT64,
    `Transmission Type` STRING,
    `Engine Size` STRING
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.carPrice` (
    `Year` INT64,
    `Manufacturer` STRING,
    `Model` STRING,
    `co2` INT64,
    `co2TailpipeGpm` INT64,
    `fuelCost08` INT64,
    `fuelCostA08` INT64,
    `fuelType` STRING,
    `ghgScore` INT64,
    `highway08` INT64,
    `range` INT64,
    `Price` FLOAT64
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.fuelConsumption` (
  `Year` INT64,
  `Make` STRING,
  `Model` STRING,
  `Vehicle Class` STRING,
  `Engine Size` FLOAT64,
  `Cylinders` INT64,
  `Transmission` STRING,
  `Fuel` STRING,
  `Fuel Consumption` FLOAT64,
  `Fuel_Con_Hwy` FLOAT64,
  `Fuel_Con_Comb` FLOAT64,
  `Fuel_Con_Comb_Mpg` INT64,
  `CO2 Emissions` INT64,
  `CO2` INT64,
  `Smog` INT64
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.weather` (
  `date` DATE,
  `hour_of_day` INT64,
  `relative_humidity_2m` FLOAT64,
  `apparent_temperature` FLOAT64,
  `rain` FLOAT64,
  `snowfall` FLOAT64,
  `snow_depth` FLOAT64,
  `cloud_cover_low` FLOAT64,
  `wind_speed_10m` FLOAT64,
  `wind_gusts_10m` FLOAT64
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.tlc` (
  `hvfhs_license_num` STRING,
  `request_datetime` TIMESTAMP,
  `pickup_datetime` TIMESTAMP,
  `dropoff_datetime` TIMESTAMP,
  `PULocationID` INT64,
  `DOLocationID` INT64,
  `trip_miles` FLOAT64,
  `trip_time` INT64,
  `base_passenger_fare` FLOAT64,
  `waiting_time` INT64,
  `pickup_datehour` TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `nyc_taxis.Auditoria` (
    `file_name` STRING,
    `file_format` STRING,
    `initial_record_count` INT64,
    `final_record_count` INT64,
    `initial_column_count` INT64,
    `final_column_count` INT64,
    `null_values_sum` INT64,
    `duplicate_records_count` INT64,
    `execution_time_seconds` FLOAT64,
    `execution_date` DATE
);