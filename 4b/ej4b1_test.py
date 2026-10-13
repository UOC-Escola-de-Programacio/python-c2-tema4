"""
Tests para el ejercicio ej4b1.py (primera figura con Bokeh).
"""

import os

from bokeh.models import GlyphRenderer
from bokeh.plotting import figure

from ej4b1 import MESES, TEMPERATURAS, crear_figura_temperaturas, guardar_figura


def test_crear_figura_temperaturas():
    fig = crear_figura_temperaturas()

    assert isinstance(fig, figure)
    assert fig.title.text == "Temperatura media mensual (Madrid)"
    assert fig.xaxis[0].axis_label == "Mes"
    assert fig.yaxis[0].axis_label == "Temperatura (ºC)"

    # Debe haber al menos un renderer de tipo línea y uno de dispersión
    tipos_glyph = [type(r.glyph).__name__ for r in fig.renderers
                   if isinstance(r, GlyphRenderer)]
    assert "Line" in tipos_glyph
    assert any(tipo in tipos_glyph for tipo in ("Scatter", "Circle"))


def test_guardar_figura(tmp_path):
    fig = crear_figura_temperaturas()
    ruta_salida = tmp_path / "test_ej4b1.html"

    ruta_devuelta = guardar_figura(fig, ruta_salida=str(ruta_salida))

    assert ruta_devuelta == str(ruta_salida)
    assert os.path.exists(ruta_salida)

    contenido = ruta_salida.read_text(encoding="utf-8")
    assert "<html" in contenido.lower()
    # Los datos de temperatura deben estar embebidos en el HTML/JS generado
    assert str(TEMPERATURAS[0]) in contenido
