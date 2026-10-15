Esta página explica, en simple, **qué significa cada campo** del formulario de FactorUno: de dónde sale, qué información va y cómo se calculan los factores.

**Cómo leerla:** en el formulario, cada nombre de campo tiene un botón **?** al lado que abre esta página directo en la explicación de ese campo.

## Cómo se calculan los factores {#calculo}

El certificado del SII (DJ 1948) desglosa cada dividendo en **30 columnas**, numeradas de la **8** a la **37**. Cada columna es un tipo de renta distinto:

- **Monto:** cuánto del dividendo corresponde a esa columna (en pesos).
- **Factor:** qué proporción del total representa esa columna. Se calcula solo:

> **factor = monto de la columna ÷ suma de los montos de las columnas 8 a 19**

La suma de las columnas 8 a 19 es la **base** (representa el 100 %). El factor se redondea a 8 decimales y siempre debe ser **menor o igual a 1 (≤ 1)**. Si la suma de los factores 8 a 19 **supera 1**, los montos no cuadran: el sistema lo avisa con «¡supera 1!».

Cada columna pertenece a un **grupo** (el texto de abajo aparece bajo cada nombre en el formulario). Por ejemplo, las columnas 8 a 11 comparten el grupo «Afectos a impuestos globales y/o adicional (IDPC)»: son rentas del mismo tipo de impuesto. **Con derecho / sin derecho** significa si la renta tiene o no derecho a usar el crédito por el impuesto ya pagado.

## Los datos básicos {#datos-basicos}

### Ejercicio {#ejercicio}

El **año comercial** (tributario) al que pertenece el dividendo. No es lo mismo que la fecha de pago: un dividendo pagado en 2024 puede pertenecer al ejercicio 2023 o 2024, según lo indique el certificado.

**Qué escribir:** el año que trae el certificado (por ejemplo, `2024`).

### Mercado {#mercado}

De dónde viene el instrumento:

- **ACN** — acciones (empresas que cotizan en bolsa).
- **CFI** — cuotas de fondos de inversión.
- **FM** — fondos mutuos.

**Qué elegir:** el mercado que indique el certificado.

### Instrumento {#instrumento}

El **nombre del emisor** que pagó el dividendo (la empresa o el fondo).

**Qué escribir:** el nombre tal como aparece en el certificado (por ejemplo, `ENEL AMERICAS S.A.`).

### Fecha pago {#fecha-pago}

El día en que el dividendo **se pagó**.

**Qué escribir:** en formato `AAAA-MM-DD` (por ejemplo, `2024-05-06`). En la carga masiva, cualquier otro formato se marca como error.

### Secuencia evento {#secuencia}

El **número de orden del pago** dentro del mismo instrumento y ejercicio: si el mismo emisor pagó dos dividendos en el año, cada uno tiene su secuencia (1, 2, …).

**Qué escribir:** el número que trae el certificado.

### N° dividendo {#numero-dividendo}

El **número identificador del dividendo** que trae el certificado. Junto con el instrumento, el ejercicio y la secuencia, distingue este pago de cualquier otro.

**Qué escribir:** el número del certificado.

### Tipo sociedad {#tipo-sociedad}

- **Abierta (A)** — sociedad anónima abierta (cotiza en bolsa).
- **Cerrada (C)** — sociedad anónima cerrada.

**Qué elegir:** el tipo que indique el certificado.

### Valor histórico {#valor-historico}

El **valor de la acción o cuota al momento del dividendo** que trae el certificado.

**Qué escribir:** el valor histórico del certificado; si no lo trae, se puede dejar en `0`.

### Origen {#origen}

El **canal por el que llegó la información**: `corredor` (corredor de bolsa) o `entidad` (banco u otra institución).

**Qué elegir:** en el uso normal del mantenedor, `corredor`.

### ISFUT {#isfut}

Casilla del **impuesto sustitutivo al FUT** (Ley 20.780). Se **marca** solo si el certificado indica que el pago está acogido a ese régimen; si no, se deja sin marcar.

## Montos y factores: las columnas 8 a 37 {#montos}

**Montos:** se copian del certificado columna por columna. Si el certificado no trae una columna (porque ese tipo de renta no aplica a ese dividendo), se deja **vacía** (el sistema la guarda como 0).

**Factores:** se calculan solos con el botón **Calcular factores** (está en el detalle del registro). También se pueden editar a mano en la pestaña **Factores**, por ejemplo si el certificado ya los trae calculados.

### Columna 8 — Con crédito IDPC (gen. 01.01.2017) {#c8}

Dividendos con crédito por **IDPC** (Impuesto de Primera Categoría: el impuesto a la renta que pagan las empresas) por utilidades generadas **a contar del 01.01.2017**.

### Columna 9 — Con crédito IDPC (acum. 31.12.2016) {#c9}

Lo mismo que la columna 8, pero por utilidades **acumuladas hasta el 31.12.2016** (régimen anterior a la reforma tributaria).

### Columna 10 — Con derecho crédito pago IDPC voluntario {#c10}

Rentas con derecho al crédito por el **pago voluntario del IDPC**.

### Columna 11 — Sin derecho a crédito {#c11}

Rentas afectas a impuestos, pero **sin derecho a crédito**.

### Columna 12 — RAP y Dif. Inicial (ex Art. 14 TER A) {#c12}

Rentas del registro **RAP** (Rentas Afectas a los Propietarios) y la **Diferencia Inicial** de sociedades que venían del ex Art. 14 TER A de la Ley de la Renta.

### Columna 13 — Otras rentas percibidas sin prioridad {#c13}

**Otras rentas percibidas** que no tienen prioridad en su orden de imputación.

### Columna 14 — Exceso Distribuciones Desproporcionadas (N°9 Art. 14 A) {#c14}

Montos del **exceso de distribuciones desproporcionadas** (N° 9 del Art. 14 A de la Ley de la Renta).

### Columna 15 — ISFUT Ley N°20.780 {#c15}

Utilidades afectadas con el **ISFUT** (impuesto sustitutivo al FUT) de la Ley 20.780.

### Columna 16 — Rentas hasta 31.12.1983 / ISFUT Ley N°21.210 {#c16}

Rentas generadas **hasta el 31.12.1983** y/o rentas del **ISFUT** de la Ley 21.210.

### Columna 17 — Rentas exentas IGC (Art.11 L.18.401) afectas a IA {#c17}

Rentas **exentas del IGC** (Impuesto Global Complementario: el impuesto personal de las personas) que sí están afectas al **IA** (Impuesto Adicional).

### Columna 18 — Rentas exentas IGC y/o IA {#c18}

Rentas exentas del **IGC y/o del IA**.

### Columna 19 — Ingresos No Constitutivos de Renta {#c19}

Ingresos que **no constituyen renta**: no se gravan; se informan aparte.

### Columna 20 — No sujetos restitución hasta 31.12.2019 sin derecho {#c20}

Rentas **no sujetas a restitución** (tramo hasta el 31.12.2019), **sin derecho** a crédito.

### Columna 21 — No sujetos restitución hasta 31.12.2019 con derecho {#c21}

Igual que la columna 20, pero **con derecho** a crédito.

### Columna 22 — No sujetos restitución desde 01.01.2020 sin derecho {#c22}

Rentas no sujetas a restitución **desde el 01.01.2020**, **sin derecho** a crédito.

### Columna 23 — No sujetos restitución desde 01.01.2020 con derecho {#c23}

Igual que la columna 22, pero **con derecho** a crédito.

### Columna 24 — Sujetos a restitución sin derecho {#c24}

Rentas **sujetas a restitución**, **sin derecho** a crédito.

### Columna 25 — Sujetos a restitución con derecho {#c25}

Rentas sujetas a restitución, **con derecho** a crédito.

### Columna 26 — Sujetos a restitución sin derecho (2) {#c26}

Segundo grupo de rentas sujetas a restitución, **sin derecho** (el certificado separa estos montos igual que en las columnas 24 y 25).

### Columna 27 — Sujetos a restitución con derecho (2) {#c27}

Segundo grupo, **con derecho** a crédito.

### Columna 28 — Crédito por IPE {#c28}

**Crédito por IPE** (así lo rotula el certificado): un crédito de impuesto asociado a las rentas del dividendo.

### Columna 29 — Asociados a Rentas Afectas, sin derecho {#c29}

Montos **asociados a rentas afectas** (acumulados hasta el 31.12.2016), **sin derecho** a crédito.

### Columna 30 — Asociados a Rentas Afectas, con derecho {#c30}

Igual que la columna 29, pero **con derecho** a crédito.

### Columna 31 — Asociados a Rentas Exentas (Art.11 L.18.401), sin derecho {#c31}

Montos **asociados a rentas exentas** (Art. 11, Ley 18.401), **sin derecho** a crédito.

### Columna 32 — Asociados a Rentas Exentas (Art.11 L.18.401), con derecho {#c32}

Igual que la columna 31, pero **con derecho** a crédito.

### Columna 33 — Crédito por IPE (acumulados 31.12.2016) {#c33}

Crédito por IPE **acumulado hasta el 31.12.2016**.

### Columna 34 — Crédito impuesto tasa adicional ex Art.21 LIR, sin derecho {#c34}

Crédito por el **impuesto de tasa adicional** del Art. 21 de la Ley de la Renta (el impuesto a los gastos rechazados), **sin derecho**.

### Columna 35 — Crédito impuesto tasa adicional ex Art.21 LIR, con derecho {#c35}

Igual que la columna 34, pero **con derecho**.

### Columna 36 — Tasa efectiva crédito FUT (TEF) {#c36}

**Tasa efectiva del crédito FUT (TEF).** No es un monto en pesos: es una tasa que trae el certificado.

### Columna 37 — Tasa efectiva crédito FUT (TEX) {#c37}

**Tasa efectiva del crédito FUT (TEX).** Segunda tasa del certificado, igual que la columna 36.

## El resto de la aplicación {#resto}

- **Carga masiva (CSV):** sube varios certificados de una vez. Antes de grabar, el sistema **previsualiza** el archivo y avisa los errores de formato por línea (fecha, cantidad de columnas, tipo de sociedad). Cada fila se identifica por su **llave** (ejercicio + mercado + instrumento + fecha + secuencia + N° dividendo + tipo sociedad): si ya existe, se **actualiza**; si no, se **inserta**.
- **Auditoría:** registra cada cambio (INSERT, UPDATE, DELETE) con fecha, usuario y detalle, y se espeja en la nube (DynamoDB) para trazabilidad.
- **Exportar:** genera un respaldo JSON o CSV y lo publica en la nube (S3); devuelve una **URL firmada** que dura 1 hora para compartirlo sin dar acceso al bucket.
- **Usuarios:** `admin` y `analista` pueden ingresar y modificar; `consulta` solo puede ver.
