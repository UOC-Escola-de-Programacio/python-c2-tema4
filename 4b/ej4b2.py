"""
Enunciado:
Una de las grandes ventajas de Bokeh frente a matplotlib es la posibilidad de
añadir interactividad directamente en el navegador sin escribir JavaScript.
En este ejercicio aprenderás a usar `ColumnDataSource` y la herramienta
`HoverTool`, que muestra información adicional al pasar el ratón por encima
de los puntos.

Tareas:
1. Construir un `ColumnDataSource` a partir de un DataFrame de pandas con las
   ventas mensuales de dos productos.
2. Dibujar dos líneas (una por producto) a partir del mismo
   `ColumnDataSource`.
3. Añadir un `HoverTool` que muestre el mes, el producto y el valor de ventas
   al pasar el ratón por encima de cada punto.
4. Guardar el resultado como fichero HTML.
"""

import os

import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Category10
from bokeh.plotting import figure, output_file, save

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4b2_ventas_productos.html")


def crear_dataframe_ventas():
    """
    Crea un DataFrame de pandas con las ventas mensuales de dos productos.
    """
    # TODO: implementa esta función.
    pass


def crear_figura_con_hover(df_ventas):
    """
    Crea una figura de Bokeh con una línea por producto y un HoverTool que
    muestra el mes, el producto y el valor de ventas correspondiente.

    Devuelve la figura de Bokeh.
    """
    # TODO: implementa esta función.
    pass


def guardar_figura(fig, ruta_salida=OUTPUT_PATH):
    """Guarda la figura de Bokeh recibida como un fichero HTML."""
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    df_ventas = crear_dataframe_ventas()
    fig = crear_figura_con_hover(df_ventas)
    ruta = guardar_figura(fig)
    print(f"Gráfico de Bokeh guardado en: {ruta}")
