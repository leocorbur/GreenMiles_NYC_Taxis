# Importar librerias estándar
import datetime
import pandas as pd

# Importar librerias de manejo de solicitudes y caché
import openmeteo_requests
import requests_cache
from retry_requests import retry

# Importar librerias de visualización
import plotly.express as px

# Importar librerias de machine learning
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Importar librerias de Streamlit
import streamlit as st


### Cargar el df y crear el modelo
# Cargar el df
df = pd.read_csv("prediccion_demanda.csv")

# Seleccionar características (X) y variable objetivo (y)
X = df.drop(['num_trips'], axis=1)
y = df['num_trips']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
rf_model = RandomForestRegressor(max_depth= None, min_samples_leaf= 1, 
                                 min_samples_split= 2, n_estimators= 200, 
                                 random_state=42)
rf_model.fit(X_train, y_train)


### Crear df vacio para alojar los resultados
res = pd.DataFrame({'relative_humidity_2m': 0.0, 'apparent_temperature':0.0,
                    'year':0, 'month':0, 'day':0, 'hour':0, 'Friday':0, 'Monday':0, 
                    'Saturday':0, 'Sunday':0, 'Thursday':0, 'Tuesday':0,
                    'Wednesday':0}, index=[0])


### Widgets para seleccionar fecha y hora
today = datetime.datetime.now()
end_date = today + datetime.timedelta(days=14)

st.write("Ingrese fecha y hora a predecir")
date = st.date_input(label='Fecha', min_value=today, max_value=end_date, 
                     label_visibility="collapsed")
hour_widget = st.time_input(label="Hora UTC", label_visibility="collapsed",
                            value=datetime.time(0,0),step=3600)


### Agregar año, mes, dia, hora y dia de la semana a res
res.iloc[0,2] = date.year
res.iloc[0,3] = date.month
res.iloc[0,4] = date.day
res.iloc[0,5] = hour_widget.hour


### Crear selected_datetime y agregar dia de la semana a res
selected_datetime = datetime.datetime(date.year, date.month, date.day, 
                                      hour_widget.hour,0,0)

weekday = date.weekday()

days = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday',
        5:'Saturday', 6:'Sunday'}

res.loc[:,days.get(weekday)] = 1


### Importar datos de clima y agregarlos a res
# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 40.714,
	"longitude": -74.006,
	"hourly": ["relative_humidity_2m", "apparent_temperature"],
	"timezone": "GMT",
	"start_date": today.strftime("%Y-%m-%d"),
	"end_date": end_date.strftime("%Y-%m-%d")
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_relative_humidity_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_apparent_temperature = hourly.Variables(1).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s"),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s"),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
)}
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["apparent_temperature"] = hourly_apparent_temperature

hourly_df = pd.DataFrame(data = hourly_data)

weather_for_hour = hourly_df[hourly_df.date == selected_datetime].reset_index(drop=True)

res.iloc[0,0] = weather_for_hour.iloc[0,1] # Humedad
res.iloc[0,1] = weather_for_hour.iloc[0,2] # Temperatura aparente


### Mostrar la temperatura aparente y la humeda relativa
st.write("Humedad relativa porcentual a 2 m:", round(res.iloc[0,0], 2))
st.write("Temperatura aparente (°C):", round(res.iloc[0,1], 2))


### Función de predicción y predicción
def predict_num_trips(res):
    pred = rf_model.predict(res)
    return pred[0]

# Realizar la predicción cuando se hace clic en el botón
if st.button('Realizar Predicción'):
    prediction = predict_num_trips(res)
    st.success(f'Número de Viajes Predicho: {round(prediction)}')


### Mostrar las tendencias diarias
# Definir una fila con los valores deseados
row_data = {'relative_humidity_2m': 0.0, 'apparent_temperature': 0.0,
            'year': 0, 'month': 0, 'day': 0, 'hour': 0, 'Friday': 0, 'Monday': 0,
            'Saturday': 0, 'Sunday': 0, 'Thursday': 0, 'Tuesday': 0,
            'Wednesday': 0}

# Crear un DataFrame con 24 filas iguales
res_day = pd.DataFrame([row_data] * 24)

# Agregar año, mes, dia a res_day
res_day.iloc[:,2] = date.year
res_day.iloc[:,3] = date.month
res_day.iloc[:,4] = date.day

# Agregar hora a res_day
for i in range(24):
    res_day.iloc[i,5] = i

# Agregar dia de la semana a res_day
res_day.loc[:,days.get(weekday)] = 1

# Agregar humedad y temperatura a res_day
weather_for_day = hourly_df[(hourly_df['date'].dt.year == selected_datetime.year) &
                            (hourly_df['date'].dt.month == selected_datetime.month) &
                            (hourly_df['date'].dt.day == selected_datetime.day)]\
                                .reset_index(drop=True)

for i in range(24):
    res_day.iloc[i,0] = weather_for_day.iloc[i,1] # Humedad
    res_day.iloc[i,1] = weather_for_day.iloc[i,2] # Temperatura aparente


# Mostrar la nueva tabla con las columnas 'hour' y 'num_trips'
if st.button('Ver tendencia diaria'):
    # Crear una nueva columna 'num_trips' en res_day con las predicciones del modelo
    res_day['num_trips'] = rf_model.predict(res_day[['relative_humidity_2m', 'apparent_temperature',
                                                 'year', 'month', 'day', 'hour',
                                                 'Friday', 'Monday', 'Saturday',
                                                 'Sunday', 'Thursday', 'Tuesday',
                                                 'Wednesday']]).round().astype(int)

    # Renombrar las columnas
    res_day = res_day.rename(columns={'hour': 'Hora', 'num_trips': 'Número de viajes'})

    result_table = res_day[['Hora', 'Número de viajes']]

    # Crear el gráfico interactivo con Plotly Express
    fig = px.line(result_table, x='Hora', y='Número de viajes', markers=True, title='Número de viajes en función de la hora')

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)