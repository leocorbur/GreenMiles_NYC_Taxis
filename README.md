# <h1 align="center">**`GreenMiles NYC Taxis`**</h1>

Somos **CREATIVE DATA TECHNOLOGY**, una empresa joven que se dedica al proceso completo de Análisis de Proyectos, desde el diseño de una estructura de datos adecuados para la empresa hasta el diseño de un modelo de predicción de Machine Learning.

<p align=center><img src=./src/CreativeData.png><p>

El equipo de trabajo se compone de los siguientes integrantes: 
-	Roberto Schaefer
-	Diego Sebastian Drajlin Gordon
-	Bruno Mangione
-	Leonel Tonatiuh Cortez Burgos
-	Rafael Gabriel Alvarez Leon
-	Jorge Andrés González Gómez


# Introducción

GreenMiles NYC Taxis es una empresa de transporte de pasajeros de la ciudad de Nueva York, que actualmente se encuentra operando en el sector de micros de media y larga distancia y está interesada en invertir en el sector de transporte de pasajeros de automóviles. 
La empresa nos ha contratado para analizar los movimientos de los taxis actuales en la ciudad de Nueva York, analizar datos históricos y las tendencias futuras del mercado, para que podamos acompañarlos en el proceso de la toma de decisión. 

GreenMiles tiene una visión de un futuro menos contaminado y pretende que la inversión se ajuste a dicho modelo y las tendencias futuras en relación al cuidado del medioambiente. Para dicho trabajo la empresa nos provee una serie de datos principales y complementarios que debemos tener en cuenta a la hora de realizar nuestro trabajo y nos da libertad de acción para seleccionar y trabajar con los mismos.


<p align=center><img src=./src/LogoGreenMiles.png width="400"><p>



# Contexto

En la ciudad de Nueva York, los servicios de taxis y viajes compartidos, como Uber, han transformado la movilidad urbana al ofrecer una alternativa conveniente y accesible al transporte público y al alquiler de automóviles. Estos servicios generan grandes cantidades de datos en tiempo real, que pueden ser analizados para identificar patrones de viaje, demanda y mejorar la eficiencia del servicio.

Además, en respuesta al cambio climático acelerado por actividades humanas, la sostenibilidad se ha vuelto crucial en el desarrollo energético. Las compañías  y las autoridades locales de Nueva York están tomando medidas para medir y mejorar la eficiencia energética y reducir su impacto ambiental.

En este sentido, hemos sido contratados por la empresa GreenMiles NYC, para el estudio e interpretación de los datos disponibles y libres en las distintas fuentes.

La propuesta contempla la implementación de vehículos eléctricos tomando en cuenta la iniciativa viajes verdes impulsada por la Comisión de Limusinas y Taxis de la Ciudad (TLC, por sus siglas en inglés) y establece que, a partir de 2024, Nueva York requerirá que el 5 % de todos los viajes de alquiler de gran volumen, se envíen a vehículos eléctricos. 

Ese punto de referencia aumentará al 15% en 2025 y al 25% en 2026. Los requisitos aumentarán anualmente en 20 puntos porcentuales hasta el final de la década, alcanzando el 100% en 2030. Sumado a esto existen una serie de incentivos Federales y Estatales que fomentan la adquisición de vehículos eléctricos.

# Sprint 1

# Objetivo General

Nuestro objetivo es realizar un análisis integral que respalde la posible expansión de la flota de vehículos de nuestra empresa cliente, evaluando la relación entre los medios de transporte particulares, la calidad del aire y la contaminación sonora en Nueva York. Con este análisis, pretendemos proporcionar una base sólida para la toma de decisiones, considerando la posible transición a vehículos eléctricos.

# Objetivos Específicos

1. Análisis de la Demanda
   - Examinar y predecir patrones de demanda de servicios de taxi según la hora del día, día de la semana y condiciones climáticas.
   - Identificar tendencias estacionales o eventos específicos que puedan influir en la demanda de servicios de transporte.
   - Examinar el tiempo promedio de espera de los clientes.

2. Impacto Ambiental
    - Evaluar el uso de vehiculos eléctricos con la finalidad de reducir las emisiones CO2 y la contaminacion sonoro.
  
2. Inversion
   - Evaluar los diferentes modelos de vehículos eléctricos disponibles en el mercado, considerando aquellos que tengan un balance optimo entre costos y rendimiento.
   - Estimar el retorno de la inversión basado en la transición a vehículos eléctricos, teniendo en cuenta factores como el ahorro en costos operativos y potenciales ingresos adicionales derivados de la percepción pública positiva.

# Alcance del Proyecto

- Analizar el desempeño de los servicios de transporte de alto volumen, como los proporcionados por las empresas Uber y Lyft, a partir del año 2020.
- Estas compañías gestionan un flujo diario de más de 10,000 viajes en la ciudad de Nueva York.
- Estos estudios no han incluido otros vehículos que ofrecen servicios similares, como los taxis tradicionales de color amarillo y verde.
- Las diferencias entre los servicios de transporte de alto volumen y los taxis tradicionales se centran en aspectos como:
  - El modelo de negocio
  - Restricciones en las licencias
  - Limitaciones para ingresar al mercado
- Investigar las correlaciones entre el transporte de alto volumen y factores como las condiciones climáticas, la calidad del aire y la contaminación atmosférica.
- Realizar un estudio de factibilidad economica respecto a la inversion en el sector y en el ROI. 

# Actividades

1. **Datos de Taxis:**
- Utilizar datos de taxis y viajes compartidos en Nueva York.
- Utilizar datos de taxis y/o vehículos eléctricos.
2. **Calidad del Aire:**
- Obtener datos de calidad del aire de fuentes gubernamentales o estaciones meteorológicas.
- Integrar datos de contaminantes como CO2.
3. **Contaminación Sonora:**
- Utilizar datos de contaminación sonora en la ciudad, considerando zonas y horarios específicos.
- Incluir mediciones de decibelios para evaluar el impacto sonoro.
4. **Correlaciones Climáticas:**
- Obtener información de fuentes APIs de datos climáticos históricos y actuales.
- Analizar la relación entre eventos climáticos extremos, cambios en el transporte, la calidad del aire y la contaminación sonora.

# Stack Tecnológico

En nuestro proyecto, hemos seleccionado cuidadosamente un stack tecnológico que combina eficiencia y potencia para abordar los desafíos en el análisis de datos y la toma de decisiones. A continuación, se detallan las principales tecnologías que integran nuestro stack:

1. **Google Cloud Platform (GCP):**
   - Utilizaremos GCP como nuestra plataforma en la nube principal, aprovechando la confiabilidad y escalabilidad que ofrece. En particular, haremos uso de los siguientes servicios:

2. **Cloud Storage:**
   - Emplearemos Cloud Storage para el almacenamiento seguro y eficiente de nuestros conjuntos de datos. Configuraremos adecuadamente los permisos para garantizar la integridad y privacidad de la información.

3. **Dataproc:**
   - Aprovecharemos Dataproc para ejecutar nuestros scripts de Extracción, Transformación y Carga (ETL). Esta herramienta nos permitirá procesar grandes volúmenes de datos de manera distribuida y eficiente.

4. **BigQuery:**
   - Para la creación de nuestro DataWarehouse, confiaremos en BigQuery. Esta potente base de datos relacional nos proporcionará la capacidad de realizar consultas SQL rápidas y efectivas, facilitando el análisis y la extracción de información valiosa.

5. **Streamlit:**
   - Para la visualización de datos y el desarrollo de aplicaciones interactivas, hemos elegido Streamlit como nuestro framework principal. Su simplicidad y flexibilidad nos permitirán crear interfaces intuitivas y atractivas.

Este stack tecnológico integral nos brinda las herramientas necesarias para gestionar grandes conjuntos de datos, realizar análisis complejos y presentar de manera efectiva los resultados a través de interfaces interactivas. Estamos comprometidos a aprovechar al máximo estas tecnologías para respaldar nuestro análisis y facilitar la toma de decisiones basada en datos.

# KPIs Propuestos

Se proponen los siguientes KPIs en una medición mensual:

-  🎯 Reducir el promedio de tiempo de espera del cliente para tomar un viaje 
-  🎯 Incrementar el numero de viajes en un 2% con respecto al mes anterior
-  🎯 Incrementar la ganancias por viajes en 2% con respecto al mes anterior
-  🎯 Reducir el promedio de emisiones de CO2 

El siguiente KPI es de forma anual:

-  🎯 La flota de automóviles eléctricos se incremente en un 15% anualmente
-  🎯 El promedio de la autonomía de los vehículos sea > 300km

# Diagrama de Gantt

<p align=center><img src=./src/Diagrama-Gantt.jpg><p>

# Matriz de Responsabilidades

<p align=center><img src=./src/Matriz_de_Responsabilidades.jpg><p>

# Roles y Responsabilidades:

-	Roberto Schaefer: Data Scientist / Machine Learning
-	Diego Sebastian Drajlin Gordon: Data Scientist / Machine Learning
-	Bruno Mangione: Data Analyst / Business Intelligence
-	Leonel Tonatiuh Cortez Burgos: Data Engineer
-	Rafael Gabriel Alvarez Leon: Data Analyst / Business Intelligence
-	Jorge Andrés González Gómez: Data Engineer

# Información Adicional

Este README será actualizado regularmente para reflejar nuestro progreso y resultados. ¡Acompáñanos en nuestro viaje hacia un futuro más verde y sostenible en el transporte urbano de Nueva York! 🌍🚖

# Sprint 2

## Data Engineer

En el Sprint 2, el equipo de Data Engineering ha consolidado un sólido progreso en la implementación de soluciones para abordar los desafíos planteados en el análisis de datos. Centrándonos en el stack tecnológico previamente definido, hemos empleado Google Cloud Platform (GCP) como nuestra plataforma principal en la nube. Cloud Storage se ha utilizado de manera efectiva para almacenar y gestionar conjuntos de datos de manera segura.

Dataproc ha demostrado ser instrumental para la ejecución eficiente de scripts ETL, a través del uso de PySpark, permitiéndonos procesar grandes volúmenes de datos de manera distribuida. En paralelo, hemos aprovechado las capacidades de BigQuery como base de datos relacional para la creación de nuestro DataWarehouse, facilitando la realización de consultas SQL rápidas y efectivas.

<p align=center><img src=./src/Workflow.jpeg><p>

## Data Analytics 

En el Sprint 2, el equipo de DA, solicitó una primer reunión con el equipo de Data Engineer y Machine Learning para terminar de decidir que datasets se iba a utilizar tanto para la analítica como para los modelos de machine learning.
A partir de allí, el equipo de DA tuvo reuniones y solicitudes de datos al equipo de DE, para que disponga de los datos en Big Query. Una vez disponibles lo datos en Big Query, el equipo de DA, inició el trabajo de armado de power bi, obteniendo los datos directamente de Big Query. Al haber demasiada cantidad de datos y power bi no sopórtalo, se decidió trabajar las tablas directamente en Big Query y luego conectarlas con power bi.
Una vez obtenidas las tablas, se hicieron las relaciones y se comenzaron a trabajar en los diferentes dashboards y kpi planteados en el proyecto. 
Para el sprint final, el equipo de DA, seguirá trabajo en el diseño de los dashboards y completará el análisis junto con el equipo de machine learning para entregar las mejores propuesta a nuestro cliente.

<p align=center><img src=./src/EntidadRelacion.jpeg><p>

## Machine Learning 

En el Sprint 2, el equipo de machine learning, después de definir objetivos y modelos propuestos, inició el desarrollo del primer modelo. El mismo apunta a predecir la cantidad de vehículos necesarios durante ciertos periodos laborales, utilizando datos de fecha, día y hora almacenados en la tabla de vehículos de alto volumen en Big Query. De esta forma, la empresa ahorra dinero al no tener autos ociosos recorriendo las calles. Estos datos fueron procesados en un Jupyter Notebook usando Python y librerias como Pandas y Scikit-learn y el modelo se disponibilizó a través de Streamlit para la interacción con el usuario final.

La siguiente fase implica la integración de una nueva variable: el clima. Se analizará cómo las condiciones meteorológicas, como la lluvia o la nieve, afectan la necesidad de vehículos. Este análisis permitirá mejorar la precisión del modelo al considerar factores climáticos.

Además, el equipo está trabajando en un segundo modelo basado en programación lineal. El objetivo de este modelo es optimizar la composición de la flota de taxis, considerando restricciones como la menor emisión de CO2, mayor rango de desplazamiento y costo del vehículo. La optimización se realiza en función de la cantidad de inversión disponible y el porcentaje destinado a vehículos eléctricos.

<p align=center><img src=./src/Streamlit.jpeg><p>


# FROND-END. (AppGreenTaxis)
  
| archivos   |  
| --------- | 
| app.py| 
| dockerfile | 
| app-yaml|   
|  gcloudignore.txt|  
|  requirements.txt|  
|  github.json| 
|  coding.json| 
|  green.png| 
|  equipo.png| 

# Metodo.

Se dispone la creación de una interfaz gráfica que agrupe todos los servicios de la consultoría a través de una sola aplicación (APP). Se diseñó de manera ágil y rápida, ya que cada servicio dentro de la consultoría tuvo un proceso independiente en la carga de archivos y el procesamiento. Cada departamento llevó a cabo estas tareas de forma separada utilizando servicios como Power BI y Fabric para la analítica, Streamlit y Streamlit Cloud para los modelos de Machine Learning (MC).

La interfaz gráfica se desarrolló exclusivamente con Streamlit, y mediante etiquetas de incrustación, se integraron los demás servicios presentes en este desarrollo y consultoría. Esto se llevó a cabo con el objetivo de optimizar la velocidad y agilizar el proceso al realizar consultas.


<img width="700" alt="Captura de pantalla 2024-01-25 a la(s) 9 58 55 a m" src="https://github.com/leocorbur/GreenMiles_NYC_Taxis/assets/54252072/77544167-b967-47b2-9e57-a59de77576c2">












