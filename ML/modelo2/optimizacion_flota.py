# Importar librerias estándar
import pandas as pd
import streamlit as st

# Cargar el df
data_car = pd.read_excel("data_car_completa.xlsx")

# Establecer formato decimal
pd.set_option('display.float_format', '{:.2f}'.format)

# Calcula los percentiles para determinar los límites
percentiles = data_car['Price'].quantile([0, 0.33, 0.66, 1])

# Asigna etiquetas a las categorías según los percentiles y crea la nueva columna 'Gama'
data_car['Gama'] = pd.cut(data_car['Price'], bins=percentiles, labels=['Gama Baja', 'Gama Media', 'Gama Alta'], include_lowest=True)

# Seleccionar el mejor vehículo eléctrico para una categoría y tipo de combustible específicos
def seleccionar_mejor_vehiculo(data_car, gama, tipo_combustible, inversion_a_gastar):
    vehiculos_filtrados = data_car[(data_car['Gama'] == gama) & (data_car['fuelType'] == tipo_combustible)]
    if vehiculos_filtrados.empty:
        print(f"No se encontraron vehículos que cumplan con los criterios para Gama {gama}.")
        return pd.DataFrame()

    vehiculos_filtrados = vehiculos_filtrados.sort_values(by='Price')
    vehiculos_filtrados = vehiculos_filtrados.sort_values(by=['co2', 'range'], ascending=[True, False])
    mejor_vehiculo = vehiculos_filtrados.iloc[0].copy()

    cantidad_vehiculos = int(inversion_a_gastar / mejor_vehiculo['Price'])
    vehiculos_sugeridos = [mejor_vehiculo] * cantidad_vehiculos

    return pd.DataFrame(vehiculos_sugeridos)

# Seleccionar los mejores vehículos según la inversión inicial y porcentajes dados
def seleccionar_mejores_vehiculos(data_car, inversion_inicial, porcentaje_electrico, porcentaje_gama_media):
    porcentaje_electrico_decimal = porcentaje_electrico / 100
    porcentaje_gama_media_decimal = porcentaje_gama_media / 100

    monto_gama_media = inversion_inicial * porcentaje_gama_media_decimal
    monto_electricos_gama_media = monto_gama_media * porcentaje_electrico_decimal
    monto_gasolina_gama_media = monto_gama_media * (1 - porcentaje_electrico_decimal)

    monto_gama_baja = inversion_inicial * (1 - porcentaje_gama_media_decimal)
    monto_electricos_gama_baja = monto_gama_baja * porcentaje_electrico_decimal
    monto_gasolina_gama_baja = monto_gama_baja * (1 - porcentaje_electrico_decimal)

    resultados_electricos_gama_media = seleccionar_mejor_vehiculo(data_car, 'Gama Media', 'Electricity', monto_electricos_gama_media)
    resultados_gasolina_gama_media = seleccionar_mejor_vehiculo(data_car, 'Gama Media', 'Regular', monto_gasolina_gama_media)

    resultados_electricos_gama_baja = seleccionar_mejor_vehiculo(data_car, 'Gama Baja', 'Electricity', monto_electricos_gama_baja)
    resultados_gasolina_gama_baja = seleccionar_mejor_vehiculo(data_car, 'Gama Baja', 'Regular', monto_gasolina_gama_baja)

    todos_los_resultados = pd.concat([
        resultados_electricos_gama_media,
        resultados_gasolina_gama_media,
        resultados_electricos_gama_baja,
        resultados_gasolina_gama_baja
    ])

    resultados_agrupados = todos_los_resultados.groupby(['Manufacturer', 'Model', 'fuelType', 'Price', 'Gama']).size().reset_index(name='Cantidad')

    orden_gamas = {'Gama Baja Electricidad': 1, 'Gama Baja Gasolina': 2, 'Gama Media Electricidad': 3, 'Gama Media Gasolina': 4}
    orden_combustible = {'Electricity': 1, 'Regular': 2}

    resultados_agrupados['Orden_Gama'] = resultados_agrupados['Gama'] + ' ' + resultados_agrupados['fuelType']
    resultados_agrupados['Orden_Gama'] = resultados_agrupados['Orden_Gama'].map(orden_gamas)
    resultados_agrupados['Orden_Combustible'] = resultados_agrupados['fuelType'].map(orden_combustible)

    resultados_agrupados = resultados_agrupados.sort_values(by=['Orden_Gama', 'Orden_Combustible', 'Manufacturer', 'Model'])
    resultados_agrupados = resultados_agrupados.drop(['Orden_Gama', 'Orden_Combustible'], axis=1)

    # Redondear los precios a dos decimales
    resultados_agrupados['Price'] = resultados_agrupados['Price'].round(2)

    
    # Devolver los resultados para verificar en main()
    return resultados_agrupados

# Aplicación Streamlit
def main():
    st.title("Selección de Vehículos")

    # Agregar widget para ingresar el monto de la inversión inicial
    inversion_inicial = st.number_input("Inversión Inicial", min_value=0, value=1000000)

    # Agregar widgets para ingresar otros parámetros
    porcentaje_electrico = st.slider("Porcentaje de Vehículos Eléctricos (%)", min_value=0, max_value=100, value=50)
    porcentaje_gama_media = st.slider("Porcentaje de Vehículos en Gama Media (%)", min_value=0, max_value=100, value=50)

    # Botón para ejecutar la selección
    if st.button("Seleccionar Vehículos"):
        # Capturar la salida de la función en una variable
        resultados = seleccionar_mejores_vehiculos(data_car, inversion_inicial, porcentaje_electrico, porcentaje_gama_media)

        # Verificar si la variable resultados es None antes de intentar acceder al atributo empty
        if resultados is not None:
            if not resultados.empty:
                # st.write("\nVehículos Sugeridos y Cantidad:\n")  # No es necesario imprimir aquí, ya se hizo en la función
                st.table(resultados[['Cantidad', 'Manufacturer', 'Model', 'fuelType', 'Price', 'Gama']])
            else:
                st.write("No se encontraron resultados para los criterios proporcionados.")
        else:
            st.write("Error al procesar los resultados. Por favor, verifica los parámetros proporcionados.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()


