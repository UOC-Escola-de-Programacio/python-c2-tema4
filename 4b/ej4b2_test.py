"""
Tests para el ejercicio ej4b2.py (ColumnDataSource + HoverTool en Bokeh).
"""

import os

from bokeh.models import GlyphRenderer, HoverTool
from bokeh.plotting import figure

from ej4b2 import crear_dataframe_ventas, crear_figura_con_hover, guardar_figura


def test_crear_dataframe_ventas():
    df_ventas = crear_dataframe_ventas()

    assert "mes" in df_ventas.columns
    assert "Producto A" in df_ventas.columns
    assert "Producto B" in df_ventas.columns
    assert len(df_ventas) == 12


def test_crear_figura_con_hover():
    df_ventas = crear_dataframe_ventas()
    fig = crear_figura_con_hover(df_ventas)

    assert isinstance(fig, figure)

    # Debe haber una línea por cada producto
    renderers_linea = [r for r in fig.renderers
                        if isinstance(r, GlyphRenderer) and type(r.glyph).__name__ == "Line"]
    assert len(renderers_linea) == 2

    # Debe tener configurado un HoverTool con tooltips para ambos productos
    hover_tools = [h for h in fig.toolbar.tools if isinstance(h, HoverTool)]
    assert len(hover_tools) == 1

    campos_tooltip = [campo for _, campo in hover_tools[0].tooltips]
    assert "@mes" in campos_tooltip
    assert "@{Producto A}" in campos_tooltip
    assert "@{Producto B}" in campos_tooltip


def test_guardar_figura(tmp_path):
    df_ventas = crear_dataframe_ventas()
    fig = crear_figura_con_hover(df_ventas)
    ruta_salida = tmp_path / "test_ej4b2.html"

    guardar_figura(fig, ruta_salida=str(ruta_salida))

    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0
