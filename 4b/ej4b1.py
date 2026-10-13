"""
Enunciado:
Bokeh es una biblioteca de visualización interactiva pensada para navegadores
web modernos. A diferencia de matplotlib, Bokeh genera una página HTML (con
JavaScript) que permite hacer zoom, desplazarse o guardar la imagen sin
necesidad de volver a ejecutar Python.

En este primer ejercicio aprenderás lo más básico: crear una figura, añadir
una "glyph" (línea) y guardar el resultado como fichero HTML.

Tareas:
1. Crear una figura de Bokeh con título y etiquetas de los ejes.
2. Añadir una línea (glyph `line`) con los datos de temperatura.
3. Guardar la figura en un fichero HTML con `output_file` + `save`.
"""

import os

from bokeh.plotting import figure, output_file, save

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
TEMPERATURAS = [6, 8, 11, 14, 18, 23, 27, 26, 22, 16, 10, 7]

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4b1_temperaturas.html")


def crear_figura_temperaturas():
    """
    Crea y devuelve una figura de Bokeh con una línea que representa la
    temperatura media mensual.
    """
    # TODO: implementa esta función.
    pass


def guardar_figura(fig, ruta_salida=OUTPUT_PATH):
    """
    Guarda la figura de Bokeh recibida como un fichero HTML autocontenido.
    """
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    fig = crear_figura_temperaturas()
    ruta = guardar_figura(fig)
    print(f"Gráfico de Bokeh guardado en: {ruta}")
