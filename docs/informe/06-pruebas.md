## 2.1.6.13 Pruebas unitarias, integrales y de rendimiento

El plan de pruebas cubre los tres niveles solicitados por la rúbrica, con resultados ejecutados y verificables.

| Nivel | Objetivo | Alcance | Resultado |
|-------|----------|---------|-----------|
| Unitarias | Reglas de negocio puras | `app/reglas.py`: redondeo a 8 decimales, cálculo y validación de factores, normalización de fecha, tipo de sociedad, mapeo de filas CSV | **62 casos — 100% OK** |
| Integrales | API completa con autenticación y base real (SQLite temporal) | Login y matriz de roles (16), flujo CRUD completo, cálculo automático, filtros, carga CSV (idempotencia y errores por fila), auditoría, exportes S3 (9) y espejado DynamoDB | **34 casos — 100% OK** |
| Rendimiento | Tiempos sobre volumen representativo | Carga masiva CSV de **500 registros**, listado de 500 registros y cálculo de factores | **0,11 s / 0,03 s / 0,004 s** |

**Total: 99 pruebas automatizadas, 100% exitosas.**

### Resultados por archivo de prueba

| Archivo | Casos | Qué verifica |
|---------|:-----:|--------------|
| `tests/test_reglas.py` | 62 | Funciones puras de reglas de negocio (parametrizadas por caso). |
| `tests/test_auth.py` | 16 | `401` sin token / token inválido, login por rol, matriz de permisos completa, auditoría con usuario real. |
| `tests/test_servicio.py` | 9 | Flujo integral CRUD vía API, recálculo de factores, filtros, carga CSV idempotente, errores por fila, auditoría de escrituras. |
| `tests/test_aws_ext.py` | 9 | Espejo de auditoría a DynamoDB (tipos y contenido), exportes JSON/CSV a S3 (URL firmada), `503` sin bucket, `403` por rol. |
| `tests/test_perf.py` | 3 | Umbrales de tiempo de carga masiva, listado y cálculo. |

### Cobertura de código

Ejecutada con `pytest-cov` sobre `app/`:

| Módulo | Cobertura |
|--------|:---------:|
| `reglas.py` | 100% |
| `servicio.py` | 97% |
| `main.py` | 96% |
| `auth.py` | 92% |
| `db.py` | 90% |
| `aws_ext.py` | 82% |
| **Total** | **94%** |

### Rendimiento medido (pytest + `-s`)

| Escenario | Volumen | Resultado | Umbral del test |
|-----------|---------|-----------|-----------------|
| Carga masiva CSV | 500 registros | **0,11 s** | < 15 s |
| Listado con filtros | 500 registros | **0,03 s** | < 5 s |
| Cálculo de factores | 29 montos | **0,004 s** | < 2 s |

### Cómo reproducir

```bash
cd backend
.venv/bin/python -m pytest tests/ -q                          # 99 pruebas
.venv/bin/python -m pytest tests/ -q --cov=app --cov-report=term-missing
.venv/bin/python -m pytest tests/test_perf.py -s              # tiempos impresos
```

Las pruebas integrales usan **SQLite temporal** (`tmp_path`) por cada test: no tocan datos reales ni requieren credenciales AWS (las integraciones AWS se prueban con clientes simulados).

## 2.1.6.14 Uso de herramientas automatizadas y manuales

La estrategia combina herramientas **automatizadas** (regresión continua) y **manuales** (juicio funcional y de usabilidad), de forma balanceada:

### Herramientas automatizadas

| Herramienta | Uso en el proyecto |
|-------------|--------------------|
| **pytest** | Framework de pruebas: 99 casos (unitarias, integrales y rendimiento). |
| **pytest-cov** | Medición de cobertura de código (94%). |
| **httpx / TestClient** | Cliente HTTP de las pruebas integrales contra la API real (con autenticación). |
| **boto3 (mockeado)** | Verificación del espejo DynamoDB y de los exportes S3 sin consumir AWS. |
| **Script de rendimiento** | Generador de 500 registros CSV con umbrales de tiempo como aserción. |
| **Playwright (script de capturas)** | Prueba de humo E2E real sobre la interfaz: login → grilla → detalle → auditoría → modales → vista móvil (genera las capturas de la sección 2.1.3). |

### Herramientas manuales

| Actividad manual | Procedimiento | Resultado |
|------------------|---------------|-----------|
| Checklist funcional | Recorrido guiado del flujo principal en la interfaz real | Ejecutado — flujo completo OK |
| Verificación de la matriz de roles en UI | Sesión con rol `consulta` (solo lectura) vs `analista` | Ejecutado — acciones ocultas/deshabilitadas y API responde `403` |
| Revisión visual y responsiva | Revisión de consistencia y captura en viewport móvil 390 × 962 | Ejecutado — sin quiebres de layout |
| Revisión cruzada de errores | Envío de datos inválidos (fecha, tipo de sociedad, suma de factores > 1) | Ejecutado — mensajes claros por fila/campo |

### Justificación del balance

Lo automatizado cubre lo **determinista y repetible** (reglas, API, permisos, tiempos): es la red de seguridad que se ejecuta completa antes de cada entrega de trabajo. Lo manual cubre lo que la herramienta no juzga: **claridad visual, flujo de uso y comprensión de mensajes**, además de servir de preparación de la demostración en video. Cada hallazgo manual relevante se convirtió en un caso automatizado cuando fue posible (por ejemplo, la matriz de roles y la idempotencia de la carga CSV).
