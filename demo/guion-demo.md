# FactorUno — guía única (video + uso de la app)

**Video:** 5–7 minutos · **Aplicación:** FactorUno, el mantenedor de calificaciones tributarias de dividendos que desarrollé para la empresa **nuam** (la bolsa), a partir de su HDU real. **Caso:** cierre de dividendos del ejercicio 2024.
**Quién habla:** el autor del desarrollo, en primera persona. No se actúa como funcionario de nuam: se muestra la aplicación y se explica lo que hace.
**Regla del profesor:** mostrar la aplicación, no disertar. Frases de 5–10 segundos.
**Cómo leer esta guía:** cada toma dice, paso a paso, dónde hacer clic, qué escribir, qué decir y qué debe verse. Al final está el anexo con el uso completo de la app. Y si alguna palabra no se entiende, está **`glosario.md`** en esta misma carpeta: la explica en simple.

## Antes de grabar

- [ ] Abrir `http://100.57.30.193/`. Si no carga, el laboratorio está apagado: avisar y esperar.
- [ ] Usuario `admin` / `Admin1234!` (tomas 1 a 10). Solo la toma 11 usa `analista` / `Analista1234!`.
- [ ] Tener a mano los dos archivos CSV, que están en la carpeta `demo/` del proyecto (y en esta misma carpeta en Obsidian):
  - `carga-montos-demo-error.csv` → se usa en la toma 3.
  - `carga-montos-demo.csv` → se usa en la toma 4.
- [ ] Cerrar notificaciones y pestañas. Grabar en 1080p con la cámara a la vista.
- [ ] Si algo se traba: se corta y se repite esa toma.

## Los conceptos, en una línea cada uno

Esta sección es solo para preparar la grabación: no se lee en cámara.

| Dato | Qué es | Ejemplo de la demo |
|---|---|---|
| Ejercicio | El año comercial al que pertenece el dividendo. | 2024 |
| Mercado | Dónde se transó el instrumento: **ACN** acciones, **CFI** cuotas de fondos de inversión, **FM** fondos mutuos. | ACN |
| Instrumento | Quién pagó el dividendo: la empresa o el fondo. | ENEL AMERICAS S.A. |
| Fecha de pago | El día en que se pagó el dividendo (formato AAAA-MM-DD). | 2024-05-09 |
| Secuencia | Cuántos dividendos pagó ese instrumento en el año (1 = el primero). | 2 |
| N° de dividendo | El número de dividendo que trae el certificado del SII. | 880 |
| Tipo de sociedad | **A** = sociedad anónima abierta (cotiza en bolsa) · **C** = cerrada. | A |
| Valor histórico | El monto del dividendo, según el certificado. | 640000 |
| Montos (columnas 8 a 37) | El desglose del certificado DJ 1948 por tipo de renta y crédito. Cada grupo que aparece bajo el campo es un concepto de la homologación del SII. | col. 8 = 200000 |
| Suma de la base (8 a 19) | Los montos de esas columnas sumados: es la base del cálculo y no puede pasar de 1. | 320000 |
| Factores | Cada monto dividido por la base. Los calcula el sistema. | 200000 ÷ 320000 = 0,625 |

**En resumen:** el certificado dice cuánto se pagó y en qué columnas; la aplicación calcula qué parte de ese dividendo corresponde a cada concepto, deja la trazabilidad y genera el respaldo.

## Toma 1 — Entrar al sistema

**Hacer (clic por clic):**
1. Abrir `http://100.57.30.193/` en el navegador.
2. Clic en el campo **Usuario** y escribir `admin`.
3. Clic en el campo **Contraseña** y escribir `Admin1234!`.
4. Clic en el botón **Ingresar** del cuadro de acceso.

**Decir:** "Esta es FactorUno, la aplicación que desarrollé para la empresa nuam, la bolsa: registra la calificación de los dividendos del ejercicio 2024, con sus factores, la trazabilidad y el respaldo. Ya está publicada en la nube, así que la abro directo."

**Ver:** la pantalla de login (título "Calificaciones Tributarias") y, al entrar, la grilla (todavía vacía: los certificados se cargan en la toma 4).

## Toma 2 — La grilla y sus filtros

**Hacer (clic por clic):**
1. Pasar el mouse por la tabla, sin apretar nada.
2. Señalar con el mouse los filtros de arriba (**Mercado**, **Origen**, **Período**) y los botones **Buscar** y **Limpiar**.
3. Señalar la barra de botones: **Ingresar**, **Carga de calificaciones** y **Exportar**.

**Decir:** "La grilla lista los certificados del período y parte vacía: los cargo en un momento. Arriba se filtra por mercado, origen y período comercial."

**Ver:** el mensaje "Sin calificaciones. Usa «Ingresar» o carga un CSV." y todos los botones descritos. Con datos, cada fila muestra **Ver**, **Modificar** y **Eliminar**.

## Toma 3 — Llega el archivo y el sistema lo revisa antes de grabar

**Hacer (clic por clic):**
1. Clic en el botón **Carga de calificaciones** (barra superior).
2. Dejar **Tipo de carga** en `Montos (DJ 1948)`.
3. Clic en el botón del cuadro **Archivo** (el que abre el explorador, tipo "Seleccionar archivo") y elegir `carga-montos-demo-error.csv` de la carpeta `demo`.
4. Mirar la vista previa: "3 registros detectados · 20 columnas · 3 avisos de formato" y la lista de avisos (fecha inválida, una fila con columnas de menos, tipo de sociedad inválido).
5. Clic en **Cancelar**.

**Decir:** "Este archivo tiene errores a propósito, para mostrar la validación. Antes de grabar, el sistema lo previsualiza: dice cuántos registros trae y qué línea está mal."

**Ver:** la vista previa con las primeras 5 filas, el contador de registros y los avisos. Nada se grabó.

## Toma 4 — Cargar el lote de certificados

**Hacer (clic por clic):**
1. Clic en **Carga de calificaciones**.
2. Dejar **Tipo de carga** en `Montos (DJ 1948)`.
3. Clic en el cuadro **Archivo** y elegir `carga-montos-demo.csv`.
4. Verificar la vista previa: "3 registros detectados · sin problemas de formato".
5. Clic en **Confirmar carga (3)**.
6. Esperar: aparece el aviso "Carga OK: 3 insertados" y la grilla se refresca sola con los 3 registros.

**Decir:** "Ahora el mismo formato con datos válidos: tres certificados identificados por llave, así la carga actualiza en vez de duplicar."

**Ver:** el mensaje "Carga OK: 3 insertados, 0 actualizados" y las filas `CENCOSUD S.A.`, `ENEL AMERICAS S.A.` y `FONDO MUTUO LARRAIN VIAL` en la grilla.

## Toma 5 — Filtrar por mercado

**Hacer (clic por clic):**
1. Clic en la lista **Mercado** (filtro de arriba) y elegir `ACN`.
2. Clic en **Buscar**.

**Decir:** "Filtro por mercado: quedan solo los dos certificados de acciones que acabo de cargar."

**Ver:** la tabla con 2 filas: `CENCOSUD S.A.` y `ENEL AMERICAS S.A.`

## Toma 6 — Ver el cálculo que hace el sistema

**Hacer (clic por clic):**
1. En la fila de `ENEL AMERICAS S.A.`, clic en **Ver** (primer botón de la fila).
2. En la ventana de detalle, clic en **Calcular factores** (abajo a la derecha).
3. Mirar la columna **8** → `M: 200.000` / `F: 0.625`; y la columna **12** → `M: 120.000` / `F: 0.375`.
4. Clic en **Cerrar**.

**Decir:** "El sistema divide cada monto por la base 8 a 19: 0,625 y 0,375. Así se reparte la base del dividendo."

**Ver:** en el detalle, monto y factor por columna (el factor se muestra con punto decimal), y el mensaje "Factores recalculados".

## Toma 7 — Corregir un error de tipeo

**Hacer (clic por clic):**
1. En la fila de `ENEL AMERICAS S.A.`, clic en **Modificar** (segundo botón de la fila).
2. Clic en la pestaña **Factores**.
3. Clic en el campo que empieza con **8** (el primero de la lista), borrar y escribir `0.7`.
4. Ver el recuadro de suma en rojo: "1.07500000 ¡supera 1!".
5. Corregir: en ese mismo campo escribir `0.625` → el recuadro vuelve a "1.00000000 (≤ 1 ✓)".
6. Clic en **Cancelar** (no se guarda nada).

**Decir:** "Si me equivoco, la suma se calcula en vivo y me avisa antes de grabar."

**Ver:** el recuadro de suma que cambia de rojo (¡supera 1!) a normal (≤ 1 ✓).

## Toma 8 — Registrar a mano un certificado que no vino en el lote

**Hacer (clic por clic):**
1. Clic en **Ingresar** (barra superior).
2. En la pestaña **Datos básicos**, completar campo por campo (clic en cada uno para escribirlo):

| Campo | Qué escribir / elegir |
|---|---|
| Mercado | elegir `CFI` en la lista |
| Instrumento | `AGUAS ANDINAS S.A.` |
| Ejercicio | `2024` (borrar el año que trae por defecto) |
| Fecha de pago | `2024-08-12` |
| Secuencia | `1` |
| N° de dividendo | `1450` |
| Tipo de sociedad | elegir `Abierta (A)` |
| Valor histórico | `300000` |
| Origen | dejar `corredor` · ISFUT: sin marcar |

3. Clic en la pestaña **Montos**.
4. En el campo que empieza con **8** escribir `150000`; en el campo que empieza con **12** escribir `50000`. Todo lo demás queda en 0.
5. Clic en **Guardar**. La ventana se cierra sola.
6. En la grilla, clic en **Limpiar** (queda filtrada por ACN de la toma 5) y ver los 4 registros.

**Decir:** "Cuando llega un certificado suelto, lo ingreso a mano. Los montos van agrupados por concepto de la homologación del SII."

**Ver:** el mensaje "Calificación creada"; tras **Limpiar**, `AGUAS ANDINAS S.A.` junto a los otros tres.

## Toma 9 — Auditoría

**Hacer (clic por clic):**
1. Clic en la pestaña **Auditoría** (arriba, junto a Calificaciones).

**Decir:** "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora, y además se replica en la base de datos en la nube."

**Ver:** la tabla con el registro del ingreso recién hecho (acción INSERT) y el usuario `admin`.

## Toma 10 — Exportar el respaldo

**Hacer (clic por clic):**
1. Clic en **Exportar** (barra superior).
2. Clic en **JSON**.
3. Ver el mensaje con el nombre del archivo y el bucket; la descarga se abre en una pestaña nueva con la URL firmada.
4. Clic en **Cerrar**.

**Decir:** "El respaldo se publica en S3 y el sistema devuelve una URL firmada que dura una hora, para compartirlo sin dar acceso al bucket."

**Ver:** el modal con `factoruno-...json`, el bucket y la descarga.

## Toma 11 — Cierre en el teléfono

**Hacer (clic por clic):**
1. Clic en **Salir** (arriba a la derecha, junto al nombre de usuario).
2. Entrar con `analista` / `Analista1234!`.
3. Achicar la ventana del navegador hasta unos 390 px de ancho (o abrir la misma dirección en el teléfono).

**Decir:** "La misma aplicación en pantalla chica: la grilla se convierte en tarjetas y el formulario se apila en una columna. Con esto cierro la demo; el repositorio, el informe y la solución en la nube están en el documento de entrega."

**Ver:** la grilla como tarjetas (etiqueta a la izquierda, valor a la derecha) y el formulario de ingreso en una sola columna.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El paso 8 guarda pero la grilla no muestra el registro | Clic en **Limpiar** o **Buscar** para refrescar la lista. |
| La toma 4 dice "0 insertados, 3 actualizados" | Ya cargaste el lote antes: la carga actualiza por llave. Sirve igual para la demo. |
| La toma 5 muestra menos filas de las esperadas | El lote ya no está completo: volver a cargar `carga-montos-demo.csv`. |
| La toma 8 dice que actualizó en vez de insertar | Ese certificado ya existía: cambiar el N° de dividendo a `1451`. |
| **Exportar** muestra error | La nube no está configurada en ese entorno. En el servidor de la demo sí funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP. Revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` con `Analista1234!` y seguir. |
| No encuentro los CSV en el explorador de archivos | Están en la carpeta `demo/` del proyecto (`proyectos/factoruno/demo/`) y en la carpeta `demo` de esta guía en Obsidian. |

## Después de grabar

1. Subir el video (Drive o YouTube no listado) y pegar el enlace en el documento de entrega, en la línea del video.
2. Avisar para dejar la grilla con datos de ejemplo y el laboratorio encendido el día de la entrega.

## Anexo — Cómo se usa la app (referencia rápida)

**Entrar:** `http://100.57.30.193/`. Usuarios: `admin` y `analista` (ven y editan todo) · `consulta` (solo ve).

**Grilla y filtros:** filtros por **Mercado** (ACN/CFI/FM), **Origen** (corredor/entidad) y **Período** (año) + botones **Buscar** y **Limpiar**. Cada fila tiene **Ver**, **Modificar** y **Eliminar** (modificar y eliminar solo admin/analista).

**Ingresar un certificado:** botón **Ingresar** → pestañas **Datos básicos** → **Montos** → **Factores** → **Guardar**. Si cargas montos, los factores se calculan solos al guardar.

**Ver el detalle:** **Ver** → muestra monto y factor por columna y el botón **Calcular factores** (deja el cálculo guardado).

**Factores a mano:** pestaña **Factores** con la suma de la base 8–19 en vivo; si supera 1, avisa en rojo.

**Cargar un CSV:** botón **Carga de calificaciones** → tipo de carga → archivo → vista previa con avisos → **Confirmar carga (N)**. La carga actualiza por llave (ejercicio + mercado + instrumento + fecha + secuencia + dividendo + tipo de sociedad), no duplica.

**Auditoría:** pestaña **Auditoría** — cada cambio con usuario, fecha y hora; además se replica en la base de datos en la nube (DynamoDB).

**Exportar:** botón **Exportar** → **JSON** o **CSV** → se publica en el bucket S3 y devuelve una URL firmada válida por 1 hora.

**Móvil:** con la ventana bajo 560 px, la grilla pasa a tarjetas y el formulario a una sola columna.

**Reglas fijas:** fecha AAAA-MM-DD · mercado ACN/CFI/FM · sociedad A/C · origen corredor/entidad · suma de la base 8–19 ≤ 1 · montos en columnas 8–37 agrupados por concepto del SII · solo admin y analista editan.

## No hace falta mostrar

- El código, los tests o los diagramas: eso se evalúa en el informe.
- No leer el informe en cámara ni pasar diapositivas.
- No explicar el modelo de datos: se ve en la grilla y en el detalle.
