"""
Tests para el ejercicio ej4b3.py (layouts/gridplot en Bokeh).
"""

import os

from bokeh.models.plots import GridPlot
from bokeh.plotting import figure

from ej4b3 import (
    crear_figura_evolucion,
    crear_figura_barras,
    crear_layout,
    guardar_layout,
)


def test_crear_figura_evolucion():
    fig = crear_figura_evolucion()
    assert isinstance(fig, figure)
    assert fig.title.text == "Evolución mensual de ventas"


def test_crear_figura_barras():
    fig = crear_figura_barras()
    assert isinstance(fig, figure)
    assert fig.title.text == "Total de ventas por producto"

    tipos_glyph = [type(r.glyph).__name__ for r in fig.renderers]
    assert "VBar" in tipos_glyph


def test_crear_layout():
    layout = crear_layout()

    assert isinstance(layout, GridPlot)
    figuras_en_layout = [elemento[0] for elemento in layout.children]
    assert len(figuras_en_layout) == 2
    assert all(isinstance(f, figure) for f in figuras_en_layout)


def test_guardar_layout(tmp_path):
    layout = crear_layout()
    ruta_salida = tmp_path / "test_ej4b3.html"

    guardar_layout(layout, ruta_salida=str(ruta_salida))

    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0
