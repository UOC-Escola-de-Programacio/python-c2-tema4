"""
Tests para el ejercicio ej4c4/app.py (Dash con callbacks).
"""

from dash import dcc, html

from ej4c4.app import (
    CIUDADES,
    MESES,
    crear_dataframe_temperaturas,
    filtrar_por_ciudad,
    crear_figura_ciudad,
    crear_layout,
    actualizar_grafico,
    app,
)


def test_crear_dataframe_temperaturas():
    df_temperaturas = crear_dataframe_temperaturas()

    assert {"ciudad", "mes", "temperatura"}.issubset(df_temperaturas.columns)
    # Una fila por cada combinación ciudad/mes
    assert len(df_temperaturas) == len(CIUDADES) * len(MESES)


def test_filtrar_por_ciudad():
    df_temperaturas = crear_dataframe_temperaturas()
    df_madrid = filtrar_por_ciudad(df_temperaturas, "Madrid")

    assert len(df_madrid) == len(MESES)
    assert set(df_madrid["ciudad"]) == {"Madrid"}
    assert list(df_madrid["mes"]) == MESES


def test_crear_figura_ciudad():
    df_temperaturas = crear_dataframe_temperaturas()
    fig = crear_figura_ciudad(df_temperaturas, "Bilbao")

    assert len(fig.data) == 1
    assert "Bilbao" in fig.layout.title.text


def test_crear_layout():
    layout = crear_layout()

    assert isinstance(layout, html.Div)

    dropdowns = [hijo for hijo in layout.children if isinstance(hijo, dcc.Dropdown)]
    assert len(dropdowns) == 1
    assert dropdowns[0].id == "selector-ciudad"
    assert {opcion["value"] for opcion in dropdowns[0].options} == set(CIUDADES)

    graficos = [hijo for hijo in layout.children if isinstance(hijo, dcc.Graph)]
    assert len(graficos) == 1
    assert graficos[0].id == "grafico-temperatura"


def test_actualizar_grafico_callback():
    # El callback debe poder invocarse directamente como una función normal,
    # devolviendo una figura filtrada para la ciudad indicada.
    fig = actualizar_grafico("Madrid")

    assert len(fig.data) == 1
    assert "Madrid" in fig.layout.title.text
    assert list(fig.data[0].y) == [6, 8, 11, 14, 18, 23, 27, 26, 22, 16, 10, 7]


def test_app_registrada():
    assert app.layout is not None
