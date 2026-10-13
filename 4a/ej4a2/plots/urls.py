"""
URLs de la app `plots`.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina_principal, name="pagina_principal"),
    path("grafico.png", views.grafico_png, name="grafico_png"),
]
