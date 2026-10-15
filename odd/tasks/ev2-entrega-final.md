# Ev2 Proyecto Integrado — entrega final FactorUno

**Objective:** Completar los entregables de la Evaluación 2 (Sumativa) de Proyecto Integrado (TIHI43): seguridad, pruebas, base no estructurada, artefactos de planificación/arquitectura, informe con la rúbrica como índice, documento único de entrega con links y re-despliegue en AWS. Entrega: viernes 16-10-2026 (grupo t420). El video demo queda a cargo del usuario (Benjamín).
**Branch:** `main` — repo público solo-developer https://github.com/Gatoco/FactorUno; el despliegue clona `main`, así que los work-unit commits van directo a `main` (estrategia `exception-ok`, autorizada por el usuario: "ve viendo todo", entrega mañana).
**Test runner:** `pytest` desde `backend/` con `python -m pytest` (venv `.venv`).

## Specs

- **S1 — Autenticación y autorización (rúbrica 2.1.5.10, 10 pts).** El sistema define e implementa políticas authn/authz. Criterio: *"Define políticas de autenticación y autorización"* — Destacado: *"Políticas robustas, específicas y alineadas con mejores prácticas; cubren roles y perfiles."* Implementación: login con hash bcrypt, sesión JWT (HS256, expiración, secreto por env), roles `admin` / `analista` / `consulta` con matriz de permisos aplicada en API y UI; auditoría registra el usuario autenticado.
- **S2 — Amenazas y mitigación (2.1.5.11, 10 pts).** Documento de amenazas (STRIDE/OWASP) con mitigaciones implementadas. Destacado: *"Identificación exhaustiva con medidas de mitigación bien documentadas."*
- **S3 — Codificación segura (2.1.5.12, 10 pts).** Estándares documentados y aplicados: validación de entrada estricta, consultas parametrizadas, sin secretos versionados (`.env.example`), cabeceras de seguridad, CORS restringido, errores sin fugas de detalle, dependencias fijadas. Destacado: *"Estándares bien documentados, implementados y alineados a buenas prácticas."*
- **S4 — Pruebas (2.1.6.13, 10 pts).** Suite pytest: unitarias (reglas de negocio), integrales (API con httpx/TestClient, incluyendo auth y matriz de roles), rendimiento (carga masiva CSV medida contra umbral). Resultados documentados. Destacado: *"Plan de pruebas completo y ejecutado, con resultados bien documentados."*
- **S5 — Herramientas de prueba (2.1.6.14, 5 pts).** Documento de plan de pruebas: herramientas automatizadas (pytest, coverage, httpx, script de carga) y manuales (checklist QA manual ejecutado). Destacado: *"Uso balanceado y efectivo de herramientas automatizadas y manuales."*
- **S6 — Base no estructurada (2.1.4.9, 5 pts).** Además de SQLite (estructurada): Amazon DynamoDB para historial de auditoría y Amazon S3 para CSV originales/exportes JSON, integrados desde la app (boto3, degradación limpia si no están configurados). Destacado: *"Uso eficaz de bases estructuradas y no estructuradas con ejemplos funcionales."*
- **S7 — Planificación (2.1.1.1, 2.1.1.2, 10 pts).** Secciones del informe: actividades y fases según metodología, cronograma con plazos y responsables, dependencias y prioridades entre tareas.
- **S8 — Arquitectura (2.1.2.3, 2.1.2.4, 10 pts).** Vistas 4+1 (lógica, desarrollo, procesos, física, escenarios) y tecnologías de infraestructura justificadas (RHEL 9, EC2 t3.small, Elastic IP, Docker Compose, FastAPI, React/Vite, SQLite, DynamoDB/S3).
- **S9 — Entrega (prof, video 02-10 → transcripción en vault).** Un documento con links: repo GitHub, video demo, informe, correo de la cuenta AWS (`benjamin.cifuentes07@inacapmail.cl`) y IP elástica. La solución *"sí o sí"* en la nube, revisable por el profesor levantando el lab con la cuenta del alumno. El video lo graba el usuario: todos los integrantes (grupo t420) hablando y con cara, demostrando la funcionalidad (~80%).
- **S10 — Fuera de alcance.** El video demo no se produce aquí (tarea del usuario). La app debe quedar funcional y desplegada al momento de entregar.

## Tasks

| ID | Tarea | Specs | Ruta | Estado |
|---|---|---|---|---|
| T1 | Feature doc + espejo Engram | — | inline | ✅ hecho |
| T2 | Borradores informe: planificación + arquitectura (con diagramas) | S7, S8 | delegado | ✅ hecho |
| T3 | Tests unitarios `reglas.py` (pytest) | S4 | delegado | ✅ hecho |
| T4 | Backend authn/authz: `auth.py`, `db.py`, `servicio.py`, `main.py`, seed usuarios | S1 | inline | ✅ hecho |
| T5 | Frontend: login + token/roles en `api.js` y `App.jsx` | S1 | inline | ✅ hecho |
| T6 | Hardening: compose/nginx/env + requirements + `.env.example` | S3 | inline | ✅ hecho |
| T7 | Tests integrales + rendimiento + resultados documentados | S4, S5 | inline | ✅ hecho |
| T8 | Docs seguridad: STRIDE, políticas authn/authz, estándares | S2, S3 | inline | ✅ hecho |
| T9 | DynamoDB + S3: integración + ejemplo funcional | S6 | inline | ✅ hecho |
| T10 | README/help + commits work-unit + push | S3 | inline | ⬜ |
| T11 | Informe Ev2 ensamblado (rúbrica como títulos, gráficos) | S7, S8 + todo | inline | ⬜ |
| T12 | Documento único de entrega con links | S9 | inline | ⬜ |
| T13 | Re-despliegue AWS + verificación pública + datos (EIP/correo) | S9 | inline | ⬜ |
| T14 | Video demo | S9 | **usuario** | ⬜ |

## Log

**L1 (2026-10-15, usuario, verbatim):** "mañana está la entrega, revisa tu el ambiente todo lo que necesites, saca screenshot, usa playwrright, estoy en el grupo t420, ve viendo todo, el video nomas tiene que quedar pendiente que eso lo iré a hacer yop"

**L2 (2026-10-15, exploración AAI):** Tarea Ev2 (id 1501167) en AAI: entrega bajo **Grupo t420**; Moodle sin fecha límite configurada y sin envío online (confirmar canal con el profe). Rúbrica oficial completa (con niveles Destacado/Habilitado/En desarrollo/No logrado) extraída y guardada en el vault: `Ev2 — Rúbrica oficial (AAI).md`. Capturas en `Evidencias AAI/`. AWS: lab desmontado ayer; re-despliegue reproducible en ~5 min con `inacap_aai/scripts/userdata.sh`. Prioridad: Seguridad 30 pts → Pruebas 20 pts → no estructurada 5 → planificación/arquitectura 20 → informe → entrega → nube.

**L3 (2026-10-15, evidencia de ejecución T2–T9):** Tests: **98 passed** (62 reglas + 16 auth + 9 servicio + 8 aws_ext + 3 rendimiento), cobertura **96%** (`pytest --cov=app --cov-report=term-missing`). Rendimiento 500 filas: carga CSV 0,11 s · listado 0,03 s · cálculo 0,004 s. Auth: bcrypt + JWT HS256 (secreto por env), roles admin/analista/consulta con matriz en API y UI; auditoría con usuario real; login UI compilado (vite build OK). Hardening: CORS por env, headers de seguridad + CSP en nginx, `.env.example`, `.env` en `.gitignore`. AWS: `aws_ext.py` — espejo de auditoría a DynamoDB y exportes JSON/CSV a S3 con URL firmada; degradación limpia sin variables de entorno (503 en `/api/exportar` sin bucket). Docs: `docs/informe/01-planificacion.md`, `02-arquitectura.md`; `docs/seguridad/01-amenazas-y-mitigacion.md`, `02-codificacion-segura.md`. Archivos: `backend/app/auth.py`, `aws_ext.py`, `backend/tests/` (5 archivos), `frontend/src/{api.js,App.jsx,styles.css}`.
