"""
Enunciado:
Además de `plotly.express`, Plotly ofrece la API de más bajo nivel
`plotly.graph_objects`, que da control total sobre la figura. En este
ejercicio la usaremos para combinar varios gráficos relacionados en una
misma figura mediante subplots.

Tareas:
1. Construir un DataFrame de pandas con las ventas y el margen de beneficio
   mensuales de una tienda.
2. Crear una figura con dos subplots apilados verticalmente (compartiendo el
   eje X) usando `plotly.subplots.make_subplots`:
   - arriba: un gráfico de barras con las ventas mensuales.
   - abajo: un gráfico de líneas con el margen de beneficio (%).
3. Guardar el resultado como un fichero HTML interactivo.
"""

import os

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4c2_ventas_margen.html")


def crear_dataframe_tienda():
    """
    Crea un DataFrame de pandas con las ventas (en unidades) y el margen de
    beneficio (en %) mensuales de una tienda.
    """
    # TODO: implementa esta función.
    pass


def crear_figura_subplots(df_tienda):
    """
    Crea una figura de Plotly con dos subplots apilados (ventas arriba,
    margen de beneficio abajo), compartiendo el eje X.

    Devuelve el objeto `Figure` de Plotly.
    """
    # TODO: implementa esta función.
    pass


def guardar_grafico(fig, ruta_salida=OUTPUT_PATH):
    """Guarda la figura de Plotly recibida como un fichero HTML interactivo."""
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    df_tienda = crear_dataframe_tienda()
    fig = crear_figura_subplots(df_tienda)
    ruta = guardar_grafico(fig)
    print(f"Gráfico de Plotly guardado en: {ruta}")
