import matplotlib.pyplot as plt
import seaborn as sns
import math

def eda_inicial(df):
    """
    Realiza un Análisis Exploratorio de Datos (EDA) inicial en un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame que se analizará.

    Returns
    -------
    None

    Prints
    ------
    None
        Imprime información sobre el DataFrame, incluyendo nombre y tipo de columnas,
        número de filas y valores nulos.
    None
        Imprime el número de duplicados en el DataFrame.
    None
        Imprime estadísticas descriptivas de las columnas.
    """
    # Obtener información del DataFrame, incluyendo nombre y tipo de columnas,
    # número de filas y valores nulos.
    print(df.info(), "\n")

    # Obtener los duplicados considerando todas las columnas.
    print(f"El número de duplicados en el DataFrame es: {df.duplicated().sum()} \n")

    # Describir las columnas.
    print(df.describe(include="all"), "\n")


def get_outliers_df(df, exclude = [], size = (16,8), ylim= None):
    """
    Crea un boxplot para visualizar los valores atípicos en las columnas numéricas 
    de un DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        El DataFrame que se utilizará para crear el boxplot.
    exclude : list, optional
        Lista de columnas a excluir del boxplot. Por defecto, es una lista vacía.
    size : tuple, optional
        Tamaño de la figura. Por defecto, es (16, 8).
    ylim : tuple, optional
        Límites del eje y. Por defecto, se ajusta automáticamente.

    Returns
    -------
    None

    Prints
    ------
    None
        Muestra un boxplot de todas las columnas numéricas del DataFrame excluyendo las especificadas en "exclude".
    """
    # Configurar el tamaño de la figura.
    plt.figure(figsize=size)

    # Crear el boxplot con todas las columnas numéricas no incluidas en "exclude".
    sns.boxplot(data=df.drop(exclude, axis=1))

    # Personalizar el título y las etiquetas de los ejes.
    plt.title("Boxplot de las Columnas Numéricas")
    plt.xlabel("Columnas")
    plt.ylabel("Valores")

    # Ajustar las etiquetas del eje x para mejorar la legibilidad.
    plt.xticks(rotation=45, ha="right")

    # Ajustar los límites del eje y.
    plt.ylim(ylim)

    # Mostrar el gráfico.
    plt.show()

    