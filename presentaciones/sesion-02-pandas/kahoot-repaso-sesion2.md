# Kahoot de repaso — Sesión 2

Kahoot **no evaluable**, pensado para los primeros ~10 minutos de la Sesión 3, repasando los conceptos de la Sesión 2 (historia y gobernanza de Pandas, clase/objeto, Series/DataFrame, Big O, y la limpieza del dataset Airbnb NYC). 16 preguntas de opción múltiple, tono cálido y sin trampas — el objetivo es repasar, no reprobar a nadie.

Cada pregunta incluye las 4 opciones (✅ marca la correcta) y una línea de **"Por qué"** para que el profesor la lea en voz alta apenas Kahoot muestre el resultado, reforzando el concepto en el momento.

---

## Bloque 1 · Pandas: historia y objetos (4 preguntas)

**1. ¿En qué año nació Pandas y quién lo creó?**
A. 2015, un equipo de NumFOCUS
B. ✅ 2008, Wes McKinney, en un fondo de inversión (AQR Capital Management)
C. 2020, en un curso universitario de ciencia de datos
D. 1995, junto con el propio Python

*Por qué:* Pandas nació resolviendo un problema real de análisis financiero en 2008, se volvió open source en 2009, y en 2015 pasó a ser patrocinado por NumFOCUS (la misma organización de NumPy, Jupyter y Matplotlib).

**2. ¿Quién mantiene Pandas hoy en día?**
A. Una sola empresa de tecnología
B. El gobierno de Estados Unidos
C. ✅ Una comunidad de ~15 desarrolladores voluntarios, la mayoría sin afiliación corporativa
D. Nadie — ya no se actualiza

*Por qué:* mismo mensaje que con "qué es un lenguaje de programación" en sesión 1 — Pandas no es magia ni una caja negra corporativa, es gente real resolviendo un problema real y sosteniéndolo por convicción.

**3. Según la analogía que vimos, ¿qué es una "clase" y qué es un "objeto"?**
A. Son exactamente lo mismo
B. ✅ La clase es el plano/molde; el objeto es la cosa concreta construida con ese plano
C. El objeto es el plano; la clase es la cosa concreta
D. Ninguno de los dos existe en Python

*Por qué:* la clase es como el plano de una casa; el objeto es una casa concreta construida con ese plano, con sus propios datos (atributos) y acciones que puede hacer (métodos).

**4. ¿Qué hace que una Series de Pandas sea distinta de un array común?**
A. Nada, son exactamente lo mismo
B. Una Series no puede contener números
C. ✅ Cada valor de una Series tiene una etiqueta (su índice), no solo una posición
D. Una Series solo puede tener un valor

*Por qué:* por dentro, una Series es un array de NumPy, pero con algo extra — cada valor tiene una etiqueta, así que puedes pedir "el valor de Juan" y no solo "el valor en la posición 3".

---

## Bloque 2 · DataFrame y particularidades de Pandas (4 preguntas)

**5. ¿Qué es un DataFrame, en relación con las Series?**
A. Es lo mismo que una Series
B. ✅ Es una tabla hecha de varias Series, todas compartiendo el mismo índice de filas
C. Es una lista de listas sin ninguna relación entre sí
D. Es un tipo de archivo CSV

*Por qué:* cada columna de un DataFrame es una Series independiente; todas comparten el mismo índice, por eso se alinean perfectamente como filas de una tabla.

**6. ¿Por qué puede ser peligroso asumir que el índice de un DataFrame es único?**
A. Porque Pandas nunca asigna un índice automático
B. ✅ Porque Pandas no exige que el índice sea único, y filtrar o combinar sin resetearlo puede duplicar valores sin avisar
C. Porque el índice siempre debe ser texto
D. Porque los DataFrames no tienen índice

*Por qué:* a diferencia de una llave primaria en una base de datos, Pandas no exige unicidad en el índice — por eso conviene usar `.reset_index(drop=True)` después de filtrar.

**7. Truco para recordar `axis=0` vs `axis=1` en métodos como `.mean()`: "axis es..."**
A. El número de columnas del DataFrame
B. ✅ La dirección que desaparece — `axis=0` colapsa las filas, `axis=1` colapsa las columnas
C. Siempre el eje de las columnas
D. Un parámetro que ya no se usa en Pandas

*Por qué:* `axis=0` (el default) hace que las filas desaparezcan y deja un valor por columna; `axis=1` hace que las columnas desaparezcan y deja un valor por fila.

**8. Vas a modificar valores de un DataFrame justo después de filtrarlo. ¿Qué deberías usar para evitar el `SettingWithCopyWarning`?**
A. `.head()`
B. ✅ `.loc[]`
C. `.describe()`
D. `print()`

*Por qué:* al filtrar y modificar en la misma línea, Pandas no siempre sabe si trabajas sobre el original o sobre una copia temporal — usar `df.loc[filtro, 'columna'] = valor` es la forma correcta y explícita.

---

## Bloque 3 · Rendimiento y Big O (4 preguntas)

**9. ¿Qué describe realmente la notación Big O?**
A. El número exacto de segundos que tarda un código
B. ✅ Qué tan rápido crece el tiempo de ejecución cuando crecen los datos
C. Cuántas líneas de código tiene un programa
D. El lenguaje de programación más rápido que existe

*Por qué:* Big O no mide segundos exactos — describe la forma en que la tardanza crece cuando el tamaño de los datos crece.

**10. Leer `df.shape` tarda lo mismo con 10 filas que con 10 millones. ¿Qué notación Big O es esa?**
A. ✅ O(1) — constante
B. O(n) — lineal
C. O(n²) — cuadrático
D. No tiene notación Big O

*Por qué:* O(1) significa tiempo constante — no importa cuántos datos haya, la operación tarda igual.

**11. ¿Por qué buscar `"Ana" in diccionario` suele ser mucho más rápido que `"Ana" in lista`?**
A. Los diccionarios son más rápidos al azar, sin razón técnica
B. ✅ La lista es O(n) y hay que recorrerla; el diccionario es O(1) en promedio gracias al hashing
C. Las listas no pueden contener texto
D. Los diccionarios siempre tienen menos elementos

*Por qué:* buscar en una lista puede requerir revisar todos los elementos (O(n)); un diccionario usa hashing para ir directo a la llave (O(1) en promedio) — por eso conviene usar diccionarios o sets para preguntas de tipo "¿está esto aquí?".

**12. El `for` de Python puro y el `.str` de Pandas hacen, técnicamente, el mismo trabajo O(n). ¿Por qué Pandas es más rápido en la práctica?**
A. Porque Pandas usa una notación Big O distinta
B. ✅ Porque Pandas/NumPy ejecutan ese recorrido en código C compilado, más rápido que el intérprete de Python
C. Porque Pandas en realidad no recorre los datos
D. No es más rápido, tarda exactamente igual siempre

*Por qué:* Big O describe cómo crece el tiempo, no cuánto pesa cada paso — dos códigos O(n) pueden tardar tiempos muy distintos en la práctica según qué tan "pesado" es cada paso.

---

## Bloque 4 · Limpieza del dataset Airbnb con Pandas (4 preguntas)

**13. Con `.isna().sum()` ven que `reviews_per_month` tiene 10,052 valores faltantes. ¿Qué significa eso?**
A. Que hay un error grave en el dataset que hay que eliminar sí o sí
B. ✅ Que esos anuncios nunca han recibido una reseña — es información real, no un dato roto
C. Que Pandas no pudo leer esas filas
D. Que el precio de esos anuncios es incorrecto

*Por qué:* faltante no siempre significa error — un anuncio sin reseñas no tiene `reviews_per_month` porque nunca lo han reseñado, y por eso lo rellenamos con 0 en vez de eliminarlo.

**14. Al mirar los percentiles de `price` con `.quantile()`, ¿qué encontraron como candidatos a valores atípicos?**
A. Anuncios con precios negativos
B. ✅ Anuncios en $0 (error de carga) y anuncios por encima de $1000
C. Anuncios sin ningún precio registrado
D. Todos los anuncios tenían el mismo precio

*Por qué:* el percentil 100% (el máximo) estaba muchísimo más lejos que la mediana — señal clara de valores atípicos, confirmada al contar anuncios en $0 y por encima de $1000.

**15. ¿Qué hace el accesor `.str` en Pandas, por ejemplo en `df['name'].str.strip().str.title()`?**
A. Convierte la columna completa a números
B. ✅ Aplica métodos de texto (como `.strip()`, `.title()`) a cada valor de la columna, de una sola vez
C. Elimina la columna completa
D. Solo funciona sobre una fila a la vez

*Por qué:* es la misma lógica de `.strip()`/`.title()` que usaron en sesión 1 sobre un string — el `.str` al frente le dice a Pandas que la aplique a toda la columna de golpe.

**16. Después de filtrar los precios atípicos (entre el percentil 1% y el 99%), ¿qué pasó con la media y la mediana del precio?**
A. No cambiaron en nada
B. ✅ Se acercaron entre sí — la media dejó de estar tan inflada por los valores extremos
C. La mediana desapareció
D. Se alejaron todavía más

*Por qué:* es la misma lección de los salarios y de TiendaExpress en sesión 1 — un análisis descriptivo solo es tan confiable como los datos que le des; al limpiar los atípicos, la media se acerca más al valor "típico" real.

---

*Nota: estas preguntas están pensadas para recrearse manualmente en la plataforma Kahoot (kahoot.com) — este archivo es solo el contenido en Markdown. El archivo `kahoot-sesion2-import.xlsx`, en esta misma carpeta, trae el mismo contenido en el formato de importación masiva de Kahoot.*
