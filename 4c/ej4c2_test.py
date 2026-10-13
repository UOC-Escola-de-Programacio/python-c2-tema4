"""
Tests para el ejercicio ej4c2.py (Plotly graph_objects + subplots).
"""

import os

import pandas as pd
import plotly.graph_objects as go

from ej4c2 import crear_dataframe_tienda, crear_figura_subplots, guardar_grafico


def test_crear_dataframe_tienda():
    df_tienda = crear_dataframe_tienda()

    assert isinstance(df_tienda, pd.DataFrame)
    assert {"mes", "ventas", "margen_pct"}.issubset(df_tienda.columns)
    assert len(df_tienda) == 12


def test_crear_figura_subplots():
    df_tienda = crear_dataframe_tienda()
    fig = crear_figura_subplots(df_tienda)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) == 2

    tipos_trazas = {trace.type for trace in fig.data}
    assert tipos_trazas == {"bar", "scatter"}

    # Cada traza debe estar asignada a un subplot distinto (xaxis/xaxis2)
    ejes_x = {trace.xaxis for trace in fig.data}
    assert len(ejes_x) == 2


def test_guardar_grafico(tmp_path):
    df_tienda = crear_dataframe_tienda()
    fig = crear_figura_subplots(df_tienda)
    ruta_salida = tmp_path / "test_ej4c2.html"

    guardar_grafico(fig, ruta_salida=str(ruta_salida))

    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0
