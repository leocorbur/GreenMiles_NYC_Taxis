# Importar librerias estándar
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


# Cargar el df
data_car = pd.read_excel("data_car_completa.xlsx")

# Cambiar el nombre de la columna
data_car.rename(columns={'fuelType': 'Tipo de Combustible'}, inplace=True)
data_car.rename(columns={'Manufacturer': 'Fabricante'}, inplace=True)
data_car.rename(columns={'Model': 'Modelo'}, inplace=True)
data_car.rename(columns={'Price': 'Precio'}, inplace=True)

# Cambiar los valores en la columna 'Tipo de Combustible'
data_car['Tipo de Combustible'] = data_car['Tipo de Combustible'].replace({'Electricity': 'Electricos', 'Regular': 'Gasolina'})

# Establecer formato decimal
pd.set_option('display.float_format', '{:.2f}'.format)

# Calcula los percentiles para determinar los límites
percentiles = data_car['Precio'].quantile([0, 0.33, 0.66, 1])

# Asigna etiquetas a las categorías según los percentiles y crea la nueva columna 'Gama'
data_car['Gama'] = pd.cut(data_car['Precio'], bins=percentiles, labels=['Gama Baja', 'Gama Media', 'Gama Alta'], include_lowest=True)

# Seleccionar el mejor vehículo eléctrico para una categoría y tipo de combustible específicos
def seleccionar_mejor_vehiculo(data_car, gama, tipo_combustible, inversion_a_gastar):
    vehiculos_filtrados = data_car[(data_car['Gama'] == gama) & (data_car['Tipo de Combustible'] == tipo_combustible)]
    if vehiculos_filtrados.empty:
        print(f"No se encontraron vehículos que cumplan con los criterios para Gama {gama}.")
        return pd.DataFrame()

    vehiculos_filtrados = vehiculos_filtrados.sort_values(by='Precio')
    vehiculos_filtrados = vehiculos_filtrados.sort_values(by=['co2', 'range'], ascending=[True, False])
    mejor_vehiculo = vehiculos_filtrados.iloc[0].copy()

    cantidad_vehiculos = int(inversion_a_gastar / mejor_vehiculo['Precio'])
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

    resultados_electricos_gama_media = seleccionar_mejor_vehiculo(data_car, 'Gama Media', 'Electricos', monto_electricos_gama_media)
    resultados_gasolina_gama_media = seleccionar_mejor_vehiculo(data_car, 'Gama Media', 'Gasolina', monto_gasolina_gama_media)

    resultados_electricos_gama_baja = seleccionar_mejor_vehiculo(data_car, 'Gama Baja', 'Electricos', monto_electricos_gama_baja)
    resultados_gasolina_gama_baja = seleccionar_mejor_vehiculo(data_car, 'Gama Baja', 'Gasolina', monto_gasolina_gama_baja)

    todos_los_resultados = pd.concat([
        resultados_electricos_gama_media,
        resultados_gasolina_gama_media,
        resultados_electricos_gama_baja,
        resultados_gasolina_gama_baja
    ])

    resultados_agrupados = todos_los_resultados.groupby(['Fabricante', 'Modelo', 'Tipo de Combustible', 'Precio', 'Gama']).size().reset_index(name='Cantidad')

    orden_gamas = {'Gama Baja Electricidad': 1, 'Gama Baja Gasolina': 2, 'Gama Media Electricidad': 3, 'Gama Media Gasolina': 4}
    orden_combustible = {'Electricos': 1, 'Gasolina': 2}

    resultados_agrupados['Orden_Gama'] = resultados_agrupados['Gama'] + ' ' + resultados_agrupados['Tipo de Combustible']
    resultados_agrupados['Orden_Gama'] = resultados_agrupados['Orden_Gama'].map(orden_gamas)
    resultados_agrupados['Orden_Combustible'] = resultados_agrupados['Tipo de Combustible'].map(orden_combustible)

    resultados_agrupados = resultados_agrupados.sort_values(by=['Orden_Gama', 'Orden_Combustible', 'Fabricante', 'Modelo'])
    resultados_agrupados = resultados_agrupados.drop(['Orden_Gama', 'Orden_Combustible'], axis=1)

    # Redondear los precios a dos decimales
    resultados_agrupados['Precio'] = resultados_agrupados['Precio'].round(2)

    
    # Devolver los resultados para verificar en main()
    return resultados_agrupados

def main():
    st.title("Selección de Vehículos")

    # Agregar widget para ingresar el monto de la inversión inicial
    inversion_inicial = st.number_input("Inversión Inicial", min_value=0, value=1000000)

    # Agregar widgets para ingresar otros parámetros
    porcentaje_electrico = st.slider("Porcentaje de la Inversión en Vehículos Eléctricos (%)", min_value=0, max_value=100, value=50)
    porcentaje_gama_media = st.slider("Porcentaje de Vehículos de Gama Media (%)", min_value=0, max_value=100, value=50)

    # Botón para ejecutar la selección
    if st.button("Seleccionar Vehículos"):
        # Capturar la salida de la función en una variable
        resultados = seleccionar_mejores_vehiculos(data_car, inversion_inicial, porcentaje_electrico, porcentaje_gama_media)

        # Verificar si la variable resultados es None antes de intentar acceder al atributo empty
        if resultados is not None:
            if not resultados.empty:
                st.dataframe(resultados[['Cantidad', 'Fabricante', 'Modelo', 'Tipo de Combustible', 'Precio', 'Gama']])


                
                # Importar la paleta viridis desde Seaborn
                # Obtener la paleta viridis
                viridis_palette = sns.color_palette("viridis", n_colors=2)
                
                # Crear gráfico de barras con la paleta viridis
                plt.figure(figsize=(10, 6))
                sns.barplot(x='Gama', y='Cantidad', hue='Tipo de Combustible', data=resultados, palette=viridis_palette)
                plt.title("Distribución de la Flota")
                plt.xlabel("Gama")
                plt.ylabel("Cantidad de Vehículos")
                st.pyplot(plt)
            else:
                st.write("No se encontraron resultados para los criterios proporcionados.")
        else:
            st.write("Error al procesar los resultados. Por favor, verifica los parámetros proporcionados.")


# Función para el gráfico
def plot_chart(resultados):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Usar Seaborn para un gráfico más agradable
    sns.barplot(x='Gama', y='Cantidad', data=resultados, ax=ax)
    
    # Configuraciones adicionales del gráfico
    ax.set_xlabel('Gama')
    ax.set_ylabel('Cantidad de Vehículos')
    ax.set_title('Distribución de la Flota por Gama')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

# Ejecutar la aplicación
if __name__ == "__main__":
    main()


