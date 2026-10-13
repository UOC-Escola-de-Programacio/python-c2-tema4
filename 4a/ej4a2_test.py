"""
Tests para el ejercicio 4a2 (app Django que sirve un gráfico de pandas).

Se testea tanto la lógica pura de generación del gráfico (`plots.chart`,
independiente de Django) como las vistas HTTP, usando el cliente de pruebas
de Django.
"""

import os
import sys

import django
import pandas as pd
import pytest

# Este fichero de test vive en la raíz del apartado (`4a/`), al mismo nivel
# que el resto de ejercicios, en lugar de dentro de `ej4a2/`. Como el
# proyecto Django de `ej4a2` usa nombres de módulo "planos" (`mysite`,
# `plots`), hay que añadir la carpeta del ejercicio al `sys.path` para que
# esos módulos se puedan importar igual que si se ejecutara
# `python manage.py` desde dentro de `ej4a2/`.
EJ4A2_DIR = os.path.join(os.path.dirname(__file__), "ej4a2")
if EJ4A2_DIR not in sys.path:
    sys.path.insert(0, EJ4A2_DIR)

# El registro de apps de Django solo se puede inicializar una vez por
# proceso. Si los tests se ejecutan junto con los de otro ejercicio Django
# del repositorio (por ejemplo `4b/ej4b6`), puede que `django.setup()` ya se
# haya llamado con otra configuración: en ese caso usamos `override_settings`
# para activar temporalmente la configuración de este ejercicio en lugar de
# volver a llamar a `django.setup()` (que sería un no-op).
from django.apps import apps as django_apps

if not django_apps.ready:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()

from django.test import Client, override_settings

from plots.chart import construir_dataframe_temperaturas, generar_png_temperaturas

CONFIGURACION_EJ4A2 = override_settings(
    INSTALLED_APPS=["django.contrib.staticfiles", "plots"],
    ROOT_URLCONF="mysite.urls",
)


def test_construir_dataframe_temperaturas():
    df_temperaturas = construir_dataframe_temperaturas()

    assert isinstance(df_temperaturas, pd.DataFrame)
    assert "Barcelona" in df_temperaturas.columns
    assert "Madrid" in df_temperaturas.columns
    assert len(df_temperaturas) == 12


def test_generar_png_temperaturas():
    contenido_png = generar_png_temperaturas()

    assert isinstance(contenido_png, bytes)
    # Cabecera estándar de los ficheros PNG
    assert contenido_png.startswith(b"\x89PNG\r\n\x1a\n")


@pytest.fixture
def client():
    return Client()


@CONFIGURACION_EJ4A2
def test_vista_grafico_png(client):
    respuesta = client.get("/grafico.png")

    assert respuesta.status_code == 200
    assert respuesta["Content-Type"] == "image/png"
    assert respuesta.content.startswith(b"\x89PNG\r\n\x1a\n")


@CONFIGURACION_EJ4A2
def test_vista_pagina_principal(client):
    respuesta = client.get("/")

    assert respuesta.status_code == 200
    assert b"grafico.png" in respuesta.content
    assert b"Temperatura media mensual" in respuesta.content
