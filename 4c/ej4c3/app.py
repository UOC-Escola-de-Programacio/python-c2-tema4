"""
Enunciado:
Dash es un framework (basado en Flask, Plotly.js y React) para construir
aplicaciones web analíticas completas usando solo Python. En este primer
ejercicio construirás una app Dash básica: un layout con un título, un
párrafo descriptivo y un gráfico de Plotly generado a partir de un
DataFrame de pandas.

Tareas:
1. Construir un DataFrame de pandas con las visitas diarias a una web
   durante una semana.
2. Crear la figura de Plotly Express a partir de ese DataFrame.
3. Definir el layout de la app Dash (`app.layout`) con un título, un texto y
   el gráfico (`dcc.Graph`).
4. Ejecutar la app con `app.run()` para comprobar el resultado en el
   navegador.

Para arrancar la app:

    python app.py

Y visitar http://127.0.0.1:8050/ en el navegador.
"""

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def crear_dataframe_visitas():
    """
    Crea un DataFrame de pandas con el número de visitas diarias a una web
    ficticia durante una semana.
    """
    # TODO: implementa esta función.
    pass


def crear_figura_visitas(df_visitas):
    """
    Crea un gráfico de barras de Plotly Express con las visitas diarias.
    """
    # TODO: implementa esta función.
    pass


def crear_layout():
    """
    Construye y devuelve el layout de la app Dash: un título, un texto
    descriptivo y el gráfico de visitas diarias.
    """
    # TODO: implementa esta función.
    pass


app = Dash(__name__)
_layout = crear_layout()
if _layout is not None:
    app.layout = _layout


if __name__ == "__main__":
    app.run(debug=True)
