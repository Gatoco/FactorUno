# FactorUno — guía de la demo

**Video:** 5–7 min · **Aplicación:** FactorUno, el mantenedor de calificaciones tributarias de dividendos que desarrollé para la empresa **nuam** (la bolsa). **Caso:** cierre de dividendos del ejercicio 2024.
**Quién habla:** el autor, en primera persona. **Regla del profesor:** mostrar la app, no disertar; frases de 5–10 segundos.
**Cómo leer:** cada toma trae **Hacer** (clic por clic) → **Decir** (se lee tal cual) → **Ver** (lo que debe verse).

## Antes de grabar

- [ ] Abrir `http://100.57.30.193/`. Si no carga, el laboratorio está apagado (avisar y esperar).
- [ ] Usuario `admin` / `Admin1234!` para las tomas 1 a 10; `analista` / `Analista1234!` solo en la toma 11.
- [ ] Tener a mano los CSV de esta carpeta: `carga-montos-demo-error.csv` (toma 3) y `carga-montos-demo.csv` (toma 4).
- [ ] Cerrar notificaciones y pestañas; grabar en 1080p con la cámara a la vista. Si algo se traba: cortar y repetir la toma.

### Toma 1 — Entrar
**Hacer:** abrir `http://100.57.30.193/` → campo **Usuario**: `admin` → campo **Contraseña**: `Admin1234!` → botón **Ingresar**.
**Decir:** "Esta es FactorUno, la aplicación que desarrollé para la empresa nuam, la bolsa: registra la calificación de los dividendos del ejercicio 2024, con sus factores, la trazabilidad y el respaldo. Ya está publicada en la nube, así que la abro directo."
**Ver:** el login (título "Calificaciones Tributarias") y, al entrar, la grilla, todavía vacía: los certificados se cargan en la toma 4.

### Toma 2 — Grilla y filtros
**Hacer:** pasar el mouse por la tabla, sin apretar nada; señalar los filtros **Mercado**, **Origen**, **Período**, los botones **Buscar** y **Limpiar**, y la barra **Ingresar**, **Carga de calificaciones** y **Exportar**.
**Decir:** "La grilla lista los certificados del período y parte vacía: los cargo en un momento. Arriba se filtra por mercado, origen y período comercial."
**Ver:** el mensaje "Sin calificaciones. Usa «Ingresar» o carga un CSV." y todos los botones. Con datos, cada fila tiene **Ver**, **Modificar** y **Eliminar**.

### Toma 3 — Revisar un archivo con errores
**Hacer:** botón **Carga de calificaciones** → dejar el tipo en `Montos (DJ 1948)` → cuadro **Archivo**: elegir `carga-montos-demo-error.csv` → mirar la vista previa ("3 registros detectados · 20 columnas · 3 avisos de formato") → **Cancelar**.
**Decir:** "Este archivo tiene errores a propósito, para mostrar la validación. Antes de grabar, el sistema lo previsualiza: dice cuántos registros trae y qué línea está mal."
**Ver:** la vista previa con las primeras 5 filas y los 3 avisos (fecha inválida, fila con columnas de menos, sociedad inválida). Nada se grabó.

### Toma 4 — Cargar el lote
**Hacer:** **Carga de calificaciones** → `Montos (DJ 1948)` → **Archivo**: elegir `carga-montos-demo.csv` → verificar la vista previa ("3 registros · sin problemas") → **Confirmar carga (3)**.
**Decir:** "Ahora el mismo formato con datos válidos: tres certificados identificados por llave, así la carga actualiza en vez de duplicar."
**Ver:** "Carga OK: 3 insertados, 0 actualizados" y las filas `CENCOSUD S.A.`, `ENEL AMERICAS S.A.` y `FONDO MUTUO LARRAIN VIAL`.

### Toma 5 — Filtrar por mercado
**Hacer:** lista **Mercado**: elegir `ACN` → **Buscar**.
**Decir:** "Filtro por mercado: quedan solo los dos certificados de acciones que acabo de cargar."
**Ver:** la tabla con 2 filas: `CENCOSUD S.A.` y `ENEL AMERICAS S.A.`

### Toma 6 — Ver el cálculo
**Hacer:** en la fila `ENEL AMERICAS S.A.`, botón **Ver** → **Calcular factores** → mirar la columna **8** (`M: 200.000` / `F: 0.625`) y la columna **12** (`M: 120.000` / `F: 0.375`) → **Cerrar**.
**Decir:** "El sistema divide cada monto por la base 8 a 19: 0,625 y 0,375. Así se reparte la base del dividendo."
**Ver:** monto y factor por columna (el factor se muestra con punto decimal) y el mensaje "Factores recalculados".

### Toma 7 — Corregir un error de tipeo
**Hacer:** fila `ENEL AMERICAS S.A.` → **Modificar** → pestaña **Factores** → campo que empieza con **8**: escribir `0.7` → ver el aviso rojo "1.07500000 ¡supera 1!" → corregir a `0.625` → vuelve a "1.00000000 (≤ 1 ✓)" → **Cancelar**.
**Decir:** "Si me equivoco, la suma se calcula en vivo y me avisa antes de grabar."
**Ver:** el recuadro de suma que cambia de rojo (¡supera 1!) a normal (≤ 1 ✓).

### Toma 8 — Ingresar a mano
**Hacer:** botón **Ingresar** → pestaña **Datos básicos**, completar campo por campo:

| Campo | Qué escribir / elegir |
|---|---|
| Mercado | `CFI` |
| Instrumento | `AGUAS ANDINAS S.A.` |
| Ejercicio | `2024` (borrar el año que trae por defecto) |
| Fecha de pago | `2024-08-12` |
| Secuencia | `1` |
| N° de dividendo | `1450` |
| Tipo de sociedad | `Abierta (A)` |
| Valor histórico | `300000` |
| Origen | dejar `corredor` · ISFUT: sin marcar |

Después: pestaña **Montos** → campo **8** = `150000`, campo **12** = `50000` (el resto queda en 0) → **Guardar** → en la grilla, **Limpiar** (quita el filtro ACN de la toma 5).
**Decir:** "Cuando llega un certificado suelto, lo ingreso a mano. Los montos van agrupados por concepto de la homologación del SII."
**Ver:** el mensaje "Calificación creada"; tras **Limpiar**, `AGUAS ANDINAS S.A.` junto a los otros tres.

### Toma 9 — Auditoría
**Hacer:** pestaña **Auditoría**.
**Decir:** "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora, y además se replica en la base de datos en la nube."
**Ver:** la tabla con el ingreso recién hecho (acción INSERT) y el usuario `admin`.

### Toma 10 — Exportar
**Hacer:** botón **Exportar** → **JSON** → ver el nombre del archivo y el bucket; la descarga se abre en una pestaña nueva con la URL firmada → **Cerrar**.
**Decir:** "El respaldo se publica en S3 y el sistema devuelve una URL firmada que dura una hora, para compartirlo sin dar acceso al bucket."
**Ver:** el modal con `factoruno-...json`, el bucket y la descarga.

### Toma 11 — Cierre en el teléfono
**Hacer:** **Salir** → entrar con `analista` / `Analista1234!` → achicar la ventana a unos 390 px de ancho (o abrir la misma dirección en el teléfono).
**Decir:** "La misma aplicación en pantalla chica: la grilla se convierte en tarjetas y el formulario se apila en una columna. Con esto cierro la demo; el repositorio, el informe y la solución en la nube están en el documento de entrega."
**Ver:** la grilla como tarjetas (etiqueta a la izquierda, valor a la derecha) y el formulario de ingreso en una sola columna.

## Si algo falla

| Síntoma | Qué hacer |
|---|---|
| La toma 4 dice "0 insertados, 3 actualizados" | Normal: la carga actualiza por llave. Sirve igual para la demo. |
| La toma 5 muestra menos filas de las esperadas | Volver a cargar `carga-montos-demo.csv`. |
| La toma 8 dice que actualizó en vez de insertar | Ese certificado ya existía: cambiar el N° de dividendo a `1451`. |
| La grilla no muestra lo recién guardado | Clic en **Limpiar** o **Buscar** para refrescar. |
| **Exportar** muestra error | La nube no está configurada en ese entorno; en el servidor de la demo funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP: revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` / `Analista1234!` y seguir. |

## Después de grabar

1. Subir el video (Drive o YouTube no listado) y pegar el enlace en el documento de entrega, en la línea del video.
2. Avisar para dejar la grilla con datos de ejemplo y el laboratorio encendido el día de la entrega.

## No hace falta mostrar

El código, los tests, los diagramas y el informe: eso se evalúa aparte. No leer el informe en cámara ni pasar diapositivas.
