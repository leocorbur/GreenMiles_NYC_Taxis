## Data Engineer

En el Sprint 2, el equipo de Data Engineering ha consolidado un sólido progreso en la implementación de soluciones para abordar los desafíos planteados en el análisis de datos. Centrándonos en el stack tecnológico previamente definido, hemos empleado Google Cloud Platform (GCP) como nuestra plataforma principal en la nube. Cloud Storage se ha utilizado de manera efectiva para almacenar y gestionar conjuntos de datos de manera segura.

Dataproc ha demostrado ser instrumental para la ejecución eficiente de scripts ETL, a través del uso de PySpark, permitiéndonos procesar grandes volúmenes de datos de manera distribuida. En paralelo, hemos aprovechado las capacidades de BigQuery como base de datos relacional para la creación de nuestro DataWarehouse, facilitando la realización de consultas SQL rápidas y efectivas.

<p align=center><img src=../src/Workflow.jpeg><p>

## Data Analytics 

En el Sprint 2, el equipo de DA, solicitó una primer reunión con el equipo de Data Engineer y Machine Learning para terminar de decidir que datasets se iba a utilizar tanto para la analítica como para los modelos de machine learning.
A partir de allí, el equipo de DA tuvo reuniones y solicitudes de datos al equipo de DE, para que disponga de los datos en Big Query. Una vez disponibles lo datos en Big Query, el equipo de DA, inició el trabajo de armado de power bi, obteniendo los datos directamente de Big Query. Al haber demasiada cantidad de datos y power bi no sopórtalo, se decidió trabajar las tablas directamente en Big Query y luego conectarlas con power bi.
Una vez obtenidas las tablas, se hicieron las relaciones y se comenzaron a trabajar en los diferentes dashboards y kpi planteados en el proyecto. 
Para el sprint final, el equipo de DA, seguirá trabajo en el diseño de los dashboards y completará el análisis junto con el equipo de machine learning para entregar las mejores propuesta a nuestro cliente.

<p align=center><img src=../src/EntidadRelacion.jpeg><p>

## Machine Learning 

En el Sprint 2, el equipo de machine learning, después de definir objetivos y modelos propuestos, inició el desarrollo del primer modelo. El mismo apunta a predecir la cantidad de vehículos necesarios durante ciertos periodos laborales, utilizando datos de fecha, día y hora almacenados en la tabla de vehículos de alto volumen en Big Query. De esta forma, la empresa ahorra dinero al no tener autos ociosos recorriendo las calles. Estos datos fueron procesados en un Jupyter Notebook usando Python y librerias como Pandas y Scikit-learn y el modelo se disponibilizó a través de Streamlit para la interacción con el usuario final.

La siguiente fase implica la integración de una nueva variable: el clima. Se analizará cómo las condiciones meteorológicas, como la lluvia o la nieve, afectan la necesidad de vehículos. Este análisis permitirá mejorar la precisión del modelo al considerar factores climáticos.

Además, el equipo está trabajando en un segundo modelo basado en programación lineal. El objetivo de este modelo es optimizar la composición de la flota de taxis, considerando restricciones como la menor emisión de CO2, mayor rango de desplazamiento y costo del vehículo. La optimización se realiza en función de la cantidad de inversión disponible y el porcentaje destinado a vehículos eléctricos.

<p align=center><img src=../src/Streamlit.jpeg><p>





