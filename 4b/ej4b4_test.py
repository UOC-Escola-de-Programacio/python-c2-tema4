"""
Tests para el ejercicio ej4b4.py (widgets + CustomJS en Bokeh).
"""

import os

import numpy as np
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure

from ej4b4 import (
    AMPLITUD_INICIAL,
    calcular_onda,
    crear_figura_interactiva,
    guardar_layout_interactivo,
)


def test_calcular_onda_amplitud_por_defecto():
    x, y = calcular_onda()

    assert len(x) == len(y)
    assert np.isclose(np.max(y), AMPLITUD_INICIAL, atol=1e-2)
    assert np.isclose(np.min(y), -AMPLITUD_INICIAL, atol=1e-2)


def test_calcular_onda_con_amplitud_personalizada():
    x, y = calcular_onda(amplitud=2.5, num_puntos=50)

    assert len(x) == 50
    assert np.isclose(np.max(y), 2.5, atol=1e-2)


def test_crear_figura_interactiva():
    fig, fuente, slider_amplitud = crear_figura_interactiva()

    assert isinstance(fig, figure)
    assert isinstance(fuente, ColumnDataSource)
    assert isinstance(slider_amplitud, Slider)

    assert slider_amplitud.value == AMPLITUD_INICIAL
    assert "x" in fuente.data
    assert "y" in fuente.data

    # El slider debe tener un callback de JS registrado para el evento "value"
    callbacks_value = slider_amplitud.js_property_callbacks.get("change:value", [])
    assert len(callbacks_value) == 1
    assert isinstance(callbacks_value[0], CustomJS)


def test_guardar_layout_interactivo(tmp_path):
    fig, fuente, slider_amplitud = crear_figura_interactiva()
    ruta_salida = tmp_path / "test_ej4b4.html"

    guardar_layout_interactivo(fig, slider_amplitud, ruta_salida=str(ruta_salida))

    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0
