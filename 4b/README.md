# Apartado 4b — El framework Bokeh

Bokeh es una biblioteca de visualización interactiva para el navegador: a
diferencia de matplotlib (que vimos en el apartado 4a), genera gráficos en
HTML/JavaScript que permiten hacer zoom, desplazarse, mostrar tooltips o
reaccionar a controles sin necesidad de volver a ejecutar Python.

Los ejercicios de este apartado están pensados para aprender Bokeh de forma
progresiva:

| Ejercicio | Contenido |
| --------- | --------- |
| [ej4b1](ej4b1.py) | Primera figura: `figure`, glyphs (`line`, `scatter`) y `output_file`/`save` |
| [ej4b2](ej4b2.py) | `ColumnDataSource` a partir de un DataFrame de pandas + `HoverTool` |
| [ej4b3](ej4b3.py) | Layouts: combinar varias figuras con `gridplot` |
| [ej4b4](ej4b4.py) | Widgets (`Slider`) + interactividad con `CustomJS`, sin servidor |
| [ej4b5](ej4b5/main.py) | Primera app de **Bokeh server** (`bokeh serve`): callback de Python disparado por un `Button` |
| [ej4b6](ej4b6/) | Bokeh server embebido en una vista de **Django** con `bokeh.embed.server_document` |

Cada ejercicio genera un fichero HTML autocontenido (ignorado por git) que
puedes abrir directamente en el navegador para comprobar el resultado:

```bash
python ej4b1.py
# abre el fichero ej4b1_temperaturas.html generado en esta carpeta
```

## Cómo ejecutar las apps de Bokeh server

Los ejercicios [ej4b5](ej4b5/main.py) y [ej4b6](ej4b6/) no generan un fichero
HTML, sino que se ejecutan con el servidor de Bokeh (`bokeh serve`), que
mantiene un documento Python vivo en el backend y permite que los callbacks
se ejecuten en Python en lugar de en JavaScript.

```bash
cd ej4b5
bokeh serve --show .
```

Y visita <http://localhost:5006/ej4b5> en el navegador si no se ha abierto
automáticamente.

El ejercicio [ej4b6](ej4b6/) va un paso más allá e incrusta esa misma app de
Bokeh server dentro de una página servida por Django. Se necesitan **dos
procesos** en marcha a la vez:

```bash
# Terminal 1: el servidor de Bokeh con la app de ej4b6/bokeh_app
cd ej4b6
bokeh serve bokeh_app --allow-websocket-origin=127.0.0.1:8000

# Terminal 2: el servidor de desarrollo de Django
cd ej4b6
python manage.py runserver
```

Y visita <http://127.0.0.1:8000/> en el navegador: la página de Django
incrusta la sesión de Bokeh server mediante
`bokeh.embed.server_document`.

