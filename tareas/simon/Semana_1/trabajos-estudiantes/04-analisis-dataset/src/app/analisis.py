"""
Funciones de análisis para el proyecto "Indagación de un dataset".

Se importan desde el notebook en notebooks/analisis_dataset.ipynb (ver
INSTRUCCIONES.md en la raíz de este proyecto). Cada función recibe un
DataFrame de pandas y, en vez de devolver un valor para que el notebook lo
imprima, ella misma imprime su reporte con print(...). Completa las funciones
marcadas con TODO.
"""

import pandas as pd


def reporte_nulos(df):
    """
    Recibe un DataFrame e imprime, para cada columna que tenga al menos un
    valor faltante, cuántos valores faltantes tiene (de mayor a menor).
    Si ninguna columna tiene faltantes, imprime "(ninguno)".

    Pista: pandas ya sabe contar valores faltantes por columna con un solo
    método encadenado a df — no necesitas un for manual para contarlos
    (sí puedes usar un for para imprimir el resultado).
    """
    # TODO: implementa el reporte de nulos
    ...


def reporte_tipos(df):
    """
    Recibe un DataFrame e imprime el tipo de dato (dtype) de cada columna,
    una línea por columna: "  <columna>: <tipo>".
    """
    # TODO: implementa el reporte de tipos de datos
    ...


def reporte_tendencia_central(df, columnas=None):
    """
    Recibe un DataFrame y, opcionalmente, una lista de nombres de columnas.
    Si `columnas` es None, debes calcularlo tú: todas las columnas
    numéricas del DataFrame (pista: df.select_dtypes(...)).

    Para cada una de esas columnas imprime la media y la mediana:

        Price Per Unit: media=3.20, mediana=3.00, moda=no aplica (continua)
        Quantity: media=3.01, mediana=3.00, moda=2

    La moda es el caso interesante: **solo tiene sentido reportarla en
    variables discretas** (cantidades, conteos, categorías numéricas). En una
    variable continua —un precio, un total— casi ningún valor se repite, así
    que "el valor más frecuente" termina siendo un accidente de redondeo y no
    dice nada sobre el centro de los datos.

    Usa este criterio para decidir: si la columna tiene menos de 20 valores
    distintos, repórtala con moda; si tiene más, imprime
    "no aplica (continua)" en lugar del valor.

    Nota: puede haber más de una moda, o ninguna si la columna está vacía —
    revisa qué devuelve pandas antes de asumir que siempre hay exactamente
    un valor.
    """
    # TODO: implementa el reporte de tendencia central, decidiendo por columna
    # si la moda aplica o no
    ...


def operacion_entre_columnas(df, columna_a, columna_b, operador):
    """
    Recibe un DataFrame, dos nombres de columna, y un operador como string:
    "+", "-", "*" o "/". Devuelve una nueva Serie resultado de aplicar esa
    operación elemento a elemento entre las dos columnas (por ejemplo,
    columna_a * columna_b).

    Esta función SÍ devuelve un valor (no imprime) — la usarás dentro de
    analizar_dataframe para, por ejemplo, verificar si el total reportado
    coincide con cantidad * precio_unitario.
    """
    # TODO: implementa la operación entre columnas
    ...


def analizar_dataframe(df):
    """
    Función principal. Recibe el DataFrame completo del dataset y llama,
    en orden, a reporte_nulos, reporte_tipos y reporte_tendencia_central,
    imprimiendo un separador en blanco entre cada reporte.

    Además, usa operacion_entre_columnas para comparar dos columnas
    numéricas relacionadas del dataset (tú decides cuáles tienen sentido
    para el dataset que te dieron) y reporta cuántas filas son
    inconsistentes entre sí (por ejemplo, si el total no coincide con
    cantidad * precio).
    """
    # TODO: orquesta las llamadas a los reportes de arriba
    ...
