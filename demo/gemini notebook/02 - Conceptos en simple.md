# Los conceptos, explicados fácil

Todo lo que hay que entender, cada término en dos o tres frases, con los ejemplos de la demo.

## El dividendo y su certificado

- **Dividendo**: la parte de las utilidades de una empresa que se reparte entre sus dueños. La bolsa (nuam) lo procesa y hay que declararlo al SII.
- **Certificado DJ 1948**: el documento donde queda escrito TODO el desglose de un dividendo: cuánto se pagó y en qué conceptos tributarios se reparte. Es la entrada principal de la aplicación.
- **SII**: Servicio de Impuestos Internos de Chile; define las reglas y el formato del certificado.

## Los campos de un registro (una fila de la app)

- **Ejercicio**: el año tributario al que pertenece el dividendo. Ejemplo: `2024`.
- **Mercado**: el tipo de mercado del instrumento (`ACN`, `CFI` o `FM`, según el material de nuam).
- **Instrumento**: quién pagó el dividendo: la empresa o el fondo. Ejemplo: `ENEL AMERICAS S.A.`.
- **Fecha de pago**: cuándo se pagó, en formato `AAAA-MM-DD`. Ejemplo: `2024-05-09`.
- **Secuencia evento**: un número que ordena los hechos del mismo instrumento y fecha. Ejemplo: `2`.
- **N° de dividendo**: el número correlativo del dividendo de esa empresa. Ejemplo: `880`.
- **Tipo de sociedad**: abierta (`A`) o cerrada (`C`). Cambia cómo se tratan los créditos.
- **Valor histórico**: el monto original del dividendo (el total pagado).
- Varios de estos campos juntos identifican el dividendo de forma única: por eso la app no deja duplicados y la carga actualiza en vez de repetir.

## Los montos: las columnas del SII (8 a 37)

- El certificado no trae un solo monto: trae **un monto por concepto**, y cada concepto tiene un **número de columna** fijo (de la 8 a la 37). Es como una planilla con 30 casillas numeradas.
- **Homologación**: la tabla oficial que dice qué significa cada columna. La aplicación muestra cada columna con su grupo, por ejemplo:
  - columnas 8–11: afectos a impuestos globales y/o adicional (IDPC)
  - columnas 12–16: rentas con tributación cumplida
  - columnas 17–18: rentas exentas de IGC
  - columna 19: ingresos no constitutivos de renta
  - y así hasta la 37.
- **Suma base (columnas 8–19)**: se suman los montos de las columnas 8 a 19. Esa suma es la base sobre la que se calculan los factores.
- **Factor**: la fracción del dividendo que corresponde a cada columna. Se calcula así: `factor de la columna = monto de la columna ÷ suma base (8 a 19)`.
  - Ejemplo de la demo (ENEL AMERICAS): columna 8 tiene 200.000 y columna 12 tiene 120.000; la suma base es 320.000.
  - Factor columna 8 = 200.000 ÷ 320.000 = **0.625**. Factor columna 12 = 120.000 ÷ 320.000 = **0.375**.
  - Los factores de las columnas 8 a 19 deberían sumar como máximo **1** (el 100%). La app avisa "¡supera 1!" si te pasas al editarlos a mano.
- **IDPC, IGC**: impuestos de Chile (a las empresas y a las personas) a los que se refieren los conceptos. La app no calcula impuestos: ordena el desglose y los factores.

## Lo que la app deja de registro

- **Auditoría**: el historial de todo lo que pasó: quién insertó, modificó o eliminó un registro y cuándo. Se ve en la pestaña Auditoría.
- **Espejo en DynamoDB**: cada acción de la auditoría se copia además a una base de datos de Amazon (DynamoDB), para que quede respaldo fuera del servidor.
- **Exportación**: la app arma un archivo con todas las calificaciones (JSON o CSV), lo sube a la nube (S3) y devuelve un **enlace firmado** que sirve por 1 hora: con ese enlace se descarga el archivo sin tener acceso al resto de la nube.

## Los usuarios

- **admin**: puede todo (crear, editar, eliminar, exportar).
- **analista**: puede crear, editar y exportar.
- **consulta**: solo puede ver.
- Se entra con usuario y contraseña; el sistema devuelve un token que dura 8 horas (una credencial temporal).

## Las palabras técnicas (una línea cada una)

- **React**: la tecnología de la pantalla (lo que se ve en el navegador).
- **FastAPI**: el motor del servidor (recibe las órdenes y calcula; está hecho en Python).
- **SQLite**: la base de datos principal, guardada como archivo dentro del servidor.
- **EC2**: la computadora de Amazon donde vive todo; tiene la IP fija `100.57.30.193`.
- **S3**: el disco de Amazon donde quedan los respaldos exportados.
- **DynamoDB**: la base de datos de Amazon donde se espeja la auditoría.
- **AWS / nube**: los servicios de Amazon que se alquilan por internet; nada de esto está en un computador de la casa.
- **CSV**: un archivo de texto con filas y columnas separadas por `;` o `,`; es el formato para cargar lotes de certificados.
- **IP elástica**: una dirección de internet fija que no cambia aunque el servidor se reinicie.
- **URL firmada**: un enlace temporal (1 hora) que autoriza a descargar un archivo específico.
