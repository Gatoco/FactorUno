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
| T10 | README/help + commits work-unit + push | S3 | inline | ✅ hecho |
| T11 | Informe Ev2 ensamblado (rúbrica como títulos, gráficos) | S7, S8 + todo | inline | ✅ hecho |
| T12 | Documento único de entrega con links | S9 | inline | ✅ hecho |
| T13 | Re-despliegue AWS + verificación pública + datos (EIP/correo) | S9 | inline | ✅ hecho |
| T14 | Video demo | S9 | **usuario** | ⬜ |

## Log

**L1 (2026-10-15, usuario, verbatim):** "mañana está la entrega, revisa tu el ambiente todo lo que necesites, saca screenshot, usa playwrright, estoy en el grupo t420, ve viendo todo, el video nomas tiene que quedar pendiente que eso lo iré a hacer yop"

**L2 (2026-10-15, exploración AAI):** Tarea Ev2 (id 1501167) en AAI: entrega bajo **Grupo t420**; Moodle sin fecha límite configurada y sin envío online (confirmar canal con el profe). Rúbrica oficial completa (con niveles Destacado/Habilitado/En desarrollo/No logrado) extraída y guardada en el vault: `Ev2 — Rúbrica oficial (AAI).md`. Capturas en `Evidencias AAI/`. AWS: lab desmontado ayer; re-despliegue reproducible en ~5 min con `inacap_aai/scripts/userdata.sh`. Prioridad: Seguridad 30 pts → Pruebas 20 pts → no estructurada 5 → planificación/arquitectura 20 → informe → entrega → nube.

**L3 (2026-10-15, evidencia de ejecución T2–T9):** Tests: **98 passed** (62 reglas + 16 auth + 9 servicio + 8 aws_ext + 3 rendimiento), cobertura **96%** (`pytest --cov=app --cov-report=term-missing`). Rendimiento 500 filas: carga CSV 0,11 s · listado 0,03 s · cálculo 0,004 s. Auth: bcrypt + JWT HS256 (secreto por env), roles admin/analista/consulta con matriz en API y UI; auditoría con usuario real; login UI compilado (vite build OK). Hardening: CORS por env, headers de seguridad + CSP en nginx, `.env.example`, `.env` en `.gitignore`. AWS: `aws_ext.py` — espejo de auditoría a DynamoDB y exportes JSON/CSV a S3 con URL firmada; degradación limpia sin variables de entorno (503 en `/api/exportar` sin bucket). Docs: `docs/informe/01-planificacion.md`, `02-arquitectura.md`; `docs/seguridad/01-amenazas-y-mitigacion.md`, `02-codificacion-segura.md`. Archivos: `backend/app/auth.py`, `aws_ext.py`, `backend/tests/` (5 archivos), `frontend/src/{api.js,App.jsx,styles.css}`.

**L4 (2026-10-15, evidencia T10):** Commits work-unit en `main`: `83f965b` test suite (98 pruebas, 96 %) → `5d0f286` feat(security) auth+hardening+AWS → `eac3d6d` docs (informe + seguridad + ODD). Push `d2078c0..eac3d6d`. README: credenciales demo, sección Pruebas, stack actualizado. Validación local E2E: uvicorn 127.0.0.1:8000 + vite 5173; sin token → 401; login 3 roles; 7 capturas Playwright (login, grilla, detalle, auditoría, ingreso, montos, móvil) en `docs/informe/img/`. Docker local no disponible (daemon apagado, sin sudo): `docker compose config -q` OK; build completo se valida en el despliegue AWS.

**L5 (2026-10-15, evidencia T11):** Informe ensamblado `docs/informe/00-informe-ev2.md` (portada grupo t420 → solo Benjamín visible en AAI · introducción · índice con los 14 criterios evaluables · secciones 2.1.1–2.1.6 + anexo seguridad 2.1.5.11/12). 12 diagramas Mermaid renderizados a PNG (mermaid-cli) e incrustados; PDF final `FactorUno-Informe-Ev2.pdf` (42 págs, Letter, pandoc → chromium). Pendientes declarados en el informe: 2.1.3.7 retroalimentación — instrumento incluido, resultados de encuesta se anexan al cierre; 2.1.6.15 oral fuera de documento por diseño. Commit `b8ff20a` (29 archivos) pusheado.

**L6 (2026-10-15, evidencia T12–T13):** Re-despliegue AWS en el lab (sesión iniciada por el usuario): DynamoDB `factoruno-auditoria` + S3 `factoruno-exportes-848962746029` creados; SG `factoruno-web` (`sg-0b25f701ec7d06390`, 22/80/443/8000); EC2 `i-0649b616541af80bb` (t3.small, RHEL 9.8, AMI `ami-0fec1400d2a5313ec`, perfil `LabInstanceProfile`, user-data actualizado con `.env`); EIP **100.57.30.193** (`eipalloc-0091e8dd809236171`). Bootstrap ~165 s → frontend 200, sin token 401, login 3 roles, CRUD + auditoría con usuario real. **Hallazgo corregido:** `docker-compose.yml` no pasaba `FACTORUNO_DYNAMO_TABLA`/`FACTORUNO_S3_BUCKET` al contenedor (edit T6 previo a T9) → commit **`bf4bdbe`** + parche al servidor; tras recrear backend: espejo DynamoDB verificado (scan Count=1, item `INSERT#3 CENCOSUD S.A. analista`) y exportes JSON (3 336 B) y CSV (473 B) descargados por URL firmada (GET 200). T12: `Entrega Ev2 — Proyecto Integrado (links).md` + PDF (3 págs) en el vault (repo, informe PDF, correo AWS, EIP, credenciales demo; video queda pendiente del usuario).

**L7 (2026-10-15, revisión RDD nativa — slice S1):** Revisión RDD con gentle-ai v4 sobre la entrega (revisores en DeepSeek v4.1 Flash vía familia iwakura-verify; validador dirigido capturado por el transporte nativo). Linaje inicial `review-7a118751f424e69b` → recuperación `scope_changed` → sucesor `review-9aeeb783d44c0d2c` **aprobado y consumido** (acknowledge-approved; autoridad quemada). Findings corregidos (4): `R1-default-secret` (BLOCKER: secreto JWT con default publicado → ahora obligatorio por env, falla cerrado), `R1-default-credentials` (CRITICAL: seeds demo opt-in vía `FACTORUNO_SEED_DEMO`, sin passwords publicadas), `R4-1` (CRITICAL: espejo DynamoDB síncrono dentro de la transacción SQLite → cola + flush post-commit) y `R4-001` (CRITICAL: fallos reales de S3 devolvían 500 → `AlmacenamientoNoDisponible` + 503 controlado). Fixes `6864ee1` + `39bee3e` (validador dirigido: PASSED, sin regresiones) integrados a `main` como `54334ed` + `2fc9791`. **99 pruebas verdes en main**; `docker compose config` OK. Advisories registrados sin bloquear (rate-limit de login, revocación JWT, señal de pérdida del espejo, CSV parcial, cotas de dependencias). **Pendiente**: slices S2 [`5d0f286..eac3d6d`], S3 [`eac3d6d..b8ff20a`], S4 [`b8ff20a..214210f`]; re-despliegue del server con los fixes; video (usuario).
