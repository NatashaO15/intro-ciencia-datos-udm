# Proyecto: Carrito de compras interactivo

Esta vez el ejercicio no es solo escribir funciones — es **organizar un proyecto** como se hace en la industria: notebook para correr y mostrar resultados, código reutilizable separado en su propio módulo, y dependencias gestionadas con `uv`.

Hay dos cosas que se evalúan por separado: que las funciones queden bien, y que entiendas **qué configuración hace falta para que un proyecto así funcione**.

## 1. Las funciones que tienes que escribir

Están todas en `src/app/carrito.py`, con su docstring explicando exactamente qué debe hacer cada una, qué debe devolver y qué error debe lanzar. Solo `parsear_producto` viene resuelta, como referencia de estilo.

**Entrada y validación**
1. `parsear_producto(linea)` — *ya resuelta, es tu ejemplo*.
2. `validar_producto(producto)` — rechaza nombres vacíos, cantidades ≤ 0 y precios ≤ 0.

**Precios y descuentos**
3. `calcular_descuento(cantidad)` — 15% / 10% / 5% según la cantidad.
4. `calcular_subtotal(producto)` — aplica el descuento al subtotal.

**Operaciones sobre el carrito**
5. `buscar_producto(carrito, nombre)` — devuelve el item o `None`, sin importar mayúsculas ni espacios.
6. `agregar_al_carrito(carrito, producto)` — valida, y suma cantidades si el producto ya estaba.

**Reportes**
7. `resumen_carrito(carrito)` — diccionario con totales y máximos.
8. `formatear_resumen(resumen)` — el resumen final listo para imprimir.

Varias se apoyan en otras (`agregar_al_carrito` debe usar `buscar_producto` y `validar_producto`; `calcular_subtotal` debe usar `calcular_descuento`). **No repitas lógica**: eso también se revisa.

El notebook en `notebooks/carrito_compras.ipynb` **no define funciones**: solo importa lo que hay en `src/app/carrito.py`, pide productos al usuario con `input()`, y muestra los resultados.

## 2. Estructura obligatoria del proyecto

```
03-carrito-compras/
├── notebooks/
│   └── carrito_compras.ipynb
├── src/
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       └── carrito.py
├── pyproject.toml
└── uv.lock
```

- El notebook **debe** vivir dentro de `notebooks/`.
- El código (funciones) **debe** vivir dentro de `src/app/`.
- El notebook debe importar las funciones desde ahí — no las copies ni las vuelvas a escribir dentro del notebook.

### Sobre los `__init__.py`

Esos dos archivos vacíos ya vienen creados en el esqueleto, y **no los borres**: son los que le dicen a Python que esa carpeta es un *paquete* y no una carpeta cualquiera. Es la primera pieza de configuración del proyecto; la segunda la tienes que averiguar tú en el punto siguiente.

Vale la pena que investigues también por qué un archivo vacío alcanza para eso, y qué pasa si falta.

## 3. El import: la parte que tienes que investigar

Cuando el notebook y el `.py` están en la misma carpeta (como en las prácticas de la sesión pasada), `import archivo` simplemente funciona. Aquí ya no: `notebooks/` y `src/app/` son carpetas hermanas, y ese import directo va a fallar con un `ModuleNotFoundError`.

Esto es intencional. **No te vamos a dar la solución**, porque el objetivo real del ejercicio es que reconozcas cuáles son las configuraciones necesarias para que un proyecto quede bien armado. Estas son las pistas:

- 🔎 **`PYTHONPATH`**. Averigua qué es: dónde busca Python los módulos cuando escribes `import algo`, cómo se consulta esa lista desde el propio Python, y por qué la carpeta de tu notebook está ahí pero `src/` no. Entender esto explica el error que te va a salir.
- 🔎 **`pyproject.toml`**. Es el archivo de configuración del proyecto — el mismo que `uv` usa para las dependencias. Averigua qué se declara ahí para que *tu propio código* sea reconocido como un paquete importable, y qué comando hay que correr después de declararlo.
- 🔎 Compara las dos rutas. Una se resuelve en tiempo de ejecución dentro del notebook; la otra queda escrita en la configuración del proyecto. **No son equivalentes** cuando otra persona descomprime tu entrega.

Al final del notebook hay una celda de markdown con cuatro preguntas sobre esto. Responderlas es obligatorio y pesa en la nota tanto como el código.

## 4. Dependencias con `uv`

Este proyecto maneja sus dependencias con `uv` (ya lo usaste en `00-Setup`; revisa `00-Setup/03-dependency-management.md` si necesitas refrescar los comandos). Es un proyecto **independiente**: tiene su propio `pyproject.toml` y su propio `uv.lock`, no reutiliza los del repositorio del curso.

Como mínimo vas a necesitar `ipykernel` para poder correr el notebook. Si agregas algo más, que quede registrado en el `pyproject.toml`, no instalado a mano por fuera.

## 5. Qué debes entregar

Un **archivo comprimido (.zip)** de esta carpeta del proyecto, que debe incluir:

- `notebooks/carrito_compras.ipynb` (con las celdas corridas y las preguntas respondidas)
- `src/app/carrito.py`
- `pyproject.toml`
- `uv.lock`

**No comprimas ni incluyas la carpeta `.venv`.** Antes de entregar, investiga (y ten lista la respuesta si te preguntamos):

- ¿Cómo se hace en la industria para que Git —y, por extensión, lo que uno comparte o comprime— nunca incluya `.venv`?
- ¿Por qué se hace así, qué problema evita? (Pista: mira el `.gitignore` de la raíz de este mismo repositorio del curso, y compáralo con el hecho de que `uv.lock` sí se commitea. ¿Por qué uno sí y el otro no?)

## 6. Criterios (qué vamos a revisar)

- Las 8 funciones de `src/app/carrito.py` funcionan según sus docstrings, incluidos los mensajes de error exactos.
- Las funciones se reutilizan entre sí en vez de repetir lógica.
- El notebook no define lógica: solo importa, pide datos y muestra.
- La estructura de carpetas es la pedida y el import funciona.
- Las cuatro preguntas sobre el import y el `PYTHONPATH`/`pyproject.toml` están respondidas y demuestran que entendiste *por qué*, no solo *qué* copiaste.
- El `.zip` entregado no contiene `.venv` pero sí contiene `uv.lock`.
