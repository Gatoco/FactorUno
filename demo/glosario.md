# FactorUno — glosario: las palabras de la guía y de la pantalla, en simple

> Cuando en la guía o en la aplicación aparezca una palabra que no entiendas, búscala acá. Todo está explicado como para alguien que nunca vio contabilidad ni informática.

## 1. Tu duda: ¿por qué «Ejercicio» muestra un año?

**Ejercicio = el año.**

- Cuando el formulario muestra **Ejercicio: 2024**, significa "el año 2024": los dividendos que se pagaron durante ese año.
- "Ejercicio" es la palabra que se usa en contabilidad y en impuestos para nombrar el período de un año de actividad ("el cierre del ejercicio 2024" = el cierre del año 2024). No es ejercicio físico ni de práctica.
- Cada dividendo pertenece a un año (a un ejercicio). Por eso el campo **Ejercicio** y el filtro **Período** siempre hablan de años.

En palabras simples: si ves un año junto a "Ejercicio", es porque ahí va **el año al que pertenecen esos dividendos**.

## 2. El caso y los documentos

| Palabra | Qué significa, en simple |
|---|---|
| **nuam** | La empresa de la bolsa para la que está pensada la aplicación (la empresa que pidió el sistema). FactorUno se desarrolló para su caso. |
| **HDU** | "Historia de Usuario": el documento con los requisitos que entregó nuam. Es el material del ramo y funciona como la especificación: dice qué tiene que hacer el sistema. |
| **Dividendo** | La parte de las utilidades de una empresa que se reparte entre sus dueños (accionistas). |
| **Calificación tributaria** | La ficha que descompone un dividendo según cómo se grava: qué parte de la plata corresponde a cada tipo de renta y a cada crédito. Es lo que la aplicación guarda. |
| **Mantenedor** | Programa para mantener datos: crear, buscar, modificar, eliminar y cargar en masa. |
| **SII** | Servicio de Impuestos Internos: la entidad de impuestos de Chile. |
| **DJ** | "Declaración jurada": un formulario de declaración que se presenta al SII. |
| **DJ 1948** | La declaración jurada 1948: donde las empresas informan los **montos** de los dividendos repartidos. Es el formato del archivo que se carga en las tomas 3 y 4 ("Montos (DJ 1948)"). |
| **Certificado** | El documento con el detalle de los dividendos. En la demo se llama "certificados" a las filas que se registran. |
| **Período comercial** | El año que se está consultando: el mismo concepto que Ejercicio. Es lo que usa el filtro **Período**. |

## 3. Los campos del formulario

| Campo | Qué significa, en simple |
|---|---|
| **Ejercicio** | El año de los dividendos (ver sección 1). El formulario trae el año actual por defecto; en la demo se escribe 2024. |
| **Mercado** | De dónde viene el instrumento. Tres opciones: **ACN** = acciones · **CFI** = cuotas de fondos de inversión · **FM** = fondos mutuos. Se elige de la lista. |
| **Instrumento** | Quién pagó el dividendo: una empresa (ej: CENCOSUD S.A.) o un fondo (ej: Fondo Mutuo Larrain Vial). Se escribe tal como aparece en el certificado. |
| **Fecha de pago** | El día en que se pagó el dividendo, en formato AAAA-MM-DD (2024-05-09 = 9 de mayo de 2024). |
| **Secuencia** | El número de orden del pago: si es el primer dividendo del año, 1; el segundo, 2… Viene en el certificado. |
| **N° de dividendo** | El número del dividendo que trae el certificado (ej: 880, 1450). Se copia tal cual. |
| **Tipo de sociedad** | **A** = sociedad anónima abierta (cotiza en bolsa, como CENCOSUD) · **C** = cerrada (no cotiza). Viene en el certificado. |
| **Valor histórico** | El monto del dividendo según el certificado (en pesos), tal como quedó registrado originalmente. |
| **Origen** | Quién ingresó la información: **corredor** (corredor de bolsa) o **entidad** (entidad prestadora del servicio). Para la demo se deja "corredor". |
| **ISFUT** | Casilla de un impuesto especial (Impuesto Sustitutivo al FUT, Ley 20.780). Se marca solo si el dividendo viene acogido a ese impuesto; en la demo va sin marcar. |

## 4. Los números: montos, base y factores

| Palabra | Qué significa, en simple |
|---|---|
| **Montos (columnas 8 a 37)** | El certificado no trae "un total": reparte el dividendo en casillas numeradas de la 8 a la 37, según el tipo de renta. Cada casilla (columna) es un concepto distinto. En la pestaña **Montos**, cada campo es una casilla y muestra debajo a qué concepto pertenece. |
| **Homologación** | Hacer equivaler dos listas. Acá: la equivalencia entre los nombres del SII y el número de columna que usa la aplicación. Ej: columna 8 = "Con crédito IDPC (generado desde 01.01.2017)". |
| **Base (suma 8 a 19)** | La suma de los montos de las columnas 8 a 19: es el total sobre el que se calculan los porcentajes. Ej. de la demo: 200.000 + 120.000 = 320.000. |
| **Factor** | El monto de una columna dividido por la base: qué parte (qué porcentaje) del total le toca a esa columna. Ej: 200.000 ÷ 320.000 = **0.625** (el 62,5%). |
| **Calcular factores** | El botón que hace esa división y guarda el resultado. |
| **Regla ≤ 1** | "≤" se lee "menor o igual que". La suma de los factores de las columnas 8 a 19 no puede pasar de 1. La aplicación la calcula en vivo y avisa en rojo ("¡supera 1!") si te pasaste. |
| **Decimales** | Los factores se guardan con 8 decimales (0.62500000) para que la división sea exacta. La aplicación los muestra con punto (0.625); se lee igual: 0,625. |
| **M: y F:** | En la ventana de detalle, **M:** es el monto de esa columna y **F:** su factor. |

## 5. Las palabras tributarias de las columnas

Cada grupo de columnas tiene un nombre del SII. Traducidos a simple (son los textos que se ven bajo cada campo):

| Grupo | Nombre del SII | En simple |
|---|---|---|
| Columnas 8–11 | Afectos a impuestos globales y/o adicional (IDPC) | Plata por la que la empresa ya pagó su impuesto (**IDPC** = Impuesto de Primera Categoría, el impuesto a las utilidades). Da **crédito**: un descuento de impuesto para quien recibe el dividendo. |
| Columnas 12–16 | Rentas con tributación cumplida (RAP, ISFUT) | Plata que ya cumplió sus impuestos por otro sistema. **RAP** = el registro donde se anotan las rentas afectas; **ISFUT** = el impuesto sustitutivo (ver arriba). |
| Columnas 17–18 | Rentas exentas de IGC | Renta que **no paga** el impuesto personal. **IGC** = Impuesto Global Complementario, el impuesto a las rentas de las personas en Chile. |
| Columna 19 | Ingresos no constitutivos de renta | Plata que **no se considera renta** (por ejemplo, devolución de capital): no tributa. |
| Columnas 20–23 | No sujetos a restitución | Clasificación del crédito: **no** hay que devolverlo. Las fechas (hasta 31.12.2019 / desde 01.01.2020) indican a qué período corresponde la clasificación. |
| Columnas 24–27 | Sujetos a restitución | Clasificación del crédito: **podría** tener que devolverse. "Con derecho" / "sin derecho" = si genera devolución de impuesto o no. |
| Columna 28 y 33 | Crédito por IPE | **IPE** = Impuesto por Pago de Excedentes; acá va su crédito (la columna 33, para los acumulados hasta 2016). |
| Columnas 29–32 | Acumulados hasta 31.12.2016 | Rentas del sistema antiguo (anteriores a 2017): las afectas y las exentas, con o sin derecho. |
| Columnas 34–35 | Crédito impuesto tasa adicional (Art. 21 LIR) | Crédito del impuesto "tasa adicional" del **artículo 21** de la Ley de Impuesto a la Renta (grava los gastos que la empresa no puede descontar). |
| Columnas 36–37 | Tasa efectiva del crédito FUT (TEF/TEX) | **FUT** = Fondo de Utilidades Tributables (sistema antiguo de registros). **TEF** y **TEX** son tasas (%) ya calculadas que trae el certificado: se copian tal cual. |
| — | **IA** (Impuesto Adicional) | El impuesto que pagan quienes no pagan el IGC (típicamente inversionistas extranjeros). Aparece en el nombre de algunas columnas. |
| — | Números de leyes (20.780, 21.210, 18.401, 14…) | No hay que entenderlas: el certificado trae la columna con su nombre y la aplicación te muestra a cuál corresponde. |

## 6. La aplicación y la nube

| Palabra | Qué significa, en simple |
|---|---|
| **Grilla** | La tabla principal donde se listan las calificaciones registradas. |
| **Filtros · Buscar · Limpiar** | Se elige Mercado, Origen y Período, y se aprieta **Buscar** para ver solo lo que coincide. **Limpiar** borra los filtros y muestra todo de nuevo. |
| **Ver / Modificar / Eliminar** | Botones de cada fila: **Ver** abre el detalle (sin editar), **Modificar** abre para editar y **Eliminar** borra el registro. |
| **Ingresar** | Botón para crear una calificación a mano. |
| **Carga de calificaciones** | Botón para subir un archivo con muchos registros de una vez. |
| **Vista previa** | Antes de grabar, la aplicación muestra qué va a hacer: cuántos registros trae el archivo y qué líneas están mal. Nada se graba hasta confirmar. |
| **CSV** | Un archivo de datos en formato de tabla simple, que se puede abrir hasta en Excel. |
| **Llave** | La combinación de datos que identifica un registro (ejercicio + mercado + instrumento + fecha + secuencia + n° de dividendo + tipo de sociedad). Si una carga trae una llave que ya existe, **actualiza** en vez de duplicar. Por eso "0 insertados, 3 actualizados" es normal cuando el lote ya estaba cargado. |
| **Insertado / actualizado** | Insertado = se agregó un registro nuevo. Actualizado = se reemplazó uno que ya existía. |
| **Auditoría** | La pestaña donde queda el registro de cada cambio: quién, qué y cuándo. |
| **Trazabilidad** | Poder reconstruir qué pasó con cada dato (quién lo ingresó, cuándo, qué cambió). Eso lo entrega la auditoría. |
| **INSERT / UPDATE / DELETE** | Las etiquetas de la auditoría: INSERT = se creó, UPDATE = se modificó, DELETE = se eliminó. |
| **Espejo / réplica (DynamoDB)** | La auditoría, además de quedar en el servidor, se copia a una base de datos en la nube (**DynamoDB**) como respaldo. |
| **Exportar / respaldo** | Sacar una copia de los datos en un archivo (**JSON** o **CSV**) y publicarla en la nube. |
| **JSON** | Un formato de archivo ordenado, pensado para que lo lean otros programas. |
| **S3 / bucket** | **S3** es el servicio de archivos de AWS. Un **bucket** es como el cajón donde se guardan: el respaldo queda ahí. |
| **URL firmada** | Un enlace temporal con permiso incluido: lo abre cualquiera (sin cuenta) pero **expira en 1 hora**. |
| **Nube / servidor** | La aplicación no está en tu computador: corre en un servidor de AWS, y por eso se abre desde cualquier parte con la dirección `http://100.57.30.193/`. |
| **EC2 / IP elástica** | **EC2** = el servidor de AWS. **IP elástica** = su dirección fija, que no cambia aunque el servidor se reinicie. |
| **Laboratorio** | La cuenta de AWS que entrega el ramo (AWS Academy). Se enciende por sesiones (de unas 4 horas); si está apagado, la página no responde. |
| **Roles (admin / analista / consulta)** | Quién puede hacer qué: **admin** y **analista** ven y editan todo; **consulta** solo puede mirar. |
| **Tarjetas (móvil)** | Cuando la ventana del navegador es angosta (menos de 560 píxeles), la tabla se convierte en tarjetas: una por registro, con el nombre del dato a la izquierda y el valor a la derecha, para leer en el teléfono. |
