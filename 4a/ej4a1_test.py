"""
Tests para el ejercicio ej4a1.py (visualización local con pandas + matplotlib).
"""

import os

import pandas as pd
import pytest

from ej4a1 import (
    MESES,
    crear_dataframe_ventas,
    generar_grafico_lineas,
    calcular_totales_por_tienda,
)


def test_crear_dataframe_ventas():
    df_ventas = crear_dataframe_ventas()

    assert isinstance(df_ventas, pd.DataFrame)
    assert list(df_ventas.index) == MESES
    assert "Tienda Centro" in df_ventas.columns
    assert "Tienda Norte" in df_ventas.columns
    assert "Tienda Sur" in df_ventas.columns
    assert len(df_ventas) == 12


def test_calcular_totales_por_tienda():
    df_ventas = crear_dataframe_ventas()
    totales = calcular_totales_por_tienda(df_ventas)

    assert isinstance(totales, pd.Series)
    assert totales["Tienda Centro"] == df_ventas["Tienda Centro"].sum()
    assert totales["Tienda Norte"] == df_ventas["Tienda Norte"].sum()
    assert totales["Tienda Sur"] == df_ventas["Tienda Sur"].sum()
    # La tienda Centro, con los valores más altos, debe ser la de mayor total
    assert totales.idxmax() == "Tienda Centro"


def test_generar_grafico_lineas(tmp_path):
    df_ventas = crear_dataframe_ventas()
    ruta_salida = tmp_path / "grafico_test.png"

    ejes = generar_grafico_lineas(df_ventas, ruta_salida=str(ruta_salida))

    # El fichero se debe haber generado en disco
    assert os.path.exists(ruta_salida)
    assert os.path.getsize(ruta_salida) > 0

    # El gráfico debe tener una línea por cada tienda
    assert len(ejes.get_lines()) == len(df_ventas.columns)
    assert ejes.get_title() == "Ventas mensuales por tienda"
