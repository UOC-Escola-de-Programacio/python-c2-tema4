# python-c2-tema4-sol

# Tema 4. Visualización de datos

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás tener configurado tu entorno de python.

### Librerías

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

```bash
pip install -r requirements.txt
```

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciados

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python (o en una carpeta, cuando el ejercicio tenga varios ficheros), que incluirá un comentario con el enunciado del ejercicio.

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios |
| -------- | ---------- |
| a. Visualización de datos | [ej4a1](4a/ej4a1.py) [ej4a2](4a/ej4a2/) |
| b. El framework Bokeh | [ej4b1](4b/ej4b1.py) [ej4b2](4b/ej4b2.py) [ej4b3](4b/ej4b3.py) [ej4b4](4b/ej4b4.py) [ej4b5](4b/ej4b5/) [ej4b6](4b/ej4b6/) |
| c. Los frameworks Dash y Plotly | [ej4c1](4c/ej4c1.py) [ej4c2](4c/ej4c2.py) [ej4c3](4c/ej4c3/) [ej4c4](4c/ej4c4/) |

Cada apartado tiene además su propio `README.md` con el detalle de sus ejercicios:

* [4a/README.md](4a/README.md) — Visualización de datos
* [4b/README.md](4b/README.md) — El framework Bokeh
* [4c/README.md](4c/README.md) — Los frameworks Dash y Plotly

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta.

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor.

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos
En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad.

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest
```
```bash
python -m pip install -r requirements.txt
```
Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.

### Django (apartado 4a)

Para arrancar el servidor de desarrollo del ejercicio ej4a2:
```bash
cd 4a/ej4a2
python manage.py runserver
```

### Dash (apartado 4c)

Para arrancar cualquiera de las apps de Dash:
```bash
cd 4c/ej4c3   # o 4c/ej4c4
python app.py
```

### Bokeh server (apartado 4b)

Para arrancar la app de Bokeh server del ejercicio ej4b5:
```bash
cd 4b/ej4b5
bokeh serve --show .
```

Para el ejercicio ej4b6 (Bokeh server embebido en Django) hacen falta dos
procesos, el servidor de Bokeh y el de Django:
```bash
cd 4b/ej4b6
bokeh serve bokeh_app --allow-websocket-origin=127.0.0.1:8000
# en otra terminal
cd 4b/ej4b6
python manage.py runserver
```
