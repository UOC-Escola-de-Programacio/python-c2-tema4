"""
URLs raíz del proyecto: delega todo en las URLs de la app `dashboard`.
"""

from django.urls import include, path

urlpatterns = [
    path("", include("dashboard.urls")),
]
