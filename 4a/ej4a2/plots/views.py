"""
Vistas de la app `plots`.

- `grafico_png`: genera (de nuevo, en cada petición) el gráfico de
  temperaturas con pandas/matplotlib y lo devuelve como imagen PNG.
- `pagina_principal`: página HTML sencilla que incrusta la imagen anterior.
"""

from django.http import HttpResponse
from django.shortcuts import render

from .chart import generar_png_temperaturas


def grafico_png(request):
    """
    Devuelve el gráfico de temperaturas como una imagen PNG generada al
    vuelo. Al no cachear nada, cada petición vuelve a reconstruir el
    DataFrame y a renderizar la figura con matplotlib: un backend "lento"
    a propósito, como recordatorio del enfoque clásico frente a frameworks
    reactivos como Bokeh, Dash o Plotly.
    """
    # TODO: implementa esta función.
    pass


def pagina_principal(request):
    """
    Renderiza una página HTML que incrusta el gráfico generado por
    `grafico_png` mediante una etiqueta <img>.
    """
    # TODO: implementa esta función.
    pass
