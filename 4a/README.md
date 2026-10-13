# Apartado 4a — Visualización de datos

Este apartado es un recordatorio de las dos formas "clásicas" (no reactivas)
de generar visualizaciones que ya se trabajaron en temas anteriores, antes de
entrar en los apartados 4b y 4c con frameworks interactivos (Bokeh, Dash,
Plotly).

| Ejercicio | Contenido |
| --------- | --------- |
| [ej4a1](ej4a1.py) | Gráfico de pandas (`DataFrame.plot()`) renderizado localmente con matplotlib y guardado como PNG |
| [ej4a2](ej4a2/) | App Django construida a mano que usa pandas/matplotlib en el backend para servir una imagen de un gráfico |

## ej4a1 — pandas + matplotlib en local

```bash
python ej4a1.py
```

Esto genera `ventas_mensuales.png` en esta misma carpeta, sin necesidad de
ningún servidor: todo el renderizado ocurre en el propio proceso de Python.

## ej4a2 — Django sirviendo un gráfico de pandas

Ver [ej4a2/README.md](ej4a2/README.md) para los detalles y cómo ejecutar la
aplicación. A diferencia de ej4a1, aquí el gráfico se genera en el backend de
una app web cada vez que se solicita, de forma deliberadamente "lenta" (sin
cacheo), como contraste con los frameworks reactivos de 4b y 4c.
