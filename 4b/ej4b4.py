"""
Enunciado:
Bokeh permite añadir widgets (controles como sliders, selects o botones) que
pueden modificar un gráfico directamente en el navegador mediante callbacks
de JavaScript (`CustomJS`), sin necesidad de un servidor Python en ejecución.

En este ejercicio crearás un `Slider` que controla la amplitud de una onda
senoidal dibujada en una figura de Bokeh.

Tareas:
1. Calcular los datos iniciales de la onda con pandas/numpy y guardarlos en
   un `ColumnDataSource`.
2. Crear un `Slider` para la amplitud de la onda.
3. Escribir un callback `CustomJS` que, al mover el slider, recalcule los
   valores `y` de la onda y actualice el `ColumnDataSource`.
4. Combinar la figura y el slider en una columna (`column`) y guardarlos
   como fichero HTML.
"""

import os

import numpy as np
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, output_file, save

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ej4b4_slider.html")

AMPLITUD_INICIAL = 1.0
NUM_PUNTOS = 200


def calcular_onda(amplitud=AMPLITUD_INICIAL, num_puntos=NUM_PUNTOS):
    """
    Calcula los puntos `x`/`y` de una onda senoidal con la amplitud dada.
    Devuelve dos arrays de numpy (x, y).
    """
    # TODO: implementa esta función.
    pass


def crear_figura_interactiva():
    """
    Crea la figura, el `ColumnDataSource` con los datos iniciales de la onda
    y el `Slider` de amplitud, enlazados mediante un callback `CustomJS`.

    Devuelve una tupla (figura, fuente, slider).
    """
    # TODO: implementa esta función.
    pass


def guardar_layout_interactivo(fig, slider_amplitud, ruta_salida=OUTPUT_PATH):
    """Combina la figura y el slider en una columna y guarda el HTML resultante."""
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    fig, fuente, slider_amplitud = crear_figura_interactiva()
    ruta = guardar_layout_interactivo(fig, slider_amplitud)
    print(f"Gráfico interactivo de Bokeh guardado en: {ruta}")
