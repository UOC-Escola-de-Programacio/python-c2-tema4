"""
Vistas de la app `dashboard`.

- `pagina_principal`: renderiza una página HTML que incrusta la app de
  Bokeh server (`bokeh_app/main.py`) mediante `bokeh.embed.server_document`.
"""

from bokeh.embed import server_document
from django.conf import settings
from django.shortcuts import render


def pagina_principal(request):
    """
    Genera el `<script>` que incrusta la sesión de Bokeh server (servida
    por separado con `bokeh serve bokeh_app`) y renderiza la plantilla que
    lo incluye en la página.

    `server_document` no necesita que el servidor de Bokeh esté
    efectivamente en marcha para generar el script: solo construye el
    HTML/JavaScript que el navegador usará para conectarse a él cuando se
    cargue la página.
    """
    # TODO: implementa esta función.
    pass
