# Proyecto: Indagación de un dataset

Vas a analizar un dataset real (no es Airbnb NYC — ya lo trabajaste en la sesión de Pandas) siguiendo la misma organización de proyecto que en el ejercicio del carrito: notebook para cargar datos y mostrar resultados, funciones de análisis separadas en su propio módulo.

## 1. El dataset

**El profesor te va a enviar el archivo `.csv`.** Apenas lo recibas, colócalo dentro de la carpeta `data/` de este proyecto; el notebook lo lee desde ahí.

Son **ventas de una cafetería**: cada fila es una transacción, con estas columnas:

| Columna | Qué contiene |
| --- | --- |
| `Transaction ID` | Identificador único de la transacción |
| `Item` | Producto vendido |
| `Quantity` | Unidades vendidas (numérica **discreta**) |
| `Price Per Unit` | Precio unitario (numérica **continua**) |
| `Total Spent` | Total de la transacción (numérica **continua**) |
| `Payment Method` | Medio de pago |
| `Location` | Dónde se hizo la venta |
| `Transaction Date` | Fecha de la transacción |

Dos cosas que debes saber antes de empezar, porque son el corazón del ejercicio:

1. **Tiene valores faltantes a propósito**, y no solo en las columnas de texto: también faltan cantidades, precios y totales.
2. **Tiene inconsistencias a propósito.** Fíjate en la relación que *debería* cumplirse entre `Quantity`, `Price Per Unit` y `Total Spent`, y verifica si de verdad se cumple en todas las filas. Ahí es donde vas a usar `operacion_entre_columnas`.

No tienes que "arreglar" el dataset para entregar, pero sí tienes que **detectar y explicar** qué está mal (ver punto 4).

## 2. Qué tienes que resolver

En `src/app/analisis.py` (con TODOs y docstrings) hay 5 funciones. Todas reciben un `DataFrame` de pandas como parámetro, y en vez de devolver algo para que el notebook lo imprima, **la función misma imprime su reporte**:

1. `reporte_nulos(df)` — cuántos valores faltantes tiene cada columna.
2. `reporte_tipos(df)` — qué tipo de dato está leyendo pandas en cada columna.
3. `reporte_tendencia_central(df, columnas=None)` — media y mediana de las columnas numéricas. **La moda solo se reporta donde tiene sentido**: en `Quantity` (discreta) sí; en `Price Per Unit` o `Total Spent` (continuas) el "valor más frecuente" es un accidente de redondeo, no el centro de los datos. El docstring trae el criterio concreto para decidirlo.
4. `operacion_entre_columnas(df, columna_a, columna_b, operador)` — aplica `+`, `-`, `*` o `/` entre dos columnas (esta sí devuelve un valor, para que la uses dentro de la función principal).
5. `analizar_dataframe(df)` — la función principal: encadena las tres anteriores e incluye una comparación entre dos columnas numéricas relacionadas del dataset (tú decides cuáles, según lo que tenga sentido para los datos que te dieron), reportando cuántas filas resultan inconsistentes.

El notebook en `notebooks/analisis_dataset.ipynb` solo carga el CSV con pandas, importa `analisis.py`, y llama a estas funciones — no vuelvas a escribir la lógica ahí.

## 3. Estructura obligatoria del proyecto

```
04-analisis-dataset/
├── data/
│   └── (el csv que te envía el profesor)
├── notebooks/
│   └── analisis_dataset.ipynb
├── src/
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       └── analisis.py
├── pyproject.toml
└── uv.lock
```

Los datos van en `data/`, el notebook en `notebooks/`, el código en `src/app/`. Los `__init__.py` ya vienen creados: son los que hacen que `src/app/` sea un paquete importable y no una carpeta cualquiera — no los borres.

El import desde el notebook hacia `src/app/` es el mismo problema que ya resolviste en el proyecto del carrito (`PYTHONPATH` / `pyproject.toml`) — reutiliza esa solución y déjala explicada.

## 4. La reflexión también es parte de la entrega

Al final del notebook hay una celda de markdown con preguntas sobre lo que encontraste (nulos, diferencias entre media y mediana, cómo corregirías inconsistencias). Respóndela en texto — no es opcional, es parte de lo que se evalúa.

## 5. Qué debes entregar

Un `.zip` de esta carpeta del proyecto (mismas reglas que en el proyecto del carrito): incluye `notebooks/` con las celdas corridas y la reflexión respondida, `src/app/`, `pyproject.toml` y `uv.lock`. **No incluyas `.venv`** y tampoco el `.csv` del dataset — ese ya lo tenemos nosotros, y así tu entrega pesa poco.

## 6. Criterios (qué vamos a revisar)

- Las 5 funciones de `src/app/analisis.py` funcionan según sus docstrings y reciben un DataFrame como parámetro.
- El notebook no contiene lógica de análisis, solo carga datos y llama a las funciones.
- El reporte de tendencia central identifica bien las columnas numéricas, y distingue dónde la moda aporta información y dónde no.
- La comparación entre columnas tiene sentido para el dataset (no es una operación arbitraria).
- La reflexión final muestra que entendiste *por qué* la media puede engañar cuando hay outliers o inconsistencias — esto conecta directamente con lo que viste en la Sesión 1.
