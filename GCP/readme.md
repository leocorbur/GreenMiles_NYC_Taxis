# Ingeniería de Datos en Google Cloud

La estructura que se presenta a continuación ha sido desarrollada para llevar a cabo el procesamiento de los **datos en crudo** hasta la disposición final para el usuario.

Los datos en crudo con los que trabajamos están en formato **CSV**, **JSON** y **Parquet**. Los archivos en formato Parquet son los más representativos del grupo, constituyendo el 99% del peso total (500 MB cada uno) y la cantidad de registros, en comparación con el resto de los datos.

Debido a esto, optamos por trabajar en la nube y aprovechar la oferta de 300 USD libres de consumo que **Google Cloud Platform** proporciona por el uso de su plataforma durante 90 días. Realizamos el registro en GCP y creamos nuestro proyecto **GreenMiles NYC Taxis** con el ID del proyecto **spheric-base-407402**.

Con este punto de partida, comenzamos a estudiar qué servicios podríamos utilizar y decidimos trabajar con los siguientes:

- **Cloud Storage**: Como datalake para nuestros **datos en crudo**.
- **Cloud Dataproc**: Para la ejecución de los **scripts de PySpark**.
- **BigQuery**: Para el almacenamiento estructurado de nuestros datos. 
- **Cloud Composer**: Para la orquestación de flujos de trabajo.

A partir de esta premisa, iniciamos el proceso de desarrollo de los **ETL** utilizando el lenguaje de programación **PySpark**, los cuales se encuentran en la carpeta [cs_to_bq](cs_to_bq). Cada uno de estos ETL está diseñado para manejar un conjunto específico de datos y sigue una estructura que implica la extracción de datos en bruto desde Cloud Storage, la aplicación de las transformaciones correspondientes a cada conjunto de datos y, finalmente, la carga de los datos resultante en BigQuery. Esto implica que los scripts de PySpark tienen **rutas de archivos** de Cloud Storage y **tablas especificas** en BigQuery.

Las ***rutas de archivos*** que tienen cada script de PySpark están denotadas por `gs://bucket/folder/file_name`, donde:
- **Bucket** : Es el contenedor de objetos de almacenanimiento. Para nuestro caso `files_raw`
- **Folder** : Dentro del bucket hemos creado carpetas, nombradas por el tipo de formato.
- **File_name** : Corresponde a los nombres de los archivos que almacenan los datos. 

Esto significa que primero creamos las carpetas en Cloud Storage para luego definirlas en los scripts de PySpark.

### Configuración de Cloud Storage

Creamos una estructura organizada en la región `us-central1` para gestionar nuestros datos de manera eficiente.

La estructura nos quedó de la siguiente manera:
```
|-- gs://files_raw/
│   ├── csv/
│   ├── json/
│   ├── parquet/
|-- gs://jobs_dataproc/
|-- gs://files_intermediate/

```

Esta organización nos permite separar claramente los datos en bruto en `gs://files_raw/` , los scripts de PySpark en Dataproc en `gs://jobs_dataproc/`, y los archivos temporales utilizados durante el procesamiento ETL `gs://files_intermediate/`.

Con respecto a las ***tablas específicas*** que tienen cada script de PySpark tienen la siguiente estructura: 
- **temporaryGcsBucket**: Se especifica la carpeta de archivos temporales `files_intermediate`
- **bigquery_project** : El ID de nuestro proyecto `spheric-base-407402`
- **bigquery_dataset** : El dataset nombrado `nyc_taxis`
- **bigquery_table**   : Los nombres de las tablas.

*Nota*: Todos los scripts cargan a datos a la tabla `Auditoria`.


### Configuración de BigQuery

Habilitamos BigQuery en la región `us-central1` para almacenar y consultar datos.</br>Ejecutamos las siguientes queries [create_table.sql](create_tables.sql).

La estructura nos quedó de la siguiente manera:

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

A continuación, procedemos a habilitar Could Dataproc


### Configuración de Cloud Dataproc

Creamos un clúster con 1 nodo maestro y 0 nodos de trabajo en la región `us-central1`. La elección de nodos de trabajo es opcional y puede ajustarse según las necesidades.

Datos a considerar para el script del orquestador de flujo:

```
cluster_name = 'cluster-524f'
region = 'us-central1'
```


### Configuración de Cloud Composer

Creamos un entorno de Cloud Composer basado en Airflow con recursos mínimos para la operación. Este orquestador de flujo ejecutó nuestro script [main_dag.py](main_dag.py).

Aseguramos que las rutas de los jobs coincidan con las rutas de Cloud Storage y con el nombre y región del clúster de Cloud Dataproc.
- `main = gs://jobs_dataproc/nombre_script_pyspark.py`
- `cluster_name= cluster-524f`
- `region = us-central1`


## Procesamiento de los Datos

Con los servicios habilitados, las carpetas creadas en Cloud Storage, el clúster en ejecución de Dataproc, las tablas creadas en BigQuery y el entorno de Cloud Composer activo, procedemos con el procesamiento de nuestros datos.

Para iniciar el pipeline y ejecutar el procesamiento de datos, utiliza los siguientes comandos en la Shell de GCP. Estos comandos son esenciales para transferir datos, scripts y realizar la ejecución en tu entorno. Asegúrate de ejecutar estos comandos en la Shell de GCP para poner en marcha el flujo de trabajo

### Comandos para Shell de GCP

Dentro de esta sección, encontrarás scripts de shell diseñados para simplificar el proceso de transferencia de archivos, así como scripts de PySpark y el script DAG destinados a la plataforma Google Cloud. A continuación, se detallan los comandos esenciales que necesitarás para ejecutar estos scripts de manera efectiva.

#### 1. Transferencia de archivos a Cloud Storage

Este script de shell realiza la descarga de los archivos directamente desde sus fuentes y los carga al bucket `files_raw `de Cloud Storage. </br>
Tener en cuenta que la descarga de archivos Parquet va del año 2020 al 2023, son 45 archivos y su peso promedio es de 500 MB cada uno, haciendo un total de 22.5 GB de descarga. El rango de fecha se puede editar directamente en el script.

```bash
curl -O https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/rawData_to_cloudStorage.sh
chmod +x rawData_to_cloudStorage.sh
./rawData_to_cloudStorage.sh
```

#### 2. Transferencia de scripts Pyspark a Cloud Storage

Este script de shell realiza la transferencia de los scripts de PySpark, desde nuestro **repositorio** hacia el bucket `jobs_dataproc`

```bash
curl -O https://raw.githubusercontent.com/leocorbur/GreenMiles_NYC_Taxis/main/GCP/pyScripts_to_cloudStorage.sh
chmod +x pyScripts_to_cloudStorage.sh
./pyScripts_to_cloudStorage.sh
```

#### 3. Transferencia de script DAG a la carpeta dags

Cuanda ya se ha creado el entorno de Cloud Composer, este crea automáticamente un bucket en Cloud Storage y es ahí donde apuntará nuestro comando en la shell, realiza la descarga del script desde nuestro **repositorio** y lo envía a este bucket. Para nuestro caso `us-central1-greenmiles-c4cc86ec-bucket`.

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
- Abre los scripts de configuración, como `rawData_to_cloudStorage.sh`, `pyScripts_to_cloudStorage.sh` y `main_dag.py`. Además de los scripts de la carpeta [cs_to_bq](cs_to_bq). Cambia las variables según tu configuración de GCP, como las rutas de los buckets, nombres de proyectos y tablas, entre otros.

#### 5. Hacer Push en tu Repositorio:
- Después de realizar las modificaciones, haz push en tu repositorio para reflejar los cambios. Usa los siguientes comandos: </br>
```git add .
git commit -m "Personalizando configuraciones para mi entorno GCP"
git push origin main
```
#### 6. Ejecutar el Flujo de Trabajo:
- Es el momento de ejecutar el flujo de trabajo. Utiliza los comandos proporcionados en la sección "Comandos para Shell de GCP" para transferir datos, scripts y ejecutar el procesamiento en tu propio entorno.
- Recuerda en la lineas de comando shell cambiar mi usuario por **tu usuario**. 
</br>


¡Listo! Con estos pasos, estarás listo para ejecutar el proyecto en tu entorno de Google Cloud. Si encuentras algún problema o tienes sugerencias, ¡no dudes en abrir un problema o contribuir con mejoras! Estamos ansiosos por recibir tus comentarios.

Esperamos que disfrutes explorando y aplicando este proyecto en tu propio espacio de datos. ¡Bienvenido a la comunidad y feliz ingeniería de datos!