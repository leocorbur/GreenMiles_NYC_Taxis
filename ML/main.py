import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Cargar el DataFrame o usar tus datos
df = pd.read_csv('tlc_por_pickup.csv')

# Convierte la columna 'pickup_datehour' a formato de fecha y hora
df['pickup_datehour'] = pd.to_datetime(df['pickup_datehour'])

# Crea una nueva columna 'day_of_week' que contiene el día de la semana en texto
df['day_of_week'] = df['pickup_datehour'].dt.day_name()

# Extrae las columnas de año, mes y hora
df['year'] = df['pickup_datehour'].dt.year
df['month'] = df['pickup_datehour'].dt.month
df['hour'] = df['pickup_datehour'].dt.hour

# Convierte 'day_of_week' a one-hot encoding
df = pd.get_dummies(df, columns=['day_of_week']).astype("int")

# Seleccionar características (X) y variable objetivo (y)
X = df.drop(['num_trips', 'pickup_datehour'], axis=1)
y = df['num_trips']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar características (opcional)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y entrenar el modelo
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Función para hacer predicciones y mostrar resultados en Streamlit
def predict_num_trips(features):
    # Transformar las características de entrada (si es necesario)
    input_data = scaler.transform([features])
    # Realizar la predicción
    prediction = rf_model.predict(input_data)
    return prediction[0]

# Interfaz de usuario con Streamlit
st.title('Predictor de Viajes')

# Formulario para ingresar características
feature_input = {}

# Asegúrate de que las características coincidan con tu conjunto de datos
for feature in X.columns[:3]:
    entered_value = st.text_input(f'Ingrese {feature}', '0')
    # Intenta convertir el valor ingresado a un entero, si no es posible, asigna 0
    try:
        feature_input[feature] = int(entered_value)
    except ValueError:
        feature_input[feature] = 0

for feature in X.columns[3:]:
    feature_input[feature] = 0

# Lista de opciones para el selector
opciones = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Selector con opciones
opcion_seleccionada = st.selectbox('Selecciona una opción', opciones)

#feature_input[opcion_seleccionada] = 1

# Realizar la predicción cuando se hace clic en el botón
if st.button('Realizar Predicción'):
    prediction = predict_num_trips(list(feature_input.values()))
    st.success(f'Número de Viajes Predicho: {round(prediction)}')