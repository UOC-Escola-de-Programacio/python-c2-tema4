"""
Tests para el ejercicio 4b6 (app de Bokeh server embebida en una vista de
Django mediante `bokeh.embed.server_document`).

Se testea tanto la lógica pura de la app de Bokeh (`bokeh_app.main`,
independiente de Django) como la vista de Django que la incrusta
(`dashboard.views`), usando el cliente de pruebas de Django.
"""

import os
import sys

import django
import numpy as np
import pytest
from bokeh.layouts import Column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure

# Este fichero de test vive en la raíz del apartado (`4b/`), al mismo nivel
# que el resto de ejercicios, en lugar de dentro de `ej4b6/`. Como el
# proyecto Django de `ej4b6` usa nombres de módulo "planos" (`config`,
# `dashboard`, `bokeh_app`), hay que añadir la carpeta del ejercicio al
# `sys.path` para que esos módulos se puedan importar igual que si se
# ejecutara `python manage.py` desde dentro de `ej4b6/`.
EJ4B6_DIR = os.path.join(os.path.dirname(__file__), "ej4b6")
if EJ4B6_DIR not in sys.path:
    sys.path.insert(0, EJ4B6_DIR)

from bokeh_app.main import (
    AMPLITUD_INICIAL,
    calcular_onda,
    crear_figura_y_fuente,
    crear_layout,
    crear_slider_con_callback,
)

# El registro de apps de Django solo se puede inicializar una vez por
# proceso. Si los tests se ejecutan junto con los de otro ejercicio Django
# del repositorio (por ejemplo `4a/ej4a2`), puede que `django.setup()` ya se
# haya llamado con otra configuración: en ese caso usamos `override_settings`
# para activar temporalmente la configuración de este ejercicio en lugar de
# volver a llamar a `django.setup()` (que sería un no-op).
from django.apps import apps as django_apps

if not django_apps.ready:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    django.setup()

from django.test import Client, override_settings

CONFIGURACION_EJ4B6 = override_settings(
    INSTALLED_APPS=["django.contrib.staticfiles", "dashboard"],
    ROOT_URLCONF="config.urls",
    BOKEH_SERVER_URL="http://localhost:5006/bokeh_app",
)


def test_calcular_onda_amplitud_por_defecto():
    x, y = calcular_onda()

    assert len(x) == len(y)
    assert np.isclose(np.max(y), AMPLITUD_INICIAL, atol=1e-2)
    assert np.isclose(np.min(y), -AMPLITUD_INICIAL, atol=1e-2)


def test_crear_figura_y_fuente():
    fig, fuente = crear_figura_y_fuente()

    assert isinstance(fig, figure)
    assert isinstance(fuente, ColumnDataSource)
    assert "x" in fuente.data
    assert "y" in fuente.data


def test_crear_slider_con_callback_actualiza_la_fuente():
    _, fuente = crear_figura_y_fuente()
    slider_amplitud = crear_slider_con_callback(fuente)

    assert isinstance(slider_amplitud, Slider)
    assert slider_amplitud.value == AMPLITUD_INICIAL

    # El slider debe tener un callback de Python registrado para "value"
    callbacks = slider_amplitud._callbacks.get("value", [])
    assert len(callbacks) == 1

    # Simular un cambio de valor del slider y comprobar que la fuente
    # se actualiza acorde a la nueva amplitud
    callbacks[0]("value", AMPLITUD_INICIAL, 2.5)
    assert np.isclose(np.max(fuente.data["y"]), 2.5, atol=1e-2)


def test_crear_layout():
    layout, fuente = crear_layout()

    assert isinstance(layout, Column)
    assert isinstance(fuente, ColumnDataSource)

    sliders = [hijo for hijo in layout.children if isinstance(hijo, Slider)]
    figuras = [hijo for hijo in layout.children if isinstance(hijo, figure)]
    assert len(sliders) == 1
    assert len(figuras) == 1


@pytest.fixture
def client():
    return Client()


@CONFIGURACION_EJ4B6
def test_vista_pagina_principal(client):
    from django.conf import settings

    respuesta = client.get("/")

    assert respuesta.status_code == 200
    # El script generado por `server_document` apunta a la URL configurada
    # del Bokeh server, aunque este no esté realmente en marcha durante el
    # test: solo se genera el HTML/JavaScript de conexión.
    assert settings.BOKEH_SERVER_URL.encode() in respuesta.content
    assert b"<script" in respuesta.content
    assert b"Bokeh server embebido en una vista de Django" in respuesta.content
