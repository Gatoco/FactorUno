**Aplicación:** http://100.57.30.193/

**Usuarios de prueba**

| Rol | Usuario | Contraseña | Qué puede hacer |
|---|---|---|---|
| Administrador | `admin` | `Admin1234!` | Todo: ver, ingresar, modificar, eliminar, cargar CSV, exportar y ver auditoría |
| Analista | `analista` | `Analista1234!` | Lo mismo que el administrador |
| Consulta | `consulta` | `Consulta1234!` | Solo ver: grilla, filtros, detalle y auditoría (sin botones de edición) |

## 1. Entrar

1. Abre `http://100.57.30.193/` en el navegador.
2. Escribe el usuario y la contraseña y pulsa **Ingresar**.
3. Arriba a la derecha queda tu nombre y el botón **Salir**.

## 2. Ver la grilla de calificaciones

La grilla lista las calificaciones con: ejercicio, mercado, instrumento, fecha de pago, secuencia, N° de dividendo, tipo de sociedad (A/C), ISFUT, origen y fuente.

1. Filtra por **Mercado** (ACN, CFI o FM), **Origen** (corredor o entidad) y **Período** (el año, por ejemplo 2024).
2. Pulsa **Buscar**. Para volver a ver todo, pulsa **Limpiar**.

## 3. Ver el detalle de una calificación

1. En la fila que te interesa, pulsa **Ver**.
2. El detalle muestra los 30 montos y los 30 factores por columna, y la suma de la base (columnas 8–19).
3. Cierra con **Cerrar** o con la ×.

## 4. Ingresar una calificación manualmente

1. Pulsa **Ingresar**.
2. En **Datos básicos** completa: ejercicio, mercado, instrumento, fecha de pago (AAAA-MM-DD), secuencia, N° de dividendo, tipo de sociedad (A o C) y valor histórico.
3. Pestaña **Montos**: escribe los montos del certificado en las columnas que correspondan. Debajo de cada campo aparece el grupo de homologación SII al que pertenece (por ejemplo `C8–11: Afectos a impuestos globales y/o adicional (IDPC)`).
4. Pestaña **Factores**: solo si vas a escribir los factores a mano. La app muestra en vivo la suma de la base 8–19: si supera 1 aparece el aviso rojo **¡supera 1!**.
5. Pulsa **Guardar**. El registro queda en la grilla y registrado en la auditoría.

## 5. Calcular los factores automáticamente

1. Abre el detalle del registro con **Ver**.
2. Pulsa **Calcular factores**.
3. La app divide cada monto por la suma de los montos de las columnas 8–19 (redondeo a 8 decimales) y guarda el resultado.
   Ejemplo: 150.000 en la columna 8 y 50.000 en la columna 12 (suma 200.000) → factores 0,75 y 0,25.

## 6. Modificar o eliminar

1. En la fila, pulsa **Modificar** para editar: se abre el mismo formulario con los datos cargados; termina con **Guardar**.
2. Pulsa **Eliminar** y confirma en el diálogo para borrar el registro.
3. Estos dos botones solo los ven el administrador y el analista.

## 7. Cargar un archivo CSV

1. Pulsa **Carga de calificaciones**.
2. Elige el tipo de carga: **Montos (DJ 1948)** o **Factores (8-37)**.
3. Selecciona el archivo. **Antes de grabar aparece la vista previa**: cuántos registros y columnas detectó y los avisos de formato (fecha que no sea AAAA-MM-DD, filas con menos columnas que la cabecera, tipo de sociedad distinto de A o C).
4. Si la vista previa está correcta, pulsa **Confirmar carga (N)**. El aviso confirma: *Carga OK: N insertados, M actualizados*.
5. Si el registro ya existía (misma llave: ejercicio + mercado + instrumento + fecha de pago + secuencia + N° de dividendo + tipo de sociedad), la carga lo **actualiza** en vez de duplicarlo.
6. Archivos de ejemplo: `carga-montos-demo.csv` (3 registros nuevos) y `carga-montos-demo-error.csv` (con errores a propósito, solo para mostrar la validación).
7. Columnas del archivo: ejercicio, mercado, instrumento, fecha, secuencia, numero_dividendo, tipo_sociedad, valor_historico, `monto_8`…`monto_19` (tipo montos) o `factor_8`…`factor_37` (tipo factores).

## 8. Ver la auditoría

1. Pestaña **Auditoría**.
2. Cada operación (INSERT, UPDATE, DELETE) registra: número, fecha, acción, registro afectado, detalle y usuario.
3. La auditoría también se replica en la tabla DynamoDB `factoruno-auditoria`.

## 9. Exportar el respaldo

1. Pulsa **Exportar** y elige **CSV** o **JSON**.
2. La app genera el respaldo de todas las calificaciones, lo sube al bucket S3 del proyecto y abre una **URL firmada** válida por 1 hora. El modal muestra el nombre del archivo y el bucket.

## 10. Usar la app en el celular

- En pantallas angostas (menos de 560 px) la grilla y la auditoría se muestran como **tarjetas** (nombre del campo a la izquierda, valor a la derecha) y el formulario queda en una sola columna.

## 11. Salir

- Pulsa **Salir** arriba a la derecha. La sesión expira sola a las 8 horas.

## Reglas que la aplicación siempre aplica

| Regla | Valor |
|---|---|
| Fecha de pago | Formato AAAA-MM-DD |
| Mercado | ACN, CFI o FM |
| Tipo de sociedad | A (abierta) o C (cerrada) |
| Origen | corredor o entidad |
| Suma de la base (columnas 8–19) | menor o igual a 1 |
| Columnas de montos y factores | 8 a 37, agrupadas por concepto de homologación SII |
| Quién puede editar | administrador y analista |
