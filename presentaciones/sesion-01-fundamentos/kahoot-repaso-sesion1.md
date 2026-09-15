# Kahoot de repaso — Sesión 1

Kahoot **no evaluable**, pensado para los primeros ~10 minutos de la Sesión 2, repasando los conceptos de la Sesión 1 (motivación, estructuras de datos nativas de Python y análisis descriptivo). 16 preguntas de opción múltiple, tono cálido y sin trampas — el objetivo es repasar, no reprobar a nadie.

Cada pregunta incluye las 4 opciones (✅ marca la correcta) y una línea de **"Por qué"** para que el profesor la lea en voz alta apenas Kahoot muestre el resultado, reforzando el concepto en el momento.

---

## Bloque 1 · Motivación (3 preguntas)

**1. ¿Qué es la ciencia de datos, según lo que vimos en la motivación del curso?**
A. Aprender a programar en Python
B. ✅ Convertir datos crudos y desordenados en decisiones, historias y valor
C. Crear inteligencia artificial desde cero
D. Hacer gráficos bonitos en Excel

*Por qué:* la ciencia de datos no es "saber programar" — es un proceso de convertir datos en decisiones y valor, sin importar el sector.

**2. ¿Por qué no deberíamos confiar ciegamente en lo que responde un LLM (ChatGPT, Gemini, Claude)?**
A. Porque son muy lentos
B. Porque son gratis
C. ✅ Porque son productos de empresas y pueden equivocarse con total seguridad
D. Porque todavía no existen

*Por qué:* los LLMs son herramientas poderosas, pero no son oráculos — pueden "alucinar" datos con total seguridad y reflejar sesgos de sus datos de entrenamiento.

**3. Según lo que vimos, ¿cuál es la habilidad que de verdad va a marcar la diferencia de aquí en adelante?**
A. Escribir prompts más rápido que los demás
B. Memorizar comandos de la terminal
C. ✅ Saber juzgar si una respuesta —de un LLM o de cualquier herramienta— tiene sentido
D. Tener siempre la última versión de cada IA

*Por qué:* saber *usar* una herramienta ya no alcanza; lo que da poder de verdad es saber *juzgarla* — y eso requiere entender los fundamentos que estamos construyendo en el curso.

---

## Bloque 2 · Estructuras de datos nativas de Python (4 preguntas)

**4. Tienes `nota_texto = "4.5"` y necesitas sumarla a otras notas. ¿Qué debes hacer antes de poder sumarla?**
A. Usar `.strip()` para limpiar espacios
B. ✅ Convertirla con `float()` — está guardada como texto (`str`), no como número
C. Nada, Python la suma automáticamente
D. Usar `type()` para arreglarla

*Por qué:* los datos reales casi nunca llegan en el tipo que necesitas — hay que convertir explícitamente con `int()`/`float()`/`str()` (casting) antes de operar con ellos. Es, casi siempre, el primer error que se depura al trabajar con datos reales.

**5. Tienes `nombre_sucio = "  ana gomez  "`. ¿Qué método usarías para quitar los espacios sobrantes al inicio y al final?**
A. `.upper()`
B. ✅ `.strip()`
C. `.split()`
D. `.replace()`

*Por qué:* `.strip()` elimina espacios en blanco al principio y al final del texto — algo que vamos a necesitar constantemente para limpiar datos reales (¡la próxima sesión ya lo usamos con Pandas!).

**6. Dada `notas = [3.5, 4.0, 2.8, 5.0, 4.2]`, si recorres la lista con un `for` y cuentas cuántas notas son mayores o iguales a 3.0, ¿cuántas cuentas?**
A. 5
B. ✅ 4
C. 3
D. 2

*Por qué:* solo 2.8 queda por debajo de 3.0 — las otras cuatro (3.5, 4.0, 5.0, 4.2) sí cumplen la condición. Este patrón de `for` + `if` para filtrar y contar es la base de casi todo el análisis exploratorio.

**7. Tienes `estudiante = {"nombre": "Ana", "nota": 4.5}`. ¿Cómo accedes al valor de la nota?**
A. `estudiante[1]`
B. `estudiante.nota`
C. ✅ `estudiante["nota"]`
D. `estudiante(nota)`

*Por qué:* a diferencia de una lista (donde se accede por posición: 0, 1, 2…), en un diccionario se accede por la llave/etiqueta — `estudiante["nota"]`, sin importar el orden en que se guardó.

---

## Bloque 3 · Análisis descriptivo (9 preguntas)

**8. ¿Cuál es la diferencia entre un análisis descriptivo y uno diagnóstico?**
A. Son exactamente lo mismo
B. ✅ El descriptivo dice QUÉ pasó; el diagnóstico explica POR QUÉ pasó
C. El diagnóstico siempre es más fácil que el descriptivo
D. El descriptivo predice el futuro

*Por qué:* "cuántas ventas tuvimos" es descriptivo; "por qué bajaron las ventas" ya es diagnóstico — eso viene más adelante en la especialización.

**9. Un dato es…**
A. Solo un número
B. ✅ Un valor u observación sobre algo: una edad, un precio, una respuesta, una fecha
C. Lo mismo que una variable
D. Un error de programación

*Por qué:* cuando reunimos muchos datos sobre lo mismo tenemos una **variable** (ej. "edad de los clientes"); los datos son los valores individuales (34, 28, 45…) de esa variable.

**10. ¿Qué tipo de dato es "el color favorito de un cliente" (rojo, azul, verde…)?**
A. Cuantitativo continuo
B. Cuantitativo discreto
C. ✅ Cualitativo (categórico)
D. Ninguno de los anteriores — eso no es un dato

*Por qué:* son categorías/etiquetas, no números — no se promedian, se cuentan. Por eso la única medida de tendencia central que tiene sentido ahí es la Moda.

**11. Un equipo tiene estos salarios mensuales (en millones): 2, 2, 3, 3, 3, 4, 4, 25. ¿Por qué la MEDIA (5.75) no representa bien el salario "típico" del equipo?**
A. Porque la media siempre está mal
B. ✅ Porque hay un valor atípico (25) que la infla muy por encima de lo que gana la mayoría
C. Porque el equipo tiene muy pocos datos
D. Porque falta calcular la moda

*Por qué:* un solo valor extremo puede "jalar" la media lejos de donde está la mayoría de los datos reales.

**12. En ese mismo ejemplo de salarios, ¿cuál medida representa mejor el salario "típico" del equipo?**
A. La media
B. ✅ La mediana
C. La varianza
D. La desviación estándar

*Por qué:* la mediana (3) no se deja arrastrar por el valor extremo — por eso en las noticias casi siempre se habla de "salario mediano", no "salario promedio".

**13. ¿Para qué sirve la Moda que no sirven ni la media ni la mediana?**
A. ✅ Para datos categóricos (no numéricos), como el color de carro más vendido
B. Para datos con muchos decimales
C. Para calcular la dispersión de los datos
D. Para nada especial — es igual a la media

*Por qué:* la moda es la única de las tres que también tiene sentido con datos categóricos — no se puede "promediar" un color.

**14. ¿Qué nos dice la Desviación Estándar sobre un conjunto de datos?**
A. El valor más repetido
B. ✅ Qué tan lejos o dispersos están, en promedio, los datos respecto a la media
C. El valor máximo del conjunto
D. Cuántos datos hay en total

*Por qué:* dos grupos pueden tener exactamente la misma media y comportarse muy distinto — la desviación estándar dice qué tan "parejo" o disperso es cada grupo.

**15. Una desviación estándar de 5 puede ser "poca" o "mucha" según el caso: altura (media 170 cm) vs. peso (media 70 kg). ¿Qué mide el Coeficiente de Variación (CV) que la desviación estándar sola no muestra?**
A. Nada nuevo, es lo mismo que la desviación estándar
B. ✅ Qué tan grande es la dispersión *en relación con* la media — permite comparar variables de escalas distintas
C. El valor máximo del conjunto de datos
D. Si los datos son categóricos o numéricos

*Por qué:* CV = (Desviación estándar / Media) × 100%. Con la misma desviación (5), el CV de la altura es ≈2.9% (poco disperso) y el del peso ≈7.1% (más disperso) — la desviación sola no distinguía eso.

**16. En el caso de TiendaExpress (30 tiempos de entrega), la media fue 26.37 min y la desviación estándar 8.43 min. ¿Qué significa esto?**
A. Que todas las entregas tardan exactamente 26.37 minutos
B. ✅ Que hay bastante inconsistencia: el tiempo típico es bueno, pero algunas entregas se disparan muy por encima del promedio
C. Que el negocio no tiene ningún problema
D. Que ya podemos predecir cuál pedido específico va a tardar

*Por qué:* una desviación estándar de casi un tercio del promedio confirma que sí hay un problema real de consistencia en las entregas — no solo quejas aisladas. (Predecir cuál pedido va a tardar sería un problema de clasificación/ML, no descriptivo.)

---

*Nota: estas preguntas están pensadas para recrearse manualmente en la plataforma Kahoot (kahoot.com) — este archivo es solo el contenido en Markdown, no un archivo de importación específico de Kahoot.*
