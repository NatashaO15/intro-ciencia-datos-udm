"""
Funciones del proyecto "Carrito de compras interactivo" — versión resuelta
(uso del profesor). La versión con TODOs que reciben los estudiantes está en
para-revisar/03-carrito-compras/src/app/carrito.py.
"""


def parsear_producto(linea):
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
    if not producto["producto"]:
        raise ValueError("El nombre del producto no puede estar vacío")
    if producto["cantidad"] <= 0:
        raise ValueError("La cantidad debe ser mayor que 0")
    if producto["precio_unitario"] <= 0:
        raise ValueError("El precio debe ser mayor que 0")


def calcular_descuento(cantidad):
    if cantidad >= 10:
        return 0.15
    elif cantidad >= 5:
        return 0.10
    elif cantidad >= 3:
        return 0.05
    return 0.0


def calcular_subtotal(producto):
    cantidad = producto["cantidad"]
    precio_unitario = producto["precio_unitario"]
    descuento = calcular_descuento(cantidad)
    return cantidad * precio_unitario * (1 - descuento)


def buscar_producto(carrito, nombre):
    objetivo = nombre.strip().title()
    for item in carrito:
        if item["producto"] == objetivo:
            return item
    return None


def agregar_al_carrito(carrito, producto):
    validar_producto(producto)

    item = buscar_producto(carrito, producto["producto"])
    if item is not None:
        item["cantidad"] += producto["cantidad"]
        item["subtotal"] = calcular_subtotal(item)
        return carrito

    nuevo_item = dict(producto)
    nuevo_item["subtotal"] = calcular_subtotal(producto)
    carrito.append(nuevo_item)
    return carrito


def resumen_carrito(carrito):
    if not carrito:
        return {
            "total_items": 0,
            "total_pagado": 0.0,
            "producto_mas_caro": None,
            "producto_top_cantidad": None,
        }

    total_items = sum(item["cantidad"] for item in carrito)
    total_pagado = round(sum(item["subtotal"] for item in carrito), 2)
    producto_mas_caro = max(carrito, key=lambda item: item["subtotal"])["producto"]
    producto_top_cantidad = max(carrito, key=lambda item: item["cantidad"])["producto"]

    return {
        "total_items": total_items,
        "total_pagado": total_pagado,
        "producto_mas_caro": producto_mas_caro,
        "producto_top_cantidad": producto_top_cantidad,
    }


def formatear_resumen(resumen):
    if resumen["total_items"] == 0:
        return "El carrito está vacío."

    return (
        "🧾 Resumen del carrito\n"
        f"  Unidades totales: {resumen['total_items']}\n"
        f"  Total a pagar: ${resumen['total_pagado']:.2f}\n"
        f"  Producto con mayor gasto: {resumen['producto_mas_caro']}\n"
        f"  Producto con más unidades: {resumen['producto_top_cantidad']}"
    )
