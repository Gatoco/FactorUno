# Mantenedor de Calificaciones Tributarias

Sistema web para que un **corredor de bolsa** registre los montos de dividendos que recibe de las empresas y los convierta en **factores de calificación tributaria**, manteniendo el historial completo y trazable.

Proyecto del ramo **Proyecto Integrado** (INACAP), basado en un requerimiento real de la empresa **nuam** — el holding que une las bolsas de Santiago, Lima y Colombia.

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white&style=flat)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.141-009688?logo=fastapi&logoColor=white&style=flat)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black&style=flat)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite&logoColor=white&style=flat)](https://vitejs.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white&style=flat)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-29-2496ED?logo=docker&logoColor=white&style=flat)](https://www.docker.com/)

**Sitio del proyecto:** [factoruno.t420.dev](https://factoruno.t420.dev)

## Stack tecnológico

| Capa | Tecnología | Rol |
|------|-----------|-----|
| Frontend | React + Vite | Grilla, formularios y carga de archivos |
| Backend | Python + FastAPI | API REST y reglas de negocio |
| Base de datos | SQLite | Almacenamiento local |
| Deploy | Docker / Compose | Ambiente reproducible |

## Características

- Mantenedor de calificaciones con filtros por mercado, origen y período
- Ingreso manual de los 29 campos de montos, o carga masiva por CSV con vista previa
- Cálculo automático de factores (redondeo a 8 decimales; suma de la base 8–19 ≤ 1)
- Prioridad del corredor: la información local nunca altera la de la Bolsa
- Auditoría de ingreso, modificación y eliminación

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

```
factoruno/
├── backend/
│   ├── app/       →  API FastAPI, reglas de negocio y datos
│   └── tests/     →  pruebas automatizadas
├── frontend/
│   └── src/       →  interfaz React (grilla, formularios, carga CSV)
├── docker-compose.yml
└── README.md
```

## Pruebas

```bash
cd backend
pytest tests/ -q
```

## Licencia

Proyecto académico — ramo Proyecto Integrado, INACAP 2026.
