"""
App de Bokeh server que se ejecuta de forma independiente (con
`bokeh serve`) y que, en el ejercicio `ej4b6`, se incrusta en una página de
Django mediante `bokeh.embed.server_document` (ver `dashboard/views.py`).

Es muy similar a `ej4b4` (onda senoidal con `Slider` de amplitud), pero el
callback que recalcula la onda se ejecuta en **Python, en el servidor**
(`on_change`), en lugar de en JavaScript (`CustomJS`) dentro del navegador.
"""

import numpy as np
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import curdoc, figure

AMPLITUD_INICIAL = 1.0
NUM_PUNTOS = 200


def calcular_onda(amplitud=AMPLITUD_INICIAL, num_puntos=NUM_PUNTOS):
    """
    Calcula los puntos `x`/`y` de una onda senoidal con la amplitud dada.
    Devuelve dos arrays de numpy (x, y).
    """
    # TODO: implementa esta función.
    pass


def crear_figura_y_fuente():
    """
    Crea la figura y el `ColumnDataSource` con los datos iniciales de la
    onda. Devuelve una tupla (figura, fuente).
    """
    # TODO: implementa esta función.
    pass


def crear_slider_con_callback(fuente):
    """
    Crea el `Slider` de amplitud y le asocia un callback de Python
    (`on_change`) que recalcula la onda y actualiza el `ColumnDataSource`
    cada vez que cambia el valor del slider.
    """
    # TODO: implementa esta función.
    pass


def crear_layout():
    """
    Construye la figura, la fuente y el slider (con su callback), y
    devuelve el layout completo junto con la fuente, para facilitar las
    pruebas.
    """
    # TODO: implementa esta función.
    pass


# `bokeh serve` ejecuta este módulo una vez por cada sesión de navegador,
# construyendo el layout y añadiéndolo al documento del servidor. Al
# importar el módulo desde los tests, estas líneas también se ejecutan, pero
# no tienen efectos secundarios si no hay un servidor de Bokeh en ejecución.
#
# Mientras `crear_layout` no esté implementada, `_resultado` será `None` y
# el módulo se podrá seguir importando sin errores (por ejemplo, desde los
# tests de las funciones anteriores).
_resultado = crear_layout()
if _resultado is not None:
    layout, fuente = _resultado
    curdoc().add_root(layout)
    curdoc().title = "Ejercicio 4b6"
