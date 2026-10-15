# Cómo se usa la app, paso a paso

Dirección: `http://100.57.30.193/`
Usuarios: `admin / Admin1234!` · `analista / Analista1234!` · `consulta / Consulta1234!`

## 1. Entrar

Abrir la dirección, escribir usuario y contraseña y apretar Entrar. Arriba a la derecha queda el nombre del usuario y el botón Salir.

## 2. La grilla (la lista principal)

Es la tabla con todas las calificaciones: un registro por dividendo. Arriba están los filtros:

- **Mercado** (Todos / ACN / CFI / FM), **Origen** (corredor / entidad) y **Período** (el año).
- Botón **Buscar** aplica los filtros; **Limpiar** los borra y recarga todo.

Cada fila tiene los botones **Ver** (detalle de solo lectura), **Modificar** (editar) y **Eliminar** (con confirmación). Si no hay nada cargado, la grilla muestra "Sin calificaciones. Usa «Ingresar» o carga un CSV."

## 3. Ingresar un certificado a mano

Botón **Ingresar** → se abre un formulario con tres pestañas:

- **Datos básicos**: mercado, instrumento, ejercicio, fecha de pago, secuencia, N° de dividendo, tipo de sociedad, valor histórico y origen.
- **Montos**: una casilla por columna (8 a 37), agrupadas por concepto (cada campo muestra debajo su grupo, por ejemplo "C8–11: Afectos a impuestos globales y/o adicional (IDPC)").
- **Factores**: lo mismo, pero para escribir factores a mano; arriba aparece la suma de las columnas 8–19 en vivo ("Suma factores 8–19: …") y avisa con "¡supera 1!" si te pasas.

Al apretar **Guardar**, el registro se crea (si tiene montos y no factores, la app los calcula sola).

## 4. Ver el detalle y calcular

Con **Ver** se abre el detalle: monto y factor por columna (M y F) y la suma. Si eres admin o analista aparece el botón **Calcular factores**: recalcula todos los factores desde los montos y los guarda.

## 5. Editar factores a mano

**Modificar** abre el mismo formulario con los datos ya cargados. En la pestaña **Factores** puedes escribir un valor y ver la suma cambiar en vivo; si supera 1, salta el aviso rojo. Con **Cancelar** no se guarda nada.

## 6. Eliminar

**Eliminar** pide confirmación ("¿Eliminar [instrumento] ej.[año]?") y borra el registro. Queda registrado en la auditoría.

## 7. Cargar un lote de certificados (CSV)

Botón **Carga de calificaciones**:

1. Elegir el tipo: **Montos (DJ 1948)** o **Factores (8-37)**.
2. Elegir el archivo CSV.
3. Aparece la **vista previa**: cuántos registros trae, cuántas columnas y la lista de avisos si algo está mal (fecha que no es AAAA-MM-DD, fila con columnas de menos, tipo de sociedad distinto de A/C).
4. Si todo está bien, apretar **Confirmar carga (N)**. El sistema avisa "Carga OK: N insertados, N actualizados".
5. La carga **actualiza por llave**: si el mismo dividendo ya existe, lo actualiza en vez de duplicarlo.

Columnas del archivo: `ejercicio, mercado, instrumento, fecha, secuencia, numero_dividendo, tipo_sociedad, valor_historico` + `monto_8…monto_19` (o `factor_8…factor_37` para el otro tipo).

## 8. La auditoría

La pestaña **Auditoría** lista cada acción: número, fecha, acción (INSERT / MODIFICAR / ELIMINAR), registro afectado, detalle y usuario. Lo mismo se espeja automáticamente en la nube (DynamoDB).

## 9. Exportar el respaldo

Botón **Exportar** → elegir **JSON** o **CSV** → la app sube el archivo completo a la nube (S3), muestra el nombre del archivo y el bucket, y devuelve una **URL firmada** (válida 1 hora) que abre la descarga en una pestaña nueva.

## 10. En el celular

En pantallas de menos de 560 píxeles la grilla se convierte en tarjetas (cada fila con sus etiquetas) y el formulario se apila en una sola columna. Todo funciona igual.

## Reglas fijas

| Regla | Valor |
|---|---|
| Formato de fecha | `AAAA-MM-DD` |
| Mercados | `ACN`, `CFI`, `FM` |
| Tipo de sociedad | `A` (abierta) o `C` (cerrada) |
| Origen | `corredor` o `entidad` |
| Suma de factores 8–19 | No puede superar `1` |
| Columnas de montos | 8 a 37, agrupadas por concepto (homologación SII) |
| Cargar / editar / exportar | solo `admin` y `analista` |
| Consulta | solo mirar |

## La demo (recorrido completo del video)

1. Entrar como `admin`.
2. Ver la grilla y los filtros.
3. **Carga de calificaciones** → `carga-montos-demo-error.csv` → ver los avisos → Cancelar.
4. **Carga de calificaciones** → `carga-montos-demo.csv` → Confirmar carga (3) → "3 insertados".
5. Filtrar **Mercado = ACN** → Buscar → quedan 2 (CENCOSUD y ENEL).
6. **Ver** en ENEL → **Calcular factores** → aparecen 0.625 y 0.375.
7. **Modificar** ENEL → Factores → escribir `0.7` (aviso "¡supera 1!") → corregir `0.625` → Cancelar.
8. **Ingresar** el certificado suelto (AGUAS ANDINAS S.A.) → Guardar → **Limpiar** para verlo en la grilla.
9. Pestaña **Auditoría**.
10. **Exportar** → JSON → URL firmada.
11. **Salir** → entrar como `analista` → achicar la ventana (vista móvil en tarjetas).
