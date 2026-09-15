"""
Funciones para el proyecto "Carrito de compras interactivo".

Este módulo se importa desde el notebook en notebooks/carrito_compras.ipynb
(ver INSTRUCCIONES.md en la raíz de este proyecto para la estructura completa
y las reglas de entrega). Completa las funciones marcadas con TODO.

Regla del proyecto: ninguna función de este archivo usa `input()` ni imprime
nada como parte de su lógica. Reciben datos, los transforman, y devuelven un
resultado (o lanzan un error). El `print()` y el `input()` viven en el notebook.
"""


# ---------------------------------------------------------------------------
# 1. Entrada y validación
# ---------------------------------------------------------------------------


def parsear_producto(linea):
    """
    Convierte una línea cruda como "manzana,3,2500" en un diccionario:
        {"producto": "Manzana", "cantidad": 3, "precio_unitario": 2500.0}

    - El nombre del producto queda limpio (sin espacios) y en formato título.
    - cantidad se convierte a int, precio_unitario a float.
    - Si la línea no tiene exactamente 3 partes separadas por coma, lanza
      ValueError("Formato inválido, usa: producto,cantidad,precio").
    - Si cantidad o precio no son números válidos, deja que el ValueError
      de int(...)/float(...) se propague tal cual (no lo captures aquí).

    Esta ya está resuelta — úsala de referencia para las que siguen.
    """
    partes = [p.strip() for p in linea.split(",")]
    if len(partes) != 3:
        raise ValueError("Formato inválido, usa: producto,cantidad,precio")

    nombre, cantidad_str, precio_str = partes
    return {
        "producto": nombre.title(),
        "cantidad": int(cantidad_str),
        "precio_unitario": float(precio_str),
    }


def validar_producto(producto):
    """
    Recibe un diccionario producto (como el que devuelve parsear_producto) y
    verifica que tenga sentido como compra real. Lanza ValueError con estos
    mensajes exactos según el caso:

    - Nombre vacío            -> "El nombre del producto no puede estar vacío"
    - cantidad <= 0           -> "La cantidad debe ser mayor que 0"
    - precio_unitario <= 0    -> "El precio debe ser mayor que 0"

    Si todo está bien, no devuelve nada y no lanza nada. Parsear un dato y
    validarlo son dos responsabilidades distintas: por eso son dos funciones.
    """
    # TODO: implementa las tres validaciones
    ...


# ---------------------------------------------------------------------------
# 2. Precios y descuentos
# ---------------------------------------------------------------------------


def calcular_descuento(cantidad):
    """
    Devuelve el porcentaje de descuento (como fracción, ej. 0.10 = 10%)
    según la cantidad comprada de un mismo producto:

        cantidad >= 10  -> 0.15
        cantidad >= 5   -> 0.10
        cantidad >= 3   -> 0.05
        cantidad < 3    -> 0.0

    Ejemplo: calcular_descuento(7) -> 0.10
    """
    # TODO: implementa las reglas de descuento con if/elif/else
    ...


def calcular_subtotal(producto):
    """
    Recibe un diccionario producto (con "cantidad" y "precio_unitario") y
    devuelve el subtotal ya con el descuento de calcular_descuento(...)
    aplicado:

        subtotal = cantidad * precio_unitario * (1 - descuento)

    Ejemplo: calcular_subtotal({"producto": "Manzana", "cantidad": 5, "precio_unitario": 2000})
             -> 9000.0   (5 * 2000 * 0.90)
    """
    # TODO: usa calcular_descuento(...) dentro de esta función
    ...


# ---------------------------------------------------------------------------
# 3. Operaciones sobre el carrito
# ---------------------------------------------------------------------------


def buscar_producto(carrito, nombre):
    """
    Devuelve el item del carrito cuyo "producto" coincida con `nombre`, o
    None si no está. La comparación no debe depender de mayúsculas/minúsculas
    ni de espacios sobrantes: buscar_producto(carrito, "  manzana ") tiene que
    encontrar el item guardado como "Manzana".

    Ojo: devuelve el diccionario mismo (no una copia), para que quien la llame
    pueda modificarlo. agregar_al_carrito se apoya en esta función — escríbela
    bien y la otra te queda mucho más corta.
    """
    # TODO: implementa la búsqueda
    ...


def agregar_al_carrito(carrito, producto):
    """
    Recibe la lista `carrito` (lista de diccionarios, cada uno con
    "producto", "cantidad", "precio_unitario" y "subtotal") y un nuevo
    `producto` (como el que devuelve parsear_producto, sin "subtotal").

    - Primero valida el producto con validar_producto(...).
    - Si el producto ya existe en el carrito, súmale la cantidad nueva al item
      existente y recalcula su "subtotal" con calcular_subtotal(...). Asume que
      el precio_unitario no cambia.
    - Si no existe, agrégalo como un item nuevo (con su "subtotal" ya calculado).
    - Devuelve el carrito actualizado.

    Reutiliza buscar_producto(...) en vez de volver a recorrer la lista a mano.
    """
    # TODO: valida, busca, y actualiza o inserta
    ...


# ---------------------------------------------------------------------------
# 4. Reportes
# ---------------------------------------------------------------------------


def resumen_carrito(carrito):
    """
    Recibe la lista `carrito` (con "subtotal" ya calculado en cada item) y
    devuelve un diccionario-reporte:

        {
            "total_items": <suma de todas las cantidades>,
            "total_pagado": <suma de todos los subtotales, redondeado a 2 decimales>,
            "producto_mas_caro": <nombre del producto con mayor subtotal>,
            "producto_top_cantidad": <nombre del producto con mayor cantidad>,
        }

    Si el carrito está vacío, devuelve:
        {"total_items": 0, "total_pagado": 0.0, "producto_mas_caro": None, "producto_top_cantidad": None}
    """
    # TODO: implementa el reporte agregado
    ...


def formatear_resumen(resumen):
    """
    Recibe el diccionario que devuelve resumen_carrito(...) y devuelve un
    string de varias líneas, listo para imprimir, con este formato:

        🧾 Resumen del carrito
          Unidades totales: 8
          Total a pagar: $12500.00
          Producto con mayor gasto: Manzana
          Producto con más unidades: Pera

    Si el carrito está vacío (total_items == 0), devuelve simplemente
    "El carrito está vacío."
    """
    # TODO: arma el string con f-strings (usa "\\n" entre líneas)
    ...
