"""
Enunciado:
La verdadera potencia de Dash está en los callbacks: funciones Python que se
ejecutan en el servidor cada vez que el usuario interactúa con un control
(un dropdown, un slider...) y que actualizan otros componentes de la página
sin necesidad de recargarla.

En este ejercicio construirás una app con un `dcc.Dropdown` para elegir una
ciudad y un `dcc.Graph` que se actualiza automáticamente, mediante un
callback, mostrando la evolución de temperatura de la ciudad seleccionada.

Tareas:
1. Construir un DataFrame de pandas "en formato largo" con la temperatura
   mensual de varias ciudades.
2. Definir el layout con un `dcc.Dropdown` (una opción por ciudad) y un
   `dcc.Graph` vacío inicialmente.
3. Escribir la función `actualizar_grafico`, registrada como callback con
   `@callback(Output(...), Input(...))`, que filtra el DataFrame según la
   ciudad seleccionada y devuelve la figura de Plotly correspondiente.
4. Ejecutar la app con `app.run()` para comprobar el resultado en el
   navegador.

Para arrancar la app:

    python app.py

Y visitar http://127.0.0.1:8050/ en el navegador.
"""

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

TEMPERATURAS_POR_CIUDAD = {
    "Barcelona": [10, 11, 13, 15, 18, 22, 25, 25, 22, 18, 13, 11],
    "Madrid": [6, 8, 11, 14, 18, 23, 27, 26, 22, 16, 10, 7],
    "Bilbao": [9, 10, 12, 13, 16, 19, 21, 21, 19, 15, 12, 10],
}
CIUDADES = list(TEMPERATURAS_POR_CIUDAD.keys())


def crear_dataframe_temperaturas():
    """
    Construye un DataFrame "en formato largo" (una fila por ciudad y mes)
    con la temperatura media mensual de varias ciudades.
    """
    # TODO: implementa esta función.
    pass


DF_TEMPERATURAS = crear_dataframe_temperaturas()


def filtrar_por_ciudad(df_temperaturas, ciudad):
    """
    Filtra el DataFrame de temperaturas para quedarnos solo con los datos de
    la ciudad indicada, preservando el orden de los meses.
    """
    # TODO: implementa esta función.
    pass


def crear_figura_ciudad(df_temperaturas, ciudad):
    """
    Crea la figura de Plotly Express con la evolución de temperatura de la
    ciudad indicada.
    """
    # TODO: implementa esta función.
    pass


def crear_layout():
    """
    Construye y devuelve el layout de la app Dash: un título, un dropdown
    para elegir la ciudad y un gráfico que se actualizará vía callback.
    """
    # TODO: implementa esta función.
    pass


app = Dash(__name__)
_layout = crear_layout()
if _layout is not None:
    app.layout = _layout


@callback(
    Output("grafico-temperatura", "figure"),
    Input("selector-ciudad", "value"),
)
def actualizar_grafico(ciudad_seleccionada):
    """
    Callback de Dash: se ejecuta cada vez que cambia el valor del dropdown
    `selector-ciudad` y devuelve la nueva figura para `grafico-temperatura`.
    """
    # TODO: implementa esta función.
    pass


if __name__ == "__main__":
    app.run(debug=True)
