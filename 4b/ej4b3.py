"""
Enunciado:
Cuando queremos mostrar varios gráficos relacionados a la vez, Bokeh ofrece
utilidades de "layout" para organizarlos en filas, columnas o rejillas (como
se podría hacer con `subplots` en matplotlib, pero manteniendo cada gráfico
interactivo de forma independiente).

Tareas:
1. Crear una figura con la evolución de las ventas (línea).
2. Crear una figura con un diagrama de barras del total de ventas por
   producto.
3. Combinar ambas figuras en una rejilla (`gridplot`) de una sola fila.
4. Guardar el resultado como fichero HTML.
"""

import os

from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, save

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
VENTAS = [50, 55, 60, 65, 70, 90, 100, 95, 80, 75, 60, 120]

PRODUCTOS = ["Producto A", "Producto B", "Producto C"]
TOTAL_VENTAS = [705, 467, 318]

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4b3_layout.html")


def crear_figura_evolucion():
    """Crea una figura de línea con la evolución mensual de ventas."""
    # TODO: implementa esta función.
    pass


def crear_figura_barras():
    """Crea una figura de barras con el total de ventas por producto."""
    # TODO: implementa esta función.
    pass


def crear_layout():
    """
    Combina las dos figuras anteriores en una rejilla (gridplot) de una
    única fila y las devuelve junto con el layout resultante.
    """
    # TODO: implementa esta función.
    pass


def guardar_layout(layout, ruta_salida=OUTPUT_PATH):
    """Guarda el layout de Bokeh recibido como un fichero HTML."""
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    layout = crear_layout()
    ruta = guardar_layout(layout)
    print(f"Layout de Bokeh guardado en: {ruta}")
