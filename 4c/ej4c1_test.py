"""
Tests para el ejercicio ej4c1.py (Plotly Express: scatter desde pandas).
"""

import os

import pandas as pd
import plotly.graph_objects as go

from ej4c1 import crear_dataframe_paises, crear_grafico_dispersion, guardar_grafico


def test_crear_dataframe_paises():
    df_paises = crear_dataframe_paises()

    assert isinstance(df_paises, pd.DataFrame)
    columnas_esperadas = {"pais", "continente", "esperanza_vida",
                           "pib_per_capita", "poblacion_millones"}
    assert columnas_esperadas.issubset(df_paises.columns)
    assert len(df_paises) == 8


def test_crear_grafico_dispersion():
    df_paises = crear_dataframe_paises()
    fig = crear_grafico_dispersion(df_paises)

    assert isinstance(fig, go.Figure)
    assert len(fig.data) > 0
    # Un trazado por continente (hay 4 continentes distintos en los datos)
    assert len(fig.data) == df_paises["continente"].nunique()
    assert fig.layout.title.text == "Esperanza de vida vs. PIB per cápita"


def test_guardar_grafico(tmp_path):
    df_paises = crear_dataframe_paises()
    fig = crear_grafico_dispersion(df_paises)
    ruta_salida = tmp_path / "test_ej4c1.html"

    guardar_grafico(fig, ruta_salida=str(ruta_salida))

    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0
