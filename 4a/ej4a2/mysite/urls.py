"""
URLs raíz del proyecto: delega todo en las URLs de la app `plots`.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("plots.urls")),
]
