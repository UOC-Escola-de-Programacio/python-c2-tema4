"""
Configuración mínima de Django para el ejercicio 4b6, escrita a mano (sin
`django-admin startproject`), al estilo de `4a/ej4a2/mysite/settings.py`.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Clave de desarrollo: NUNCA debe usarse una clave como esta en producción.
SECRET_KEY = "ej4b6-clave-de-desarrollo-no-usar-en-produccion"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "dashboard",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# No se necesita base de datos para este ejercicio.
DATABASES = {}

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URL del Bokeh server donde se sirve la app de `bokeh_app/main.py`. Se debe
# arrancar por separado con:
#   bokeh serve bokeh_app --allow-websocket-origin=127.0.0.1:8000
BOKEH_SERVER_URL = "http://localhost:5006/bokeh_app"
