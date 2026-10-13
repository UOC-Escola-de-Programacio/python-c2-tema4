# Ejercicio 4a2 — Django "a mano" sirviendo un gráfico de pandas

## Enunciado

En el ejercicio anterior (`../ej4a1.py`) generamos un gráfico de forma local,
sin ningún servidor de por medio. Ahora vamos a dar un paso más: construir a
mano (sin usar `django-admin startproject`, para entender bien cada pieza) una
pequeña aplicación web Django que, en el backend, utiliza **pandas** para
preparar los datos y **matplotlib** para dibujar el gráfico, y expone el
resultado como una imagen PNG servida por una vista de Django.

Es un enfoque deliberadamente "lento": cada vez que se solicita la página, el
servidor vuelve a construir el DataFrame y a renderizar el gráfico desde cero
antes de poder responder. No hay cacheo ni pre-cálculo: así se aprecia mejor
cómo pandas/matplotlib trabajan en el backend de una aplicación web, en
contraste con los frameworks reactivos (Bokeh, Dash, Plotly) que veremos en
los siguientes apartados.

## Estructura del proyecto

```
ej4a2/
├── manage.py            # Punto de entrada de Django (escrito a mano)
├── mysite/               # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── plots/                # App que genera y sirve el gráfico
    ├── __init__.py
    ├── apps.py
    ├── chart.py          # Lógica de pandas/matplotlib, independiente de Django
    ├── urls.py
    └── views.py
```

## Tareas

1. Revisar la configuración mínima de Django en `mysite/settings.py`,
   `mysite/urls.py` y `mysite/wsgi.py`.
2. Revisar `plots/chart.py`, donde se construye el DataFrame con pandas y se
   genera la figura con matplotlib (sin ninguna dependencia de Django).
3. Revisar las vistas de `plots/views.py`:
   - `grafico_png`: genera el gráfico con pandas/matplotlib en cada petición
     y lo devuelve como una `HttpResponse` de tipo `image/png`.
   - `pagina_principal`: muestra una página HTML sencilla incrustando la
     imagen anterior con una etiqueta `<img>`.
4. Ejecutar el servidor de desarrollo y comprobar el resultado en el
   navegador.

## Cómo ejecutarlo

Instala las dependencias específicas de este ejercicio (o usa el
`requirements.txt` de la raíz del repositorio, que ya las incluye):

```bash
pip install -r requirements.txt
```

Arranca el servidor de desarrollo:

```bash
python manage.py runserver
```

Y visita <http://127.0.0.1:8000/> en el navegador. Cada recarga de la página
vuelve a generar el gráfico desde cero en el servidor.
