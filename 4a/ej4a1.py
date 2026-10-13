"""
Enunciado:
En temas anteriores ya trabajamos con pandas y con el método `.plot()` de los
DataFrames para generar gráficos rápidos apoyándonos en matplotlib. Este
ejercicio es un recordatorio de esa técnica "local": no hay servidor, no hay
navegador ni backend web de por medio, simplemente generamos el gráfico en
nuestro propio proceso de Python y lo guardamos (o mostramos) directamente.

Tareas:
1. Construir un DataFrame de pandas con las ventas mensuales de varias
   tiendas.
2. Generar un gráfico de líneas con `DataFrame.plot()` comparando las ventas
   de cada tienda a lo largo del año.
3. Guardar el gráfico resultante como imagen PNG en disco, utilizando
   matplotlib como backend de renderizado.
4. Calcular el total de ventas por tienda a partir del propio DataFrame.

Este ejercicio NO levanta ningún servidor web: todo el renderizado ocurre
localmente en el proceso de Python, igual que vimos en temas anteriores.
"""

import os

import matplotlib
# Backend no interactivo: no necesitamos abrir una ventana para generar
# la imagen, simplemente queremos guardarla a disco.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "ventas_mensuales.png")


def crear_dataframe_ventas():
    """
    Crea y devuelve un DataFrame con las ventas mensuales (en unidades)
    de tres tiendas ficticias, indexado por mes.
    """
    # TODO: implementa esta función.
    pass


def generar_grafico_lineas(df_ventas, ruta_salida=OUTPUT_PATH):
    """
    Genera un gráfico de líneas comparando las ventas de cada tienda y lo
    guarda en disco como PNG usando el método `.plot()` de pandas.

    Devuelve el objeto Axes de matplotlib generado, para poder inspeccionarlo
    en los tests sin necesidad de abrir la imagen resultante.
    """
    # TODO: implementa esta función.
    pass


def calcular_totales_por_tienda(df_ventas):
    """
    Devuelve una Series de pandas con el total de unidades vendidas por
    tienda a lo largo del año.
    """
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    df_ventas = crear_dataframe_ventas()

    print("Ventas mensuales:")
    print(df_ventas)

    totales = calcular_totales_por_tienda(df_ventas)
    print("\nTotal de ventas por tienda:")
    print(totales)

    generar_grafico_lineas(df_ventas)
    print(f"\nGráfico guardado en: {OUTPUT_PATH}")
