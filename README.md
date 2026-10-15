# Mantenedor de Calificaciones Tributarias

Sistema web para que un **corredor de bolsa** registre los montos de dividendos que recibe de las empresas y los convierta en **factores de calificación tributaria**, manteniendo el historial completo y trazable.

[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?logo=fastapi&logoColor=white&style=flat)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black&style=flat)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite&logoColor=white&style=flat)](https://vitejs.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white&style=flat)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-29-2496ED?logo=docker&logoColor=white&style=flat)](https://www.docker.com/)

---

## Descripción

Los corredores de bolsa reciben cada año la información tributaria de las empresas en **PDF sin formato estándar**. Eso hace imposible automatizar la lectura, por lo que los datos deben ingresarse manualmente y convertirse en factores.

Este sistema ordena ese proceso: **ingreso manual de montos, cálculo automático de factores, carga masiva por CSV, prioridad local del corredor, exportación de respaldos y auditoría completa** de cada operación.

Proyecto del ramo **Proyecto Integrado** (INACAP), basado en un requerimiento real de la empresa **nuam** — el holding que une las bolsas de Santiago, Lima y Colombia.

## Características

- **Mantenedor** con filtros por mercado (acciones, CFI, fondos mutuos), origen y período comercial
- **Ingreso manual** de calificaciones con 29 campos de montos
- **Cálculo automático** de factores (columnas 8 a 37, redondeo a 8 decimales)
- **Carga masiva CSV** de montos (DJ 1948) o factores, con vista previa y validación de formato por línea antes de grabar, y actualización por llave si el registro ya existe
- **Interfaz adaptable**: la grilla y la auditoría se reordenan como tarjetas en pantallas pequeñas (menos de 560 px)
- **Suma de la base 8–19 en vivo** al completar los factores, con aviso cuando supera 1
- **Agrupación por concepto de homologación SII** visible bajo cada campo de montos y factores
- **Prioridad del corredor**: la información local nunca altera la de la Bolsa
- **Auditoría** de ingreso, modificación y eliminación (log con fecha y hora, con el usuario autenticado)
- **Seguridad**: login con JWT y roles (admin / analista / consulta); matriz de permisos aplicada en API y UI
- **Exportes**: botón de exportación JSON/CSV en la interfaz y respaldo de auditoría en DynamoDB, con URL firmada de S3 (opcional, se activa por variables de entorno)

## Stack tecnológico

| Capa | Tecnología | Rol |
|------|-----------|-----|
| Frontend | React + Vite | Interfaz: grilla, formularios, carga de archivos |
| Backend | Python + FastAPI | API REST y reglas de negocio |
| Base de datos | SQLite | Almacenamiento local, sin instalación |
| Seguridad | JWT + bcrypt | Autenticación, roles y auditoría por usuario |
| Nube (opcional) | DynamoDB + S3 | Historial de auditoría y exportes (AWS) |

## Requisitos previos

- Python 3.12 o superior
- Node.js 20 o superior
- npm

**O con Docker:**

- Docker + Docker Compose

## Instalación

### Con Docker (recomendado)

```bash
docker compose up --build
```

Opcional: `cp .env.example .env` para definir el secreto JWT y las contraseñas (por defecto usa las credenciales de demostración indicadas más abajo).

Abrir [http://localhost:5173](http://localhost:5173). La API queda en `http://localhost:8001/api`.

### Sin Docker

#### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

Abrir [http://localhost:5173](http://localhost:5173). La API queda en `http://localhost:8001/api`.

## Credenciales de demostración

| Usuario | Contraseña | Rol | Permisos |
|---|---|---|---|
| `admin` | `Admin1234!` | admin | Todo |
| `analista` | `Analista1234!` | analista | Lectura, escritura, carga masiva y auditoría |
| `consulta` | `Consulta1234!` | consulta | Solo lectura |

> Cambiar estas contraseñas y `FACTORUNO_SECRET` en producción (ver `.env.example`).

## Uso

1. **Iniciar sesión** con las credenciales de demostración.
2. **Ingresar calificación**: completar datos básicos (mercado, instrumento, fecha, secuencia) y los 29 campos de montos, agrupados por concepto de homologación SII.
3. **Calcular**: el sistema convierte los montos en factores; la suma de la base 8-19 se muestra en vivo y avisa si supera 1.
4. **Cargar CSV**: subir archivo con montos o factores; la aplicación muestra una vista previa con los registros detectados y los avisos de formato antes de grabar, y actualiza por llave (ejercicio + mercado + instrumento + fecha + secuencia + dividendo + tipo sociedad).
5. **Auditoría**: pestaña con el log de todas las operaciones.
6. **Exportar**: botón que genera el respaldo JSON/CSV, lo publica en S3 y abre la URL firmada (cuando la nube está configurada).

## Pruebas

```bash
cd backend
source .venv/bin/activate
pytest tests/ -q --cov=app
```

99 pruebas: 62 unitarias (reglas de negocio), 16 de autenticación y roles, 9 integrales de API, 9 de integración AWS (DynamoDB/S3 simulados) y 3 de rendimiento. Cobertura: 94 %; carga CSV de 500 filas en 0,11 s.

## Glosario tributario

| Término | Qué significa |
|---------|---------------|
| Calificación tributaria | Clasificación de los dividendos según su tratamiento tributario (cómo se gravan) |
| Factor | Proporción (entre 0 y 1) que representa cada categoría tributaria sobre el total de montos |
| Monto | Valor en pesos de cada categoría, según el certificado que envía la empresa |
| DJ 1948 / DJ 1922 | Declaraciones Juradas que los emisores presentan al SII con la información de dividendos |
| Certificado 70 | Certificado del SII que detalla la situación tributaria de los dividendos de una empresa |
| SII | Servicio de Impuestos Internos de Chile |
| ISFUT | Impuesto Sustitutivo al FUT: utilidades que pagan un impuesto único en vez de los impuestos finales |
| IDPC | Impuesto de Primera Categoría: impuesto que pagan las empresas sobre sus utilidades |
| IGC | Impuesto Global Complementario: impuesto progresivo que pagan las personas |
| FUT | Fondo de Utilidades Tributables: registro histórico de utilidades de una empresa |
| Llave de negocio | Combinación de campos (ejercicio + mercado + instrumento + fecha + secuencia + dividendo + tipo sociedad) que identifica un registro de forma única; se usa para actualizar en la carga masiva |
| Corredor de bolsa | Intermediario que compra y vende valores por cuenta de sus clientes |
| nuam | Holding que integra las bolsas de Santiago, Lima y Colombia |

## Estructura del proyecto

```
factoruno/
├── backend/
│   ├── app/
│   │   ├── main.py       →  API (rutas)
│   │   ├── servicio.py   →  lógica de negocio (CRUD, CSV, auditoría, exportes)
│   │   ├── reglas.py     →  reglas del HDU (cálculo de factores)
│   │   ├── auth.py       →  autenticación JWT y roles
│   │   ├── aws_ext.py    →  DynamoDB (auditoría) y S3 (exportes)
│   │   └── db.py         →  base de datos SQLite
│   └── tests/            →  pruebas unitarias, integrales y de rendimiento
├── frontend/
│   └── src/
│       ├── App.jsx       →  pantalla principal + login
│       ├── api.js        →  comunicación con el backend (token Bearer)
│       └── columnas.js   →  nombres de los 30 factores y agrupación por concepto SII
├── docs/
│   ├── informe/          →  secciones del informe (rúbrica Ev2)
│   └── seguridad/        →  amenazas/mitigación y codificación segura
├── odd/tasks/            →  seguimiento del trabajo (ODD)
└── README.md
```

## Fuentes

- `HDU_Inacap.xlsx` — Historias de Usuario del cliente (nuam): objetivo, alcance, historias, tipos de datos, homologación, formato CSV y flujo de proceso.
- `Apunte_Proyecto_Integrado.md` — resumen del ramo: metodología, contexto de nuam y análisis completo del HDU.

## Estado del proyecto

- [x] Backend: CRUD, cálculo de factores, carga CSV, auditoría
- [x] Frontend: grilla, filtros, formulario, detalle, carga CSV con vista previa, exportación a S3 y vista móvil en tarjetas
- [x] Validaciones de negocio (suma ≤ 1, 8 decimales)
- [x] Seguridad: JWT + roles, hardening (CORS, CSP, headers), STRIDE y codificación segura documentados
- [x] Pruebas: 99 pruebas (unitarias, integrales, rendimiento) — 94 % de cobertura
- [x] Nube: DynamoDB (auditoría) y S3 (exportes) + despliegue en AWS (RHEL 9 + Docker Compose)
- [ ] Módulo RAG (asistente de preguntas) — siguiente paso

## Licencia

Proyecto académico — ramo Proyecto Integrado, INACAP 2026.
