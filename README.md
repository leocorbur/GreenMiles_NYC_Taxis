# <h1 align="center">*⁠ GreenMiles NYC Taxis ⁠*</h1>

Somos *CREATIVE DATA TECHNOLOGY*, una empresa joven que se dedica al proceso completo de Análisis de Proyectos, desde el diseño de una estructura de datos adecuados para la empresa hasta el diseño de un modelo de predicción de Machine Learning.

<p align=center><img src=./src/CreativeData.png><p>



---

La empresa Creative Technology ha sido contratada por Green Miles NYC con el propósito de evaluar la demanda de taxis eléctricos y de combustible en la ciudad de Nueva York, teniendo en cuenta aspectos ambientales, precios de vehículos y contaminación, entre otros. La finalidad de esta evaluación es incorporar una flota mixta de taxis a la empresa Green Miles NYC.

Nuestro equipo de Creative Tech se ha reunido para llevar a cabo la investigación, analizar el comportamiento vehicular y realizar predicciones que faciliten la toma de decisiones por parte de la empresa.

En la actualidad, Green Miles NYC Taxi no cuenta con una flota de taxis, por lo que está explorando, a través de Creative Tech, la mejor forma de inversión y la viabilidad del proyecto.

Creative Tech tiene la tarea de realizar un análisis detallado para la implementación de esta flota, considerando criterios como el comportamiento de viajes, la contaminación del aire y los efectos climatológicos. Este análisis contribuirá a la toma de decisiones estratégicas para lograr una inversión exitosa y sostenible en el mercado de transporte de taxis.

# Dashboard

En el análisis del comportamiento de los taxis en la ciudad de Nueva York, así como la evaluación de factores ambientales y la comparación entre autos a combustión y eléctricos, hemos identificado varios insights relevantes para el negocio:

1. Crecimiento Sostenido de Viajes:
Se observó un crecimiento constante en la cantidad de viajes, indicando un aumento continuo en la demanda del servicio.

<p align=center><img src=./src/viajesaño.png><p>

2. Tiempo de Espera del Cliente:
El tiempo de espera promedio por cliente se encuentra en torno a 300 segundos (6 minutos).
Se propuso un KPI para evaluar el desempeño, y se desarrolló un modelo de predicción de demanda para reducir el tiempo de espera.

<p align=center><img src=./src/tespera.png><p>

3. Análisis de Demanda por Zona:
Se estudió el comportamiento de la demanda por Borough y zonas para identificar áreas con mayor número de viajes.

<p align=center><img src=./src/demanda.png><p>

4. Impacto Ambiental:
Se evaluó el historial climático para entender su relación con los viajes.
Se comparó la producción de CO2 entre autos a combustión y eléctricos, destacando la importancia de considerar opciones más amigables con el medio ambiente.

<p align=center><img src=./src/ambiente.png><p>

5. Comparativa entre Autos:
Se realizó una comparativa detallada entre precios y rendimiento de autos a combustión y eléctricos para determinar la mejor opción de inversión.

<p align=center><img src=./src/autos.png><p>

6. Ingresos:
Se calculó el ingreso promedio por viaje y el ingreso total, proponiendo un KPI para evaluar el incremento en los ingresos por mes.

<p align=center><img src=./src/ingresos.png><p>


Los insights obtenidos del dashboard proporcionan una visión integral del rendimiento de la empresa de taxis en Nueva York. Se destaca la necesidad de implementar estrategias para reducir el tiempo de espera, considerar opciones de vehículos más amigables con el medio ambiente y evaluar continuamente las oportunidades de crecimiento de ingresos. La implementación de modelos predictivos y KPIs específicos será esencial para alcanzar los objetivos planteados y mejorar la eficiencia operativa en respuesta a la creciente demanda del servicio. Para obtener detalles más profundos, se invita a revisar el dashboard completo.

# Modelos de Machine Learning


# Ingeniería de Datos

En este proyecto, la ingeniería de datos ha sido fundamental para cumplir con las expectativas establecidas por los equipos de Analítica y Machine Learning.

## Proceso de Ingeniería de Datos

En primer lugar, se llevó a cabo la **recopilación de datos** provenientes de diversas fuentes y en distintos formatos. Posteriormente, la información recopilada se **almacenó** de manera segura y eficiente. Luego, se procedió al **procesamiento** de datos mediante la extracción de información relevante y su transformación para adecuarla a las necesidades específicas del proyecto. Finalmente, la información procesada fue depositada en una **base de datos estructurada**, proporcionando una base sólida y eficiente para el manejo de grandes conjuntos de datos. Este enfoque integral de ingeniería de datos ha sido fundamental para lograr los objetivos del equipo de Analítica y Machine Learning.

## Herramientas Utilizadas

Este flujo de trabajo ha sido implementado en la plataforma de Google Cloud, haciendo uso de los siguientes servicios:

- Almacenamiento: **Cloud Storage**
- Procesamiento: **Cloud Dataproc**
- Base de Datos: **BigQuery**
- Automatización: **Cloud Composer**

<p align=center><img src=./src/workflow.gif><p>

## Consumo de Datos

Una vez completada esta fase, los datos procesados y limpios fueron puestos a disposición de los usuarios de los equipos de Analítica y Machine Learning. Los usuarios han aprovechado las capacidades de BigQuery mediante **consultas**(queries) para trabajar directamente con sus datos. Estas capacidades se han integrado con herramientas como **Power Bi** y la plataforma **Streamlit**.

## Integración de Resultados

Para consolidar los resultados obtenidos por los equipos mencionados anteriormente, se utilizó el servicio de **Cloud Run**. Este servicio ha facilitado el despliegue de las soluciones desarrolladas en Power Bi y Streamlit, permitiendo la unificación y presentación conjunta de los resultados.

Este enfoque integral de ingeniería de datos ha proporcionado una base sólida para el análisis y la toma de decisiones, garantizando un flujo eficiente desde la recopilación inicial hasta la presentación final de los resultados.

# Conclusiones

# Contribuciones

- ⁠Roberto Schaefer
- ⁠Diego Sebastian Drajlin Gordon
- Bruno Mangione
- ⁠Leonel Tonatiuh Cortez Burgos
- ⁠Rafael Gabriel Alvarez Leon
- ⁠Jorge Andrés González Gómez