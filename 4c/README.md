# Apartado 4c — Los frameworks Dash y Plotly

Plotly es la biblioteca de gráficos interactivos sobre la que se construye
Dash, el framework para montar aplicaciones web analíticas completas usando
solo Python (sin escribir HTML, CSS ni JavaScript a mano).

| Ejercicio | Framework | Contenido |
| --------- | --------- | --------- |
| [ej4c1](ej4c1.py) | Plotly | `plotly.express`: gráfico de dispersión a partir de un DataFrame de pandas |
| [ej4c2](ej4c2.py) | Plotly | `plotly.graph_objects` + `make_subplots`: combinar varios gráficos en una figura |
| [ej4c3](ej4c3/app.py) | Dash | Primera app: layout estático con un gráfico de Plotly Express |
| [ej4c4](ej4c4/app.py) | Dash | App con un `dcc.Dropdown` y un callback (`@callback`) que actualiza el gráfico |

## Cómo ejecutar los ejercicios de Plotly

```bash
python ej4c1.py
# abre el fichero ej4c1_esperanza_vida.html generado en esta carpeta
```

## Cómo ejecutar las apps de Dash

```bash
cd ej4c3   # o ej4c4
python app.py
```

Y visita <http://127.0.0.1:8050/> en el navegador.
