"""
Tests para el ejercicio ej4c3/app.py (primera app con Dash).
"""

from dash import dcc, html

from ej4c3.app import crear_dataframe_visitas, crear_figura_visitas, crear_layout, app


def test_crear_dataframe_visitas():
    df_visitas = crear_dataframe_visitas()

    assert "dia" in df_visitas.columns
    assert "visitas" in df_visitas.columns
    assert len(df_visitas) == 7


def test_crear_figura_visitas():
    df_visitas = crear_dataframe_visitas()
    fig = crear_figura_visitas(df_visitas)

    assert len(fig.data) == 1
    assert fig.data[0].type == "bar"
    assert fig.layout.title.text == "Visitas diarias a la web"


def test_crear_layout():
    layout = crear_layout()

    assert isinstance(layout, html.Div)

    titulos = [hijo for hijo in layout.children if isinstance(hijo, html.H1)]
    assert len(titulos) == 1
    assert "Dash" in titulos[0].children

    graficos = [hijo for hijo in layout.children if isinstance(hijo, dcc.Graph)]
    assert len(graficos) == 1
    assert graficos[0].id == "grafico-visitas"


def test_app_registrada():
    # La instancia global `app` debe tener el layout ya asignado
    assert app.layout is not None
