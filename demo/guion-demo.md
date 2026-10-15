**Objetivo:** video de 5–7 minutos mostrando el sistema en uso real, con el autor **hablando a cámara**.
**Caso:** cierre de dividendos del ejercicio 2024 en nuam — registrar y respaldar los certificados DJ 1948 del SII.
**Regla del profesor:** mostrar la aplicación, no disertar. Cada frase dura 5–10 segundos.

---

## 0. Antes de grabar (5 minutos)

- [ ] Abrir `http://100.57.30.193/` y ver el login. Si no carga, el laboratorio está apagado: avisar y esperar.
- [ ] Usuario `admin` / `Admin1234!` (para registrar y cargar). El rol `analista` / `Analista1234!` se usa al final, en el móvil.
- [ ] Tener a mano los archivos: `carga-montos-demo-error.csv` y `carga-montos-demo.csv` (carpeta `demo/`).
- [ ] Tener a mano la tabla "Datos del certificado" de la sección 2.
- [ ] Cerrar notificaciones y pestañas. Grabar la pantalla completa en 1080p.
- [ ] Aparecer en cámara, aunque sea en un recuadro en una esquina de la grabación.
- [ ] Duración objetivo: 5–7 min. Si algo se traba, se corta y se repite esa toma.

## 1. El caso (lo que se narra al abrir la aplicación, 30 s)

"Trabajo en el área tributaria de nuam. Estamos cerrando los dividendos del ejercicio 2024: el SII entrega los certificados DJ 1948 y hay que dejar registrada la calificación de cada uno, con sus factores calculados, la trazabilidad de quién lo registró y el respaldo para contabilidad. Eso es lo que hace este mantenedor, y lo voy a hacer ahora con los certificados del período."

## 2. Datos del certificado (para tipear en la toma 3)

| Campo | Valor |
|---|---|
| Ejercicio | `2024` |
| Mercado | `CFI` |
| Instrumento | `AGUAS ANDINAS S.A.` |
| Fecha de pago | `2024-08-12` |
| Secuencia | `1` |
| N° de dividendo | `1450` |
| Tipo de sociedad | `A` (abierta) |
| Valor histórico | `300000` |
| Monto columna 8 (con crédito IDPC) | `150000` |
| Monto columna 12 (RAP) | `50000` |

Resultado que debe dar el sistema: base 8–19 = `200000` → factor columna 8 = `0,75` · factor columna 12 = `0,25` (suman `1`).

## 3. Toma por toma

| # | Acción en pantalla | Qué decir | Qué debe verse |
|---|---|---|---|
| 1 | Entrar con `admin` | "Entro con el rol administrador, que es el que registra y carga." | Login y luego la grilla con los registros del período |
| 2 | Filtro **Mercado = ACN** → **Buscar** | "La grilla lista lo ya cargado y se filtra por mercado, origen y período comercial." | Tabla filtrada |
| 3 | **Ingresar** → completar **Datos básicos** con la tabla de la sección 2 → pestaña **Montos** → tipear `150000` (col. 8) y `50000` (col. 12) → **Guardar** | "Registro el certificado que llegó hoy. Los montos van agrupados por concepto de la homologación del SII." | Formulario con los grupos bajo cada campo; mensaje de guardado |
| 4 | Buscar el registro → **Detalle** → **Calcular factores** | "El sistema divide cada monto por la base 8 a 19: 0,75 y 0,25. Así se reparte la base del dividendo." | Grilla M/F del detalle con los factores calculados |
| 5 | Abrir el registro en edición → pestaña **Factores** → escribir `0.8` en la columna 8 (se pasa de 1) → corregir a `0.75` | "Si me equivoco, la suma se calcula en vivo y me avisa antes de grabar." | Recuadro de suma en rojo ("¡supera 1!") y luego en verde |
| 6 | Pestaña **Auditoría** | "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora." | Tabla de auditoría con el usuario autenticado |
| 7 | **Carga de calificaciones** → subir `carga-montos-demo-error.csv` | "Este es el archivo que me devolvió el área. Antes de grabar, el sistema lo previsualiza y avisa la fecha mal escrita, las columnas que faltan y el tipo de sociedad inválido." | Vista previa con 3 registros y la lista de avisos |
| 8 | **Cancelar** → subir `carga-montos-demo.csv` → **Confirmar carga (3)** | "Cargo el lote completo del período: tres certificados, identificados por llave." | Mensaje "Carga OK: 3 insertados" |
| 9 | Botón **Exportar** → **JSON** | "Genero el respaldo del período: se publica en S3 y devuelve una URL firmada, que es la que le mando a contabilidad." | Modal y luego la descarga del JSON en una pestaña nueva |
| 10 | Cambiar a `analista` y abrir en vista móvil (390 px) | "Desde el teléfono reviso lo mismo: la grilla se convierte en tarjetas y el formulario se apila en una columna." | Grilla como tarjetas + modal de ingreso en una columna |

**Cierre en cámara (30 s):**
"El repositorio, el informe y la solución en la nube están en el documento de entrega. La aplicación corre en AWS con IP elástica, y el correo de la cuenta es el que está en ese documento."

## 4. Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El CSV dice "0 insertados, 3 actualizados" | Es una segunda toma: ya estaba cargado. La carga actualiza por llave; sirve igual. |
| El paso 3 dice "actualizado" en vez de guardar | Ese certificado ya existía: cambiar el N° de dividendo a `1451`. |
| **Exportar** muestra error | La nube no está configurada en ese entorno. En el servidor de la demo sí funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP. Revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` (su contraseña) y seguir. |

## 5. No hace falta mostrar

- El código, los tests o los diagramas: eso se evalúa en el informe.
- No leer el informe en cámara ni pasar diapositivas.
- No explicar el modelo de datos: se ve en la grilla y en el detalle.
