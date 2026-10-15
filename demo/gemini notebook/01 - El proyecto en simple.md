# FactorUno — el proyecto explicado en simple

## Qué es

FactorUno es una aplicación web (se usa en el navegador) que sirve para **registrar y calcular la calificación tributaria de los dividendos** que reparte la bolsa.

La aplicación la desarrollé para la empresa **nuam** (la bolsa), a partir de sus historias de usuario reales (HDU): las reglas y los formatos salen de ese material, no son inventados.

## El problema que resuelve

Cada vez que una empresa paga un dividendo, el Servicio de Impuestos Internos (SII) obliga a desglosar ese dividendo en muchos conceptos tributarios distintos (créditos, rentas exentas, montos no constitutivos de renta, etc.). Ese desglose viaja en un certificado llamado **DJ 1948**, donde cada concepto tiene una **columna numerada** (de la 8 a la 37).

Antes de esta aplicación, el cálculo se hacía de forma manual o con planillas: hay que tomar los montos de cada columna, sumarlos y dividir para obtener **factores** (fracciones), dejando registro de todo. Es lento y fácil de equivocar.

FactorUno hace ese trabajo: registra cada certificado con sus montos, calcula los factores automáticamente, deja trazabilidad de quién hizo qué y genera respaldos en la nube.

## Qué hace la aplicación

- Guarda las calificaciones (un registro por dividendo: empresa, fecha, montos por columna).
- Calcula los factores de cada columna: `factor = monto ÷ suma de los montos de las columnas 8 a 19`.
- Permite cargar certificados uno a uno o por lotes con un archivo CSV (con vista previa y validación antes de grabar).
- Registra una auditoría de todos los cambios (INSERT, MODIFICAR, ELIMINAR) con usuario y fecha, y la espeja en la nube.
- Exporta respaldos (JSON/CSV) a la nube con una URL firmada válida por 1 hora.
- Tiene tres tipos de usuario: **admin** (todo), **analista** (crear y editar) y **consulta** (solo ver).
- Funciona también en pantallas chicas: en el teléfono la grilla se convierte en tarjetas.

## Dónde vive todo (la nube, en simple)

- La aplicación está publicada en un servidor de **AWS** (Amazon) con una **dirección fija**: `http://100.57.30.193/`.
- **AWS** = la nube de Amazon: computadoras alquiladas por internet. El servidor se llama **EC2** y tiene una "IP elástica" (una dirección que no cambia aunque se reinicie).
- Los respaldos exportados se guardan en **S3** (un disco virtual de Amazon) y la auditoría se copia a **DynamoDB** (una base de datos de Amazon).
- Por dentro: la pantalla está hecha con **React**, el motor que calcula está hecho con **FastAPI** (Python) y los datos se guardan en **SQLite** (una base de datos en un archivo).

## El caso del video (cierre de dividendos 2024)

1. Entrar como administrador: la aplicación ya está publicada en la nube.
2. Mostrar la grilla con los certificados del período.
3. Previsualizar un archivo con errores para mostrar cómo valida.
4. Cargar un lote de 3 certificados válidos ("3 insertados").
5. Filtrar por mercado ACN y abrir uno (ENEL AMERICAS).
6. Ver el detalle y calcular los factores (0.625 y 0.375).
7. Revisar la auditoría (quién cambió qué).
8. Exportar el respaldo y mostrar la URL firmada.
9. Terminar mostrando la versión móvil.

## Material de origen (real, del ramo)

- El **HDU** (historias de usuario) y el Excel de **homologación de columnas** son material real de la empresa nuam: definen los campos, las columnas y las reglas.
- Los 3 certificados de la demo (CENCOSUD S.A., ENEL AMERICAS S.A., FONDO MUTUO LARRAIN VIAL) son de ejemplo, creados para la demostración.
