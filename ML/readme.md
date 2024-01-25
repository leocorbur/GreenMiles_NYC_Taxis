# Machine Learning
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

Alimentando el sistema con datos sobre los vehículos, desde su rango de desplazamiento hasta sus emisiones de CO2 y precio, el modelo emplea algoritmos para determinar la combinación ideal que maximiza cada especificación según tus preferencias y criterios, considerando factores como minimizar costes, maximizar alcance de los vehículos y minimizar sus emisiones de CO<sub>2</sub>, contribuyendo a las normativas medioambientales y a la sustentabilidad del proyecto.

Es esencial destacar la capacidad de nuestro modelo de optimización de flotas para escalar de manera efectiva. En este sentido, al momento de ampliar significativamente la base de datos, abarcando una variedad más extensa de vehículos, desde modelos recientes hasta opciones más antiguas, tanto de gasolina como eléctricos. Esta expansión no solo le permitirá al modelo manejar una mayor cantidad de datos, sino que también garantizará que continúe entregando de manera óptima la lista de los mejores vehículos para componer la flota. Esta capacidad única de adaptarse y optimizar las recomendaciones en función de la evolución del mercado automotriz asegura que las decisiones sobre la consolidación de la flota estén respaldadas por información actualizada y relevante.
