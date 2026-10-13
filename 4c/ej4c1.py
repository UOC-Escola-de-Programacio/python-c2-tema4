"""
Enunciado:
Plotly Express es la interfaz de alto nivel de Plotly: con muy poco código
permite construir gráficos interactivos (zoom, tooltips, exportación a PNG
desde el propio navegador) a partir de un DataFrame de pandas.

Tareas:
1. Construir un DataFrame de pandas con la esperanza de vida y el PIB per
   cápita de varios países.
2. Crear un gráfico de dispersión (`scatter`) con `plotly.express` donde el
   tamaño de cada punto represente la población y el color el continente.
3. Guardar el gráfico como un fichero HTML interactivo.
"""

import os

import pandas as pd
import plotly.express as px

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4c1_esperanza_vida.html")


def crear_dataframe_paises():
    """
    Crea un DataFrame de pandas con datos (ficticios, simplificados) de
    esperanza de vida, PIB per cápita y población de varios países.
    """
    # TODO: implementa esta función.
    pass


def crear_grafico_dispersion(df_paises):
    """
    Crea un gráfico de dispersión interactivo con plotly.express donde:
    - el eje X es el PIB per cápita
    - el eje Y es la esperanza de vida
    - el tamaño del punto representa la población
    - el color representa el continente

    Devuelve el objeto `Figure` de Plotly.
    """
    # TODO: implementa esta función.
    pass


def guardar_grafico(fig, ruta_salida=OUTPUT_PATH):
    """Guarda la figura de Plotly recibida como un fichero HTML interactivo."""
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    df_paises = crear_dataframe_paises()
    fig = crear_grafico_dispersion(df_paises)
    ruta = guardar_grafico(fig)
    print(f"Gráfico de Plotly guardado en: {ruta}")
