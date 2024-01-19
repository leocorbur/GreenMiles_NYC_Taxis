# Data Engineering

Para abordar el desafío principal de procesar 45 archivos Parquet que van desde el año 2020 al 2023, cada uno de aproximadamente 500 MB, optamos por trasladar nuestro proyecto a la nube. Este enfoque nos permitió lograr un procesamiento rápido, ágil y eficiente.

## Google Cloud Platform (GCP)

Para la implementación de este proyecto, confiamos en Google Cloud Platform, aprovechando los servicios clave que ofrece:

### Configuración de Cloud Storage

Creamos una estructura organizada en la región `us-central1` para gestionar nuestros datos de manera eficiente.

Configuración:
```
|-- gs://files_raw/
│   ├── csv/
│   ├── json/
│   ├── parquet/
|-- gs://jobs_dataproc/
|-- gs://files_intermediate/

```

Esta organización nos permite separar claramente los datos en bruto, los scripts de PySpark en Dataproc, y los archivos temporales utilizados durante el procesamiento ETL.

### Configuración de Cloud Dataproc

Creamos un clúster con 1 nodo maestro y 0 nodos de trabajo en la región `us-central1`. La elección de nodos de trabajo es opcional y puede ajustarse según las necesidades.

Configuración

```
cluster_name = 'cluster-524f'
region = 'us-central1'
```


### Configuración de BigQuery

Utilizamos BigQuery en la región `us-central1` para almacenar y consultar datos a gran escala. La integración de BigQuery permite realizar análisis complejos sobre los datos procesados, brindando una capa adicional de flexibilidad y potencia. 


Configuracion

 ```
|-- bigquery_project = "spheric-base-407402"
│   ├──bigquery_dataset = "nyc_taxis"
│   |   ├──bigquery_table = "Auditoria"
│   |   ├──bigquery_table = "tlc"
│   |   ├──bigquery_table = "airPollution"
│   |   ├──bigquery_table = "weather"
│   |   ├──bigquery_table = "fuelConsumption"
│   |   ├──bigquery_table = "altFuelVehicles"
│   |   ├──bigquery_table = "carPrice"

```  
Se ejecutó las siguientes queries en bigquery [create_table.sql](create_tables.sql)

### Configuración de Cloud Composer

Creamos un entorno de Cloud Composer basado en Airflow con recursos mínimos para la operación. Este orquestador de flujo ejecutó nuestro script [main_dag.py](main_dag.py).


## Previo al Procesamiento de los Datos

### Scripsts de PySpark

Aseguramos que las rutas de entrada y salida de cada script coincidan con las rutas de los servicios.

Ruta de entrada:

- carpeta:  `files_raw/formato/nombre_archivo`


Ruta de salidad:

- temporaryGcsBucket: `files_intermediate`
- bigquery_project : `spheric-base-407402`
- bigquery_dataset : `nyc_taxis`
- bigquery_table   : `nombre_tabla`

### Scripts de comandos Shell
[Datos en Crudo a  Cloud Storage](rawData_to_cloudStorage.sh) 
- Verificamos que la ruta de salida sea la siguiente `files_raw/formato/nombre_archivo`

[Scripts de PySpark a Cloud Storage](pyScripts_to_cloudStorage.sh)
- Verificamos que la ruta de descarga de los scripts de pyspark sea la de nuestro repositorio y verificamos la salida `jobs_dataproc/`

###  Script DAG

Asegurarnos que las rutas de los jobs coincidan con las rutas de los servicios.
- `jobs_dataproc/nombre_script.py`
- `region = us-central1`
- `cluster_name= cluster-524f`



## Procesamiento de los Datos

Con los servicios habilitados, las carpetas creadas en Cloud Storage, el clúster en ejecución de Dataproc, las tablas creadas en BigQuery y el entorno de Cloud Composer activo, procedemos con el procesamiento de nuestros datos.

La ejecución se realizará a través de la Shell de GCP, utilizando los siguientes comandos.

### Comandos para Shell de GCP

Esta sección contiene scripts de shell para facilitar el proceso de transferencia de datos y scripts de Pyspark a Google Cloud Platform (GCP). A continuación, se detallan los comandos necesarios para ejecutar estos scripts.

#### 1. Transferencia de datos brutos a Cloud Storage
```bash
curl -O https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/rawData_to_cloudStorage.sh
chmod +x rawData_to_cloudStorage.sh
./rawData_to_cloudStorage.sh
```

#### 2. Transferencia de scripts Pyspark a Cloud Storage
```bash
curl -O https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/pyScripts_to_cloudStorage.sh
chmod +x pyScripts_to_cloudStorage.sh
./pyScripts_to_cloudStorage.sh
```

#### 3. Transferencia de script DAG a la carpeta dags
```bash
curl -O https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/main_dag.py
gsutil cp dag_greenMiles.py gs://us-central1-greenmiles-c4cc86ec-bucket/dags
```

## ¡Ponlo en Práctica!
¡Gracias por explorar nuestro proyecto! Ahora te invitamos a ponerlo en práctica en tu propio entorno. Sigue estos pasos para comenzar:

#### 1. Fork del Repositorio:
- Haz un fork de este repositorio en tu cuenta de GitHub. ¡Esto te permitirá trabajar en tu propia copia del proyecto!

#### 2. Clonar el Repositorio:
- Clona tu fork del repositorio en tu máquina local utilizando el siguiente comando:</br>
```git clone https://github.com/leocorbur/GreenMiles_NYC_Taxis.git```

#### 3. Habilitar Servicios en Google Cloud Platform:
- Asegúrate de tener habilitados los servicios necesarios en Google Cloud Platform (GCP). Consulta la documentación de GCP para obtener instrucciones detalladas sobre cómo habilitar los servicios que utiliza este proyecto.

#### 4. Cambiar Variables en los Scripts:
- Abre los scripts de configuración, como `rawData_to_cloudStorage.sh`, `pyScripts_to_cloudStorage.sh`, `main_dag.py`. Cambia las variables según tu configuración de GCP, como las rutas de los buckets, nombres de proyectos y tablas, entre otros.

#### 5. Hacer Push en tu Repositorio:
- Después de realizar las modificaciones, haz push en tu repositorio para reflejar los cambios. Usa los siguientes comandos: </br>
```git add .
git commit -m "Personalizando configuraciones para mi entorno GCP"
git push origin main
```
#### 6. Ejecutar el Flujo de Trabajo:
- ¡Es el momento de ejecutar el flujo de trabajo! Utiliza los comandos proporcionados en la sección "Comandos para Shell de GCP" para transferir datos, scripts y ejecutar el procesamiento en tu propio entorno.
</br>


¡Listo! Con estos pasos, estarás listo para ejecutar el proyecto en tu entorno de Google Cloud. Si encuentras algún problema o tienes sugerencias, ¡no dudes en abrir un problema o contribuir con mejoras! Estamos ansiosos por recibir tus comentarios.

Esperamos que disfrutes explorando y aplicando este proyecto en tu propio espacio de datos. ¡Bienvenido a la comunidad y feliz ingeniería de datos!