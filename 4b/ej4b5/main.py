"""
Enunciado:
Hasta ahora, todos los ejercicios de Bokeh generaban un fichero HTML
autocontenido con `output_file`/`save`. Bokeh ofrece además un **servidor**
(`bokeh serve`) que mantiene un documento Python vivo en el backend: los
callbacks se ejecutan en Python (no en JavaScript como en `ej4b4`) y pueden
actualizar la figura sin necesidad de recargar la página.

En este ejercicio reproducirás el ejemplo más sencillo de la documentación
oficial de Bokeh server: una figura vacía y un botón que, en cada clic,
añade un punto en una posición aleatoria mediante un callback de Python.

Tareas:
1. Crear una figura vacía (sin datos iniciales) con un `ColumnDataSource`.
2. Definir un callback de Python que añada un nuevo punto a ese
   `ColumnDataSource` cada vez que se invoca.
3. Crear un `Button` y asociarle el callback con `on_click`.
4. Añadir el botón y la figura al documento del servidor con
   `curdoc().add_root(...)`.

Para arrancar el servidor de Bokeh:

    cd 4b/ej4b5
    bokeh serve --show .

Y visita <http://localhost:5006/ej4b5> en el navegador (se abrirá
automáticamente con la opción `--show`). Cada clic en el botón añadirá un
nuevo punto a la figura.
"""

from random import random

from bokeh.layouts import column
from bokeh.models import Button, ColumnDataSource
from bokeh.palettes import RdYlBu3
from bokeh.plotting import curdoc, figure

COLOR_MAS_RECIENTE = RdYlBu3[0]


def crear_figura_y_fuente():
    """
    Crea una figura vacía (sin puntos iniciales) junto con el
    `ColumnDataSource` que irá recibiendo los puntos añadidos por el botón.

    Devuelve una tupla (figura, fuente).
    """
    # TODO: implementa esta función.
    pass


def anadir_punto_aleatorio(fuente):
    """
    Callback de Python que añade un punto en una posición aleatoria al
    `ColumnDataSource` recibido. Se ejecuta en el servidor (no en el
    navegador) cada vez que se invoca, por ejemplo al pulsar un botón.

    Sigue la buena práctica de Bokeh de actualizar `.data` en un solo paso
    con un diccionario nuevo, en lugar de mutar las listas existentes.
    """
    # TODO: implementa esta función.
    pass


def crear_boton(fuente):
    """
    Crea el botón "Añadir punto" y le asocia el callback
    `anadir_punto_aleatorio` para que se ejecute en cada clic.
    """
    # TODO: implementa esta función.
    pass


def crear_layout():
    """
    Construye la figura, la fuente de datos y el botón, y devuelve el
    layout completo (una columna con el botón y la figura) junto con la
    fuente, para facilitar las pruebas.
    """
    # TODO: implementa esta función.
    pass


# `bokeh serve` ejecuta este módulo una vez por cada sesión de navegador,
# construyendo el layout y añadiéndolo al documento del servidor mediante
# `curdoc()`. Al importar `main.py` desde los tests, estas líneas también se
# ejecutan, pero `curdoc().add_root(...)` no tiene efectos secundarios si no
# hay un servidor de Bokeh en ejecución.
#
# Mientras `crear_layout` no esté implementada, `_resultado` será `None` y
# el módulo se podrá seguir importando sin errores (por ejemplo, desde los
# tests de las funciones anteriores).
_resultado = crear_layout()
if _resultado is not None:
    layout, fuente = _resultado
    curdoc().add_root(layout)
    curdoc().title = "Ejercicio 4b5"
