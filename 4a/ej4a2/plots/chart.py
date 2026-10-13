"""
Lógica de generación del gráfico, totalmente independiente de Django: recibe
y devuelve datos (DataFrame, bytes PNG), sin saber nada de peticiones HTTP.
Esto permite reutilizarla y testearla sin necesidad de levantar el servidor.
"""

import io

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

TEMPERATURAS = {
    "Barcelona": [10, 11, 13, 15, 18, 22, 25, 25, 22, 18, 13, 11],
    "Madrid": [6, 8, 11, 14, 18, 23, 27, 26, 22, 16, 10, 7],
    "Bilbao": [9, 10, 12, 13, 16, 19, 21, 21, 19, 15, 12, 10],
}
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]


def construir_dataframe_temperaturas():
    """
    Construye (de forma "lenta", recalculando cada vez) un DataFrame de
    pandas con la temperatura media mensual de varias ciudades.
    """
    # TODO: implementa esta función.
    pass


def generar_png_temperaturas():
    """
    Genera el gráfico de temperaturas con pandas + matplotlib y devuelve los
    bytes de la imagen PNG resultante, listos para enviar en una respuesta
    HTTP de tipo `image/png`.
    """
    # TODO: implementa esta función.
    pass
