**Video:** 5–7 minutos · **Caso:** cierre de dividendos del ejercicio 2024 en nuam
**Regla del profesor:** mostrar la aplicación, no disertar. Frases de 5–10 segundos.
**Cómo leer este documento:** una toma por página. Cada página dice qué hacer, qué escribir, qué decir y qué debe verse. No hay que buscar nada en otras páginas.

## Antes de grabar

- [ ] Abrir `http://100.57.30.193/`. Si no carga, el laboratorio está apagado: avisar y esperar.
- [ ] Usuario `admin` / `Admin1234!` (tomas 1 a 9). Solo la toma 10 usa `analista` / `Analista1234!`.
- [ ] Tener a mano los dos archivos: `carga-montos-demo-error.csv` y `carga-montos-demo.csv`.
- [ ] Cerrar notificaciones y pestañas. Grabar en 1080p con la cámara a la vista.
- [ ] Si algo se traba: se corta y se repite esa toma.

<div style="page-break-after: always;"></div>

## Toma 1 — Entrar al sistema

**Hacer:** abrir `http://100.57.30.193/`, usuario `admin`, contraseña `Admin1234!`.

**Decir:** "Trabajo en el área tributaria de nuam. Estamos cerrando los dividendos del ejercicio 2024: el SII entrega los certificados DJ 1948 y hay que dejar registrada la calificación de cada uno, con sus factores, la trazabilidad y el respaldo para contabilidad. Eso es lo que hace este mantenedor."

**Ver:** la pantalla de login y después la grilla con los registros ya cargados.

<div style="page-break-after: always;"></div>

## Toma 2 — Filtrar la grilla

**Hacer:** en **Mercado** elegir `ACN` y apretar **Buscar**.

**Decir:** "La grilla lista lo ya cargado y se filtra por mercado, origen y período comercial."

**Ver:** la tabla con menos filas: solo las del mercado elegido.

<div style="page-break-after: always;"></div>

## Toma 3 — Registrar el certificado que llegó hoy

**Hacer:** botón **Ingresar** → pestaña **Datos básicos**.

**Escribir (Datos básicos):**
Ejercicio `2024` · Mercado `CFI` · Instrumento `AGUAS ANDINAS S.A.` · Fecha de pago `2024-08-12` · Secuencia `1` · N° de dividendo `1450` · Tipo de sociedad `A` · Valor histórico `300000`.

**Hacer:** pestaña **Montos**.

**Escribir (Montos):** columna 8 = `150000` · columna 12 = `50000`. Todo lo demás queda en 0.

**Decir:** "Registro el certificado que llegó hoy. Los montos van agrupados por concepto de la homologación del SII."

**Ver:** el mensaje de guardado y el registro nuevo en la grilla.

<div style="page-break-after: always;"></div>

## Toma 4 — Ver el cálculo que hace el sistema

**Hacer:** en la grilla apretar **Buscar** para refrescar → abrir el registro `AGUAS ANDINAS S.A.` → botón **Detalle** → botón **Calcular factores**.

**Decir:** "El sistema divide cada monto por la base 8 a 19: 0,75 y 0,25. Así se reparte la base del dividendo."

**Ver:** en el detalle, monto y factor por columna: columna 8 → `150000` / `0,75` y columna 12 → `50000` / `0,25`.

<div style="page-break-after: always;"></div>

## Toma 5 — Corregir un error de tipeo

**Hacer:** abrir el registro `AGUAS ANDINAS S.A.` en edición → pestaña **Factores** → en la columna 8 escribir `0.8` → después corregirlo a `0.75`.

**Decir:** "Si me equivoco, la suma se calcula en vivo y me avisa antes de grabar."

**Ver:** el recuadro de suma en rojo con "¡supera 1!"; al corregirlo, vuelve a 1 con "(≤ 1 ✓)". Cerrar con **Cancelar**.

<div style="page-break-after: always;"></div>

## Toma 6 — Auditoría

**Hacer:** pestaña **Auditoría**.

**Decir:** "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora."

**Ver:** la tabla con el registro del ingreso recién hecho y el usuario `admin`.

<div style="page-break-after: always;"></div>

## Toma 7 — Previsualizar el archivo que devolvió el área

**Hacer:** botón **Carga de calificaciones** → Tipo de carga `Montos (DJ 1948)` → Archivo → elegir `carga-montos-demo-error.csv`.

**Decir:** "Este archivo me lo devolvieron con problemas. Antes de grabar, el sistema lo previsualiza: me dice cuántos registros trae y qué línea está mal."

**Ver:** la vista previa con 3 registros y la lista de avisos (fecha inválida, una fila con columnas de menos, tipo de sociedad inválido). Apretar **Cancelar**.

<div style="page-break-after: always;"></div>

## Toma 8 — Cargar el lote del período

**Hacer:** botón **Carga de calificaciones** → Tipo de carga `Montos (DJ 1948)` → Archivo → elegir `carga-montos-demo.csv` → botón **Confirmar carga (3)**.

**Decir:** "Este es el lote correcto del período: tres certificados, identificados por llave."

**Ver:** el mensaje "Carga OK: 3 insertados" y los 3 registros nuevos en la grilla.

<div style="page-break-after: always;"></div>

## Toma 9 — Exportar el respaldo

**Hacer:** botón **Exportar** → **JSON**.

**Decir:** "Genero el respaldo del período: se publica en S3 y devuelve una URL firmada, que es la que le mando a contabilidad."

**Ver:** el modal con el nombre del archivo y el bucket; después la descarga del JSON en una pestaña nueva.

<div style="page-break-after: always;"></div>

## Toma 10 — Cierre en el teléfono

**Hacer:** **Salir** → entrar con `analista` / `Analista1234!` → achicar la ventana hasta unos 390 px de ancho (o abrir la misma dirección en el teléfono).

**Decir:** "Desde el teléfono reviso lo mismo: la grilla se convierte en tarjetas y el formulario se apila en una columna. El repositorio, el informe y la solución en la nube están en el documento de entrega."

**Ver:** la grilla como tarjetas (etiqueta a la izquierda, valor a la derecha) y el formulario de ingreso en una sola columna.

<div style="page-break-after: always;"></div>

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El paso 3 guarda pero la grilla no muestra el registro | Apretar **Buscar** para refrescar la lista. |
| El CSV dice "0 insertados, 3 actualizados" | Es una segunda toma: ya estaba cargado. La carga actualiza por llave; sirve igual. |
| El paso 3 dice que actualizó en vez de insertar | Ese certificado ya existía: cambiar el N° de dividendo a `1451`. |
| **Exportar** muestra error | La nube no está configurada en ese entorno. En el servidor de la demo sí funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP. Revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` con `Analista1234!` y seguir. |

## No hace falta mostrar

- El código, los tests o los diagramas: eso se evalúa en el informe.
- No leer el informe en cámara ni pasar diapositivas.
- No explicar el modelo de datos: se ve en la grilla y en el detalle.
