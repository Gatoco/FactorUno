<div align="center">

# Mantenedor de Calificaciones Tributarias

**FactorUno** — registra los montos que un corredor de bolsa recibe de sus empresas<br>
y los convierte en **factores de calificación tributaria**, con historial completo y trazable.

Proyecto del ramo **Proyecto Integrado** (INACAP 2026), inspirado en un requerimiento real de **nuam**,<br>
el holding que une las bolsas de Santiago, Lima y Colombia.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?logo=fastapi&logoColor=white&style=for-the-badge)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black&style=for-the-badge)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite&logoColor=white&style=for-the-badge)](https://vitejs.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white&style=for-the-badge)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-29-2496ED?logo=docker&logoColor=white&style=for-the-badge)](https://www.docker.com/)

[![Sitio](https://img.shields.io/badge/sitio-factoruno.t420.dev-00c853?style=for-the-badge)](https://factoruno.t420.dev)

</div>

---

## Cómo funciona

Del documento del SII al log de auditoría — cada monto se ingresa una vez y termina como factor trazable:

```text
   SII · DJ 1948  ─┐
   Certificados   ─┼──▶  Ingreso  ──▶  Cálculo  ──▶  Mantenedor  ──▶  Auditoría
   Archivos       ─┘     manual · CSV  8.º decimal   grilla           log
```

## Stack tecnológico

| Capa | Tecnología | Rol |
|------|-----------|-----|
| Frontend | React + Vite | Grilla, formularios y carga de archivos |
| Backend | Python + FastAPI | API REST y reglas de negocio |
| Base de datos | SQLite | Almacenamiento local |
| Deploy | Docker / Compose | Ambiente reproducible |

## Características

- **Mantenedor en grilla** — filtros por mercado, origen y período comercial.
- **Doble vía de ingreso** — la carga manual de los 29 campos de montos o un CSV con vista previa.
- **Cálculo trazable** — factores redondeados al 8.º decimal; la suma de la base 8–19 nunca supera 1.
- **Prioridad del corredor** — la información local nunca sobrescribe la de la Bolsa.
- **Auditoría completa** — cada ingreso, modificación y eliminación queda registrada.

## Arquitectura

Un solo `docker compose up` levanta el sistema completo:

```text
┌─────────────────────── Docker Compose ───────────────────────┐
│                                                              │
│   ┌────────────────┐    REST     ┌────────────────┐          │
│   │    Frontend    │ ─────────▶  │    Backend     │          │
│   │  React + Vite  │             │ Python+FastAPI │          │
│   └────────────────┘             └───────┬────────┘          │
│                                          │                   │
│                                  ┌───────▼────────┐          │
│                                  │     SQLite     │          │
│                                  └────────────────┘          │
└──────────────────────────────────────────────────────────────┘
```

## Ejecución

### Con Docker (recomendado)

```bash
cp .env.example .env    # completar la configuración (ver el archivo)
docker compose up --build
```

Abrir [http://localhost:5173](http://localhost:5173). La API queda en `http://localhost:8001/api`.

### Sin Docker

Backend:

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Estructura

```text
factoruno/
├── backend/                 API FastAPI, reglas de negocio y datos
│   ├── app/                 rutas, modelos y lógica
│   └── tests/               pruebas automatizadas
├── frontend/                interfaz React + Vite
│   └── src/                 grilla, formularios, carga CSV
├── docker-compose.yml       ambiente reproducible
└── README.md
```

## Pruebas

```bash
cd backend
pytest tests/ -q
```

## Licencia

Proyecto académico — ramo Proyecto Integrado, INACAP 2026.

---

<div align="center">
<sub><strong>FactorUno</strong> · Proyecto Integrado · INACAP 2026<br>
Una sola fuente de verdad tributaria</sub>
</div>
