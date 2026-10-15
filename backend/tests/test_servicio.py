"""Integration tests for the business flow through the public API (rúbrica 2.1.6.13).

Exercises the same HTTP surface the React frontend uses: full CRUD,
automatic factor calculation, CSV bulk load (upsert by business key) and
the audit trail.
"""
import pytest
from fastapi.testclient import TestClient

from app import db
from app.main import app

ANALISTA = {"usuario": "analista", "password": "Analista1234!"}

CABECERA_CSV = (
    "ejercicio,mercado,instrumento,fecha,secuencia,numero_dividendo,"
    "tipo_sociedad,valor_historico,monto_8,monto_9,isfut"
)


def _csv(*filas: str) -> str:
    return "\n".join([CABECERA_CSV, *filas]) + "\n"


def _fila_csv(instrumento: str, valor: int = 1000) -> str:
    return f"2024,N,{instrumento},15-01-2024,1,0,A,{valor},30,70"


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test_servicio.db")
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def headers(client):
    r = client.post("/api/auth/login", json=ANALISTA)
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def _nueva(**campos):
    base = {
        "ejercicio": 2024,
        "mercado": "N",
        "instrumento": "TEST",
        "fecha_pago": "2024-01-15",
        "secuencia": 1,
        "numero_dividendo": 0,
        "tipo_sociedad": "A",
        "montos": {},
    }
    base.update(campos)
    return base


# --- flujo CRUD completo ---------------------------------------------------


def test_flujo_crud_completo(client, headers):
    r = client.post("/api/calificaciones",
                    json=_nueva(instrumento="FLUJO", montos={"8": 30.0, "9": 70.0}),
                    headers=headers)
    assert r.status_code == 201, r.text
    creado = r.json()
    rid = creado["id"]
    assert creado["instrumento"] == "FLUJO"
    assert creado["montos"] == {"8": 30.0, "9": 70.0}

    assert any(c["id"] == rid for c in client.get(
        "/api/calificaciones", headers=headers).json())

    r = client.put(f"/api/calificaciones/{rid}",
                   json={"instrumento": "FLUJO_2"}, headers=headers)
    assert r.status_code == 200, r.text
    modificado = r.json()
    assert modificado["instrumento"] == "FLUJO_2"
    assert modificado["mercado"] == "N"  # no enviado -> no se toca

    assert client.delete(f"/api/calificaciones/{rid}",
                         headers=headers).status_code == 204
    assert client.get(f"/api/calificaciones/{rid}",
                      headers=headers).status_code == 404


def test_calculo_automatico_con_redondeo_8_decimales(client, headers):
    r = client.post("/api/calificaciones",
                    json=_nueva(instrumento="REDONDEO",
                                montos={"8": 1.0, "9": 2.0}),
                    headers=headers)
    assert r.status_code == 201, r.text
    factores = r.json()["factores"]
    assert factores["8"] == 0.33333333
    assert factores["9"] == 0.66666667
    assert len(factores) == 30  # columnas 8..37


def test_modificar_montos_recalcula_factores(client, headers):
    r = client.post("/api/calificaciones",
                    json=_nueva(instrumento="RECALC",
                                montos={"8": 30.0, "9": 70.0}),
                    headers=headers)
    rid = r.json()["id"]
    assert r.json()["factores"]["8"] == 0.3

    r = client.put(f"/api/calificaciones/{rid}",
                   json={"montos": {"8": 50.0, "9": 50.0}}, headers=headers)
    assert r.status_code == 200, r.text
    factores = r.json()["factores"]
    assert factores["8"] == 0.5
    assert factores["9"] == 0.5


def test_endpoint_calcular_recalcula_y_audita(client, headers):
    r = client.post("/api/calificaciones",
                    json=_nueva(instrumento="BOTON", montos={"8": 10.0, "9": 90.0}),
                    headers=headers)
    rid = r.json()["id"]

    r = client.post(f"/api/calificaciones/{rid}/calcular", headers=headers)
    assert r.status_code == 200, r.text
    assert r.json()["factores"]["8"] == 0.1

    eventos = client.get("/api/auditoria", headers=headers).json()
    calc = next(e for e in eventos if e["accion"] == "CALCULAR")
    assert calc["registro_id"] == rid
    assert calc["usuario"] == "analista"


# --- filtros del listado ---------------------------------------------------


def test_filtros_por_mercado_origen_y_periodo(client, headers):
    for campos in (
        _nueva(instrumento="F1", mercado="N", ejercicio=2024),
        _nueva(instrumento="F2", mercado="N", ejercicio=2023),
        _nueva(instrumento="F3", mercado="R", ejercicio=2024),
        _nueva(instrumento="F4", mercado="N", ejercicio=2024, origen="entidad"),
    ):
        assert client.post("/api/calificaciones", json=campos,
                           headers=headers).status_code == 201

    def instrumentos(**params):
        r = client.get("/api/calificaciones", params=params, headers=headers)
        assert r.status_code == 200
        return sorted(c["instrumento"] for c in r.json())

    assert instrumentos(mercado="R") == ["F3"]
    assert instrumentos(periodo=2023) == ["F2"]
    assert instrumentos(origen="entidad") == ["F4"]
    assert instrumentos(mercado="N", periodo=2024) == ["F1", "F4"]


# --- carga masiva CSV ------------------------------------------------------


def test_carga_csv_inserta_y_es_idempotente_por_llave(client, headers):
    contenido = _csv(
        _fila_csv("CSV_1", 100),
        _fila_csv("CSV_2", 200),
        _fila_csv("CSV_3", 300),
    )
    r = client.post("/api/carga", files={"archivo": ("carga.csv", contenido)},
                    headers=headers)
    assert r.status_code == 200, r.text
    assert r.json() == {"insertados": 3, "actualizados": 0, "errores": []}

    # Segunda carga con la misma llave y valor nuevo -> actualiza, no duplica.
    contenido2 = _csv(
        _fila_csv("CSV_1", 999),
        _fila_csv("CSV_2", 200),
        _fila_csv("CSV_3", 300),
    )
    r = client.post("/api/carga", files={"archivo": ("carga.csv", contenido2)},
                    headers=headers)
    assert r.json() == {"insertados": 0, "actualizados": 3, "errores": []}

    registros = client.get("/api/calificaciones", params={"mercado": "N"},
                           headers=headers).json()
    assert len(registros) == 3
    csv_1 = next(c for c in registros if c["instrumento"] == "CSV_1")
    assert csv_1["valor_historico"] == 999

    eventos = client.get("/api/auditoria", headers=headers).json()
    assert [e["accion"] for e in eventos].count("CARGA") == 6
    assert all(e["usuario"] == "analista" for e in eventos if e["accion"] == "CARGA")


def test_carga_csv_reporta_filas_invalidas(client, headers):
    contenido = _csv(
        _fila_csv("OK_1"),
        "2024,N,MALA,15-01-2024,1,0,B,100,30,70",  # tipo_sociedad inválido
        "2024,N,MALA_FECHA,no-es-fecha,1,0,A,100,30,70",
    )
    r = client.post("/api/carga", files={"archivo": ("carga.csv", contenido)},
                    headers=headers)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["insertados"] == 1
    assert len(body["errores"]) == 2
    assert "fila 3" in body["errores"][0]
    assert "fila 4" in body["errores"][1]


def test_carga_csv_con_tipo_invalido_retorna_400(client, headers):
    r = client.post("/api/carga?tipo=otro",
                    files={"archivo": ("x.csv", _csv(_fila_csv("X")))},
                    headers=headers)
    assert r.status_code == 400


# --- auditoría del flujo ---------------------------------------------------


def test_auditoria_registra_insert_update_delete(client, headers):
    r = client.post("/api/calificaciones", json=_nueva(instrumento="AUD"),
                    headers=headers)
    rid = r.json()["id"]
    client.put(f"/api/calificaciones/{rid}", json={"instrumento": "AUD_2"},
               headers=headers)
    client.delete(f"/api/calificaciones/{rid}", headers=headers)

    eventos = client.get("/api/auditoria", headers=headers).json()
    acciones = [e["accion"] for e in eventos]
    assert {"INSERT", "UPDATE", "DELETE"} <= set(acciones)
    assert all(e["usuario"] == "analista" for e in eventos
               if e["registro_id"] == rid)
