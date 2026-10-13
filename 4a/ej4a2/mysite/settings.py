"""
Configuración mínima de Django para el ejercicio 4a2, escrita a mano (sin
`django-admin startproject`) para que sea fácil de leer de principio a fin.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Clave de desarrollo: NUNCA debe usarse una clave como esta en producción.
SECRET_KEY = "ej4a2-clave-de-desarrollo-no-usar-en-produccion"

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "plots",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "mysite.urls"

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

WSGI_APPLICATION = "mysite.wsgi.application"

# No se necesita base de datos para este ejercicio, todo el "estado" es el
# DataFrame que se calcula en cada petición.
DATABASES = {}

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
