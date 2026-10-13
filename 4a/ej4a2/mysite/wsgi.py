"""
Punto de entrada WSGI del proyecto, equivalente al que generaría
`django-admin startproject`.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
