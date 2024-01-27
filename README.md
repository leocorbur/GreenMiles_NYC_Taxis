# <h1 align="center">⁠GreenMiles NYC Taxis</h1>

Somos **CREATIVE DATA TECHNOLOGY**, una empresa joven especializada en el proceso integral de Análisis de Proyectos. Desde la concepción de estructuras de datos adaptadas a las necesidades empresariales hasta el diseño de modelos de predicción mediante Machine Learning.

<p align=center><img src=./src/CreativeData.png><p>



---

La empresa Creative Data Technology ha sido seleccionada por Green Miles NYC Taxis con el propósito de evaluar la demanda de taxis eléctricos y de combustible en la ciudad de Nueva York, considerando factores ambientales, precios de vehículos y niveles de contaminación, entre otros. El objetivo de esta evaluación es introducir una flota diversificada de taxis en la empresa Green Miles NYC.

Nuestro equipo en Creative Data Technology se ha congregado para llevar a cabo esta investigación, analizando el comportamiento vehicular y generando predicciones que facilitarán la toma de decisiones de la empresa.

Actualmente, Green Miles NYC Taxis no dispone de una flota de taxis, por lo que, a través de Creative Data Technology, busca la mejor estrategia de inversión y evalúa la viabilidad del proyecto.

Creative Data Technology se ha encargado de realizar un análisis exhaustivo para la implementación de esta flota, teniendo en cuenta criterios como el comportamiento de los viajes, la calidad del aire y los efectos climáticos. Este análisis contribuirá significativamente a la toma de decisiones estratégicas, con el objetivo de lograr una inversión exitosa y sostenible en el mercado del transporte de taxis.

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

Como parte de este proyecto, se desarrollaron 2 modelos de Machine Learning 
alineados con los intereses de la empresa:
* Predicción de la demanda de vehículos
* Optimización de la flota

## Predicción de la demanda de vehículos
El tráfico en la ciudad de Nueva York es fluctuante según el momento del día, 
época del año y las condiciones climáticas imperantes. Como consecuencia, la
oferta de vehículos de transporte debe adecuarse a las necesidades, a fin de 
poder suplir la demanda, sin sobreofertar, con los consecuentes gastos de tener
parte de la flota en la calle de manera ociosa. Con esto en mente, se desarrolló
un modelo de Machine Learning capaz de tener en cuenta los factores más importantes
que explican la demanda de vehículos:
* Variables temporales (año, mes, dia, hora y dia de la semana)
* Variables climáticas (humedad relativa y temperatura aparente)

Estos factores demostraron ser aquellos con mayor contribución al poder explicativo
de un modelo de Machine Learning. Se trabajó con Random Forest, optimizando los
hiperparámetros con GridSearchCV y se obtuvo que las mejores variables son:
* max_depth: None 
* min_samples_leaf: 1 
* min_samples_split: 2
* n_estimators: 200

El modelo resultante tiene un R<sup>2</sup> de 0.95 y RMSE, como porcentaje del 
rango de datos, del 3.72%.

Este modelo se deployó en Streamlit. Los datos temporales (fecha y hora) son 
introducidos por el usuario. Con esta información, el sistema se comunicá a 
través de la API de OpenMeteo para adquirir la previsión climática para la fecha
y hora indicada, y dichos datos son incorporados a la predicción.

Los resultados son el número de viajes predicho para un dia y hora, y la 
tendencia diaria. Con esta información, la empresa podrá adecuar la oferta de
vehículos en la calle en función de su disponibilidad y de las necesidades del
mercado.

<p align=center><img src=./src/prediccion_demanda.gif><p>

## Optimización de la flota
Al trabajar con una empresa que está buscando ingresar al mercado, y por lo
tanto debe adquirir vehículos nuevos, este modelo funciona como un sistema de
recomendación, orientando al inversión en función de distintas variables:  

* Inversión: se refiere al monto total, en dolares, que la empresa disponibiliza
para la adquisición de nuevos vehículos.
* Porcentaje de autos eléctricos: En función de las regulaciones de la ciudad de
Nueva York, tendientes a fomentar la adquisición de vehículos eléctricos, este
parámetro le permite a la empresa determinar el porcentaje de recursos a asignar
a vehículos eléctricos y a combustión.
* Porcentaje de autos según gama: Entendiendo que los vehículos dedicados al
transporte de pasajeros suelen estar en las gamas baja y media, este parámetro
le permite al transportista determinar el porcentaje de la inversión destinada
a cada segmento.

Alimentando el sistema con datos sobre los vehículos, desde su rango de desplazamiento hasta sus emisiones de CO2 y precio, el modelo emplea algoritmos para determinar la combinación ideal que maximiza cada especificación según preferencias y criterios, considerando factores como minimizar costes, maximizar alcance de los vehículos y minimizar sus emisiones de CO<sub>2</sub>, contribuyendo a las normativas medioambientales y a la sustentabilidad del proyecto.

Es esencial destacar la capacidad de nuestro modelo de optimización de flotas para escalar de manera efectiva. En este sentido, cuenta con la posibilidad de ampliar significativamente la base de datos, abarcando una variedad más extensa de vehículos, desde modelos recientes hasta opciones más antiguas, tanto de gasolina como eléctricos. Esta expansión no solo le permitirá al modelo manejar una mayor cantidad de datos, sino que también garantizará que continúe entregando de manera óptima la lista de los mejores vehículos para componer la flota. Esta capacidad única de adaptarse y optimizar las recomendaciones en función de la evolución del mercado automotriz asegura que las decisiones sobre la consolidación de la flota estén respaldadas por información actualizada y relevante.

<p align=center><img src=./src/optimizacion_flota.gif><p>

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

Para obtener más detalles sobre el procesamiento, se puede explorar la carpeta [gcp](https://github.com/leocorbur/GreenMiles_NYC_Taxis/tree/main/gcp) y visualizar el proceso a través del video disponible [aquí](https://www.youtube.com/watch?v=DkJ5IzbSARo)

# Conclusiones

<p align=center><img src=Dasboard/src/PlanInversion.jpg><p>

---

Nuestro producto cuenta con herramientas clave para la toma de decisiones basadas en datos. Por un lado, proporciona herramientas de análisis a través de dashboards y KPIs para un seguimiento efectivo de la información recolectada, lo que permite entender y adaptarse a las cambiantes necesidades del mercado. Por otro lado, ofrece dos soluciones de Machine Learning: predicción de la demanda de vehículos y optimización de la flota.

A partir de estos recursos y las conclusiones obtenidas, determinamos que una inversión inicial de 40 millones de dólares nos permitiría adquirir 1383 autos, cumpliendo con la normativa de Nueva York a partir del 2024, que requiere que al menos el 5 % de todos los viajes de alquiler de gran volumen, incluidos los de Uber y Lyft, se realicen en vehículos eléctricos o vehículos accesibles para sillas de ruedas. Este punto de referencia aumentará al 15% en 2025 y al 25% en 2026. Con esta cantidad de vehículos, superaríamos los 10,000 viajes diarios mínimos requeridos para ser considerados una empresa de High Volume. Esto nos posiciona para ofrecer un servicio óptimo y competitivo en un mercado en crecimiento.

Además, consideramos que es un mercado altamente competitivo donde la disponibilidad inmediata de vehículos para traslados juega un papel crucial, la cantidad de autos registrados es fundamental. Con el número de autos que proyectamos adquirir, estamos bien posicionados para ofrecer un servicio óptimo y seguir creciendo paulatinamente.

  
# Contribuciones
<p align=center><img src=./src/developers.png><p>

#### Perfiles de GitHub

- [⁠Roberto Schaefer](https://github.com/roscha10)
- [⁠Sebastian Drajlin](https://github.com/dsdrajlin)
- [Bruno Mangione](https://github.com/brunomangione)
- [⁠Leonel Cortez](https://github.com/leocorbur)
- [⁠Rafael Alvarez](https://github.com/rafaelalvarez702)
- [⁠Jorge González](https://github.com/teamlider)

#### [Link al Deploy](https://spheric-base-407402.uc.r.appspot.com)
