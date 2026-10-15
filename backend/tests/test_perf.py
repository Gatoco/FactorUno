"""Performance tests (rúbrica 2.1.6.13): carga masiva, listado y cálculo.

Mide con time.perf_counter sobre la API real (TestClient) y fija límites
holgados para evitar flakiness en máquinas lentas. Los tiempos observados
se imprimen para usarlos como evidencia en el informe (correr con -s).
"""
import time

import pytest
from fastapi.testclient import TestClient

from app import db
from app.main import app

FILAS = 500
LIMITE_CARGA_S = 15.0
LIMITE_LISTADO_S = 5.0
LIMITE_CALCULO_S = 2.0

ANALISTA = {"usuario": "analista", "password": "Analista1234!"}

CABECERA = (
    "ejercicio,mercado,instrumento,fecha,secuencia,numero_dividendo,"
    "tipo_sociedad,valor_historico,monto_8,monto_9"
)


def _csv_masivo(n: int) -> str:
    lineas = [CABECERA]
    for i in range(n):
        lineas.append(
            f"{2020 + i % 5},N,PERF_{i:05d},2024-01-{i % 28 + 1:02d},"
            f"1,0,A,{1000 + i},30,70"
        )
    return "\n".join(lineas) + "\n"


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test_perf.db")
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def headers(client):
    r = client.post("/api/auth/login", json=ANALISTA)
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def _cargar(client, headers) -> float:
    t0 = time.perf_counter()
    r = client.post("/api/carga",
                    files={"archivo": ("perf.csv", _csv_masivo(FILAS))},
                    headers=headers)
    t = time.perf_counter() - t0
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["insertados"] == FILAS, body
    assert body["errores"] == []
    return t


def test_carga_masiva_de_500_registros(client, headers):
    t = _cargar(client, headers)
    print(f"\n[perf] carga CSV de {FILAS} registros: {t:.2f}s")
    assert t < LIMITE_CARGA_S


def test_listado_de_500_registros(client, headers):
    _cargar(client, headers)
    t0 = time.perf_counter()
    r = client.get("/api/calificaciones", params={"mercado": "N"},
                   headers=headers)
    t = time.perf_counter() - t0
    assert r.status_code == 200
    assert len(r.json()) == FILAS
    print(f"[perf] listado de {FILAS} registros: {t:.3f}s")
    assert t < LIMITE_LISTADO_S


def test_calculo_de_factores_sobre_500_registros(client, headers):
    _cargar(client, headers)
    rid = client.get("/api/calificaciones", params={"mercado": "N"},
                     headers=headers).json()[0]["id"]
    t0 = time.perf_counter()
    r = client.post(f"/api/calificaciones/{rid}/calcular", headers=headers)
    t = time.perf_counter() - t0
    assert r.status_code == 200, r.text
    print(f"[perf] cálculo de factores de un registro: {t:.3f}s")
    assert t < LIMITE_CALCULO_S
