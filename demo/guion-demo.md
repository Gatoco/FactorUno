**Objetivo:** video de 5–7 minutos mostrando el sistema funcionando, con el autor **hablando a cámara**.
**Regla del profesor:** mostrar la aplicación, no disertar. Cada frase dura 5–10 segundos.

---

## 0. Antes de grabar (5 minutos)

- [ ] Abrir `http://100.57.30.193/` y ver el login. Si no carga, el laboratorio está apagado: avisar y esperar.
- [ ] Usuario `admin` / `Admin1234!` (para editar). El rol `analista` / `Analista1234!` se usa al final, en el móvil.
- [ ] Tener a mano los archivos: `demo/carga-montos-demo-error.csv` y `demo/carga-montos-demo.csv`.
- [ ] Cerrar notificaciones y pestañas. Grabar la pantalla completa en 1080p.
- [ ] Aparecer en cámara, aunque sea en un recuadro en una esquina de la grabación.
- [ ] Duración objetivo: 5–7 min. Si algo se traba, se corta y se repite esa toma.

## 1. Quién narra

Es un **proyecto individual**: una sola persona narra y muestra todas las tomas. Al cambiar de usuario, alcanza con decir "ahora entro como analista".

## 2. Toma por toma

| # | Acción en pantalla | Qué decir (breve) | Qué debe verse |
|---|---|---|---|
| 1 | Abrir la URL y entrar con `admin` | "Este es el mantenedor de calificaciones tributarias de nuam. Entramos con el rol administrador." | Pantalla de login y luego la grilla con datos |
| 2 | Usar los filtros: Mercado = **ACN**, botón **Buscar** | "La grilla lista las calificaciones cargadas y se filtra por mercado, origen y período comercial." | Tabla filtrada (3 registros de la demo) |
| 3 | Botón **Ingresar** → pestaña **Montos** | "Ingresamos una calificación manualmente. Los campos están agrupados por concepto de la homologación del SII." | Formulario con los grupos bajo cada campo; scrollear lento |
| 4 | Pestaña **Factores** → escribir dos valores | "Al completar los factores, la suma de la base 8 a 19 se calcula en vivo y avisa si supera 1." | Recuadro de suma cambiando; el aviso rojo al pasarse |
| 5 | Cerrar, abrir **Detalle** de un registro → **Calcular factores** | "El sistema divide cada monto por la base y muestra monto y factor por columna." | Grilla M/F del detalle con los factores calculados |
| 6 | Pestaña **Auditoría** | "Cada ingreso, modificación o eliminación queda auditado con usuario, fecha y hora." | Tabla de auditoría con el usuario autenticado |
| 7 | **Carga de calificaciones** → subir `carga-montos-demo-error.csv` | "Antes de grabar, la aplicación previsualiza el archivo y valida: avisa la fecha mal escrita, las columnas que faltan y el tipo de sociedad inválido." | Vista previa con 3 registros y la lista de 3 avisos |
| 8 | Cancelar y subir `carga-montos-demo.csv` → **Confirmar carga (3)** | "Con el archivo correcto, confirma la carga: tres registros insertados por llave." | Mensaje "Carga OK: 3 insertados, 0 actualizados" |
| 9 | Botón **Exportar** → **JSON** | "El respaldo se publica en S3 y devuelve una URL firmada, que abre la descarga." | Modal y luego la descarga del JSON en una pestaña nueva |
| 10 | Cambiar a `analista` y abrir en vista móvil (390 px) | "En el teléfono la grilla se convierte en tarjetas y el formulario se apila en una columna." | Grilla como tarjetas + modal de ingreso en una columna |

**Cierre en cámara (30 s):**
"El repositorio, el informe y la solución en la nube están en el documento de entrega. La aplicación corre en AWS con IP elástica, y el correo de la cuenta es el que está en ese documento."

## 3. Si algo falla

| Síntoma | Qué hacer |
|---|---|
| El CSV dice "0 insertados, 3 actualizados" | Ya estaba cargado: es correcto, la carga actualiza por llave. Sirve igual para el video. |
| **Exportar** muestra error | La nube no está configurada en ese entorno. En el servidor de la demo sí funciona. |
| La página no responde | El laboratorio se apagó o cambió de IP. Revisar antes de grabar. |
| El login con `admin` falla | Probar `analista` (misma contraseña de rol) y seguir. |

## 4. No hace falta mostrar

- El código, los tests o los diagramas: eso se evalúa en el informe.
- No leer el informe en cámara ni pasar diapositivas.
- No explicar el modelo de datos: se ve en la grilla y en el detalle.
