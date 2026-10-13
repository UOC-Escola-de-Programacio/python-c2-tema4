"""
Tests para el ejercicio ej4b5/main.py (primera app con Bokeh server).
"""

from bokeh.layouts import Column
from bokeh.models import Button, ColumnDataSource
from bokeh.plotting import figure

from ej4b5.main import (
    anadir_punto_aleatorio,
    crear_boton,
    crear_figura_y_fuente,
    crear_layout,
)


def test_crear_figura_y_fuente():
    fig, fuente = crear_figura_y_fuente()

    assert isinstance(fig, figure)
    assert isinstance(fuente, ColumnDataSource)
    assert fuente.data["x"] == []
    assert fuente.data["y"] == []
    assert fuente.data["color"] == []


def test_anadir_punto_aleatorio():
    _, fuente = crear_figura_y_fuente()

    anadir_punto_aleatorio(fuente)

    assert len(fuente.data["x"]) == 1
    assert len(fuente.data["y"]) == 1
    assert len(fuente.data["color"]) == 1
    assert 0 <= fuente.data["x"][0] <= 100
    assert 0 <= fuente.data["y"][0] <= 100

    anadir_punto_aleatorio(fuente)

    assert len(fuente.data["x"]) == 2


def test_crear_boton():
    _, fuente = crear_figura_y_fuente()
    boton = crear_boton(fuente)

    assert isinstance(boton, Button)
    assert boton.label == "Añadir punto"

    # El botón debe tener un callback de Python registrado para el clic
    assert len(boton._event_callbacks.get("button_click", [])) == 1

    boton._event_callbacks["button_click"][0]()
    assert len(fuente.data["x"]) == 1


def test_crear_layout():
    layout, fuente = crear_layout()

    assert isinstance(layout, Column)
    assert isinstance(fuente, ColumnDataSource)

    botones = [hijo for hijo in layout.children if isinstance(hijo, Button)]
    figuras = [hijo for hijo in layout.children if isinstance(hijo, figure)]
    assert len(botones) == 1
    assert len(figuras) == 1
