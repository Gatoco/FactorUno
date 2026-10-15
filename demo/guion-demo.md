**Video:** 5–7 minutos · **Caso:** cierre de dividendos del ejercicio 2024 (HDU real de nuam, usado como caso del ramo).
**Quién habla:** el autor del desarrollo, en primera persona. No se actúa como funcionario de nuam: se muestra la aplicación y se explica lo que hace.
**Regla del profesor:** mostrar la aplicación, no disertar. Frases de 5–10 segundos.
**Cómo leer este documento:** una toma por página. Cada página dice qué hacer, qué escribir, qué decir y qué debe verse. No hay que buscar nada en otras páginas.

## Antes de grabar

- [ ] Abrir `http://100.57.30.193/`. Si no carga, el laboratorio está apagado: avisar y esperar.
- [ ] Usuario `admin` / `Admin1234!` (tomas 1 a 10). Solo la toma 11 usa `analista` / `Analista1234!`.
- [ ] Tener a mano los dos archivos: `carga-montos-demo-error.csv` y `carga-montos-demo.csv`.
- [ ] Cerrar notificaciones y pestañas. Grabar en 1080p con la cámara a la vista.
- [ ] Si algo se traba: se corta y se repite esa toma.

<div style="page-break-after: always;"></div>

## Los conceptos, en una línea cada uno

Esta página es solo para preparar la grabación: no se lee en cámara.

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

<div style="page-break-after: always;"></div>

## Toma 1 — Entrar al sistema

**Hacer:** abrir `http://100.57.30.193/`, usuario `admin`, contraseña `Admin1234!`.

**Decir:** "Esta es la aplicación que desarrollé para el caso de FactorUno, que sale del HDU de nuam: registrar la calificación de los dividendos del ejercicio 2024, con sus factores, la trazabilidad y el respaldo. Ya está publicada en la nube, así que la abro directo."

**Ver:** la pantalla de login y, al entrar, la grilla (todavía vacía: los certificados se cargan en la toma 4).

<div style="page-break-after: always;"></div>

## Toma 2 — La grilla y sus filtros

**Hacer:** pasar el mouse por la tabla y por los filtros, sin apretar nada.

**Decir:** "La grilla lista los certificados del período y parte vacía: los cargo en un momento. Arriba se filtra por mercado, origen y período comercial."

**Ver:** el mensaje "Sin calificaciones. Usa «Ingresar» o carga un CSV."; los filtros con **Buscar** y **Limpiar**; y la barra con **Ingresar**, **Carga de calificaciones** y **Exportar**. Con datos, cada fila muestra **Ver**, **Modificar** y **Eliminar**.

<div style="page-break-after: always;"></div>

## Toma 3 — Llega el archivo y el sistema lo revisa antes de grabar

**Hacer:** botón **Carga de calificaciones** → Tipo de carga `Montos (DJ 1948)` → Archivo → elegir `carga-montos-demo-error.csv`.

**Decir:** "Este archivo tiene errores a propósito, para mostrar la validación. Antes de grabar, el sistema lo previsualiza: dice cuántos registros trae y qué línea está mal."

**Ver:** la vista previa con 3 registros y la lista de avisos (fecha inválida, una fila con columnas de menos, tipo de sociedad inválido). Apretar **Cancelar**.

<div style="page-break-after: always;"></div>

## Toma 4 — Cargar el lote de certificados

**Hacer:** botón **Carga de calificaciones** → Tipo de carga `Montos (DJ 1948)` → Archivo → elegir `carga-montos-demo.csv` → botón **Confirmar carga (3)**.

**Decir:** "Ahora el mismo formato con datos válidos: tres certificados identificados por llave, así la carga actualiza en vez de duplicar."

**Ver:** el mensaje "Carga OK: 3 insertados" y los 3 registros en la grilla.

<div style="page-break-after: always;"></div>

## Toma 5 — Filtrar por mercado

**Hacer:** en **Mercado** elegir `ACN` y apretar **Buscar**.

**Decir:** "Filtro por mercado: quedan solo los dos certificados de acciones que acabo de cargar."

**Ver:** la tabla con 2 filas: `CENCOSUD S.A.` y `ENEL AMERICAS S.A.`.

<div style="page-break-after: always;"></div>

## Toma 6 — Ver el cálculo que hace el sistema

**Hacer:** abrir el registro `ENEL AMERICAS S.A.` → botón **Detalle** → botón **Calcular factores**.

**Decir:** "El sistema divide cada monto por la base 8 a 19: 0,625 y 0,375. Así se reparte la base del dividendo."

**Ver:** en el detalle, monto y factor por columna: columna 8 → `200.000` / `0.625` y columna 12 → `120.000` / `0.375` (el factor se muestra con punto decimal).

<div style="page-break-after: always;"></div>

## Toma 7 — Corregir un error de tipeo

**Hacer:** abrir el registro `ENEL AMERICAS S.A.` en edición → pestaña **Factores** → en la columna 8 escribir `0.7` → después corregirlo a `0.625`.

**Decir:** "Si me equivoco, la suma se calcula en vivo y me avisa antes de grabar."

**Ver:** el recuadro de suma en rojo con "¡supera 1!"; al corregirlo, vuelve a 1 con "(≤ 1 ✓)". Cerrar con **Cancelar**.

<div style="page-break-after: always;"></div>

## Toma 8 — Registrar a mano un certificado que no vino en el lote

**Hacer:** botón **Ingresar** → pestaña **Datos básicos**.

**Escribir (Datos básicos):**
Ejercicio `2024` · Mercado `CFI` · Instrumento `AGUAS ANDINAS S.A.` · Fecha de pago `2024-08-12` · Secuencia `1` · N° de dividendo `1450` · Tipo de sociedad `A` · Valor histórico `300000`.

**Hacer:** pestaña **Montos**.

**Escribir (Montos):** columna 8 = `150000` · columna 12 = `50000`. Todo lo demás queda en 0.

**Decir:** "Cuando llega un certificado suelto, lo ingreso a mano. Los montos van agrupados por concepto de la homologación del SII."

**Ver:** el mensaje de guardado; después apretar **Limpiar** para refrescar la lista y ver `AGUAS ANDINAS S.A.` junto a los otros tres.

<div style="page-break-after: always;"></div>

## Toma 9 — Auditoría

**Hacer:** pestaña **Auditoría**.

**Decir:** "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora, y además se replica en la base de datos en la nube."

**Ver:** la tabla con el registro del ingreso recién hecho y el usuario `admin`.

<div style="page-break-after: always;"></div>

## Toma 10 — Exportar el respaldo

**Hacer:** botón **Exportar** → **JSON**.

**Decir:** "El respaldo se publica en S3 y el sistema devuelve una URL firmada que dura una hora, para compartirlo sin dar acceso al bucket."

**Ver:** el modal con el nombre del archivo y el bucket; después la descarga del JSON en una pestaña nueva.

<div style="page-break-after: always;"></div>

## Toma 11 — Cierre en el teléfono

**Hacer:** **Salir** → entrar con `analista` / `Analista1234!` → achicar la ventana hasta unos 390 px de ancho (o abrir la misma dirección en el teléfono).

**Decir:** "La misma aplicación en pantalla chica: la grilla se convierte en tarjetas y el formulario se apila en una columna. Con esto cierro la demo; el repositorio, el informe y la solución en la nube están en el documento de entrega."

**Ver:** la grilla como tarjetas (etiqueta a la izquierda, valor a la derecha) y el formulario de ingreso en una sola columna.

<div style="page-break-after: always;"></div>

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El paso 8 guarda pero la grilla no muestra el registro | Apretar **Limpiar** o **Buscar** para refrescar la lista. |
| La toma 4 dice "0 insertados, 3 actualizados" | Ya cargaste el lote antes: la carga actualiza por llave. Sirve igual para la demo. |
| La toma 5 muestra menos filas de las esperadas | El lote ya no está completo: volver a cargar `carga-montos-demo.csv`. |
| La toma 8 dice que actualizó en vez de insertar | Ese certificado ya existía: cambiar el N° de dividendo a `1451`. |
| **Exportar** muestra error | La nube no está configurada en ese entorno. En el servidor de la demo sí funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP. Revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` con `Analista1234!` y seguir. |

## No hace falta mostrar

- El código, los tests o los diagramas: eso se evalúa en el informe.
- No leer el informe en cámara ni pasar diapositivas.
- No explicar el modelo de datos: se ve en la grilla y en el detalle.
