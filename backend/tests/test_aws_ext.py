"""Tests de las integraciones con almacenamiento no estructurado (rúbrica 2.1.4.9).

Cubren el espejo de auditoría hacia DynamoDB y la exportación de respaldos
hacia S3 usando clientes falsos; ningún test toca AWS real.
"""
import json

import pytest
from fastapi.testclient import TestClient

from app import aws_ext, db
from app.main import app

ANALISTA = {"usuario": "analista", "password": "Analista1234!"}
CONSULTA = {"usuario": "consulta", "password": "Consulta1234!"}


class FakeDynamo:
    def __init__(self):
        self.items = []

    def put_item(self, TableName, Item):
        self.items.append((TableName, Item))
        return {}


class FakeS3:
    def __init__(self):
        self.objetos = []

    def put_object(self, Bucket, Key, Body, ContentType):
        self.objetos.append({"bucket": Bucket, "key": Key,
                             "body": Body, "type": ContentType})
        return {}

    def generate_presigned_url(self, op, Params, ExpiresIn):
        return (f"https://fake-s3.local/{Params['Bucket']}/{Params['Key']}"
                f"?exp={ExpiresIn}")


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test_aws.db")
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def headers(client):
    r = client.post("/api/auth/login", json=ANALISTA)
    assert r.status_code == 200, r.text
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def _crear(client, headers, instrumento="AWS_1"):
    r = client.post("/api/calificaciones", json={
        "ejercicio": 2024, "mercado": "N", "instrumento": instrumento,
        "fecha_pago": "2024-01-15", "secuencia": 1, "numero_dividendo": 0,
        "tipo_sociedad": "A", "montos": {"8": 30.0, "9": 70.0},
    }, headers=headers)
    assert r.status_code == 201, r.text
    return r.json()


# --- DynamoDB: espejo de auditoría -----------------------------------------


def test_espejo_deshabilitado_devuelve_false(monkeypatch):
    monkeypatch.delenv("FACTORUNO_DYNAMO_TABLA", raising=False)
    assert aws_ext.espejar_auditoria({"accion": "INSERT", "usuario": "x"}) is False


def test_espejo_configurado_envia_item(monkeypatch):
    monkeypatch.setenv("FACTORUNO_DYNAMO_TABLA", "factoruno-auditoria")
    fake = FakeDynamo()
    monkeypatch.setattr(aws_ext, "_cliente_dynamo", lambda: fake)

    ok = aws_ext.espejar_auditoria({
        "accion": "INSERT", "registro_id": 7, "detalle": "alta",
        "usuario": "analista", "fecha": "2026-10-15 10:00:00",
    })
    assert ok is True
    tabla, item = fake.items[0]
    assert tabla == "factoruno-auditoria"
    assert item["accion"]["S"] == "INSERT"
    assert item["usuario"]["S"] == "analista"
    assert item["registro_id"]["N"] == "7"


def test_auditoria_espeja_al_crear(client, headers, monkeypatch):
    monkeypatch.setenv("FACTORUNO_DYNAMO_TABLA", "factoruno-auditoria")
    fake = FakeDynamo()
    monkeypatch.setattr(aws_ext, "_cliente_dynamo", lambda: fake)

    _crear(client, headers)
    acciones = [item["accion"]["S"] for _, item in fake.items]
    assert "INSERT" in acciones
    assert all(item["usuario"]["S"] == "analista" for _, item in fake.items)


# --- S3: exportación de respaldos ------------------------------------------


def test_exportar_sin_configurar_retorna_503(client, headers, monkeypatch):
    monkeypatch.delenv("FACTORUNO_S3_BUCKET", raising=False)
    r = client.get("/api/exportar", headers=headers)
    assert r.status_code == 503


def test_exportar_formato_invalido_retorna_400(client, headers):
    r = client.get("/api/exportar", params={"formato": "xml"}, headers=headers)
    assert r.status_code == 400


def test_exportar_como_consulta_retorna_403(client):
    r = client.post("/api/auth/login", json=CONSULTA)
    headers = {"Authorization": f"Bearer {r.json()['access_token']}"}
    assert client.get("/api/exportar", headers=headers).status_code == 403


def test_exportar_json_sube_a_s3_con_url_firmada(client, headers, monkeypatch):
    monkeypatch.setenv("FACTORUNO_S3_BUCKET", "factoruno-respaldos")
    fake = FakeS3()
    monkeypatch.setattr(aws_ext, "_cliente_s3", lambda: fake)

    _crear(client, headers, instrumento="EXPORT")
    r = client.get("/api/exportar", params={"formato": "json"}, headers=headers)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body["bucket"] == "factoruno-respaldos"
    assert body["clave"].startswith("factoruno-") and body["clave"].endswith(".json")
    assert "factoruno-respaldos" in body["url_firmada"]

    objeto = fake.objetos[0]
    assert objeto["type"] == "application/json"
    payload = json.loads(objeto["body"])
    registro = next(x for x in payload["registros"] if x["instrumento"] == "EXPORT")
    assert registro["montos"] == {"8": 30.0, "9": 70.0}
    assert payload["auditoria"]


def test_exportar_csv_sube_a_s3(client, headers, monkeypatch):
    monkeypatch.setenv("FACTORUNO_S3_BUCKET", "factoruno-respaldos")
    fake = FakeS3()
    monkeypatch.setattr(aws_ext, "_cliente_s3", lambda: fake)

    _crear(client, headers, instrumento="EXPORT_CSV")
    r = client.get("/api/exportar", params={"formato": "csv"}, headers=headers)
    assert r.status_code == 200, r.text
    cuerpo = fake.objetos[0]["body"].decode("utf-8")
    assert cuerpo.startswith("id,ejercicio,mercado,instrumento")
    assert "EXPORT_CSV" in cuerpo
    assert fake.objetos[0]["type"] == "text/csv"


def test_exportar_error_de_s3_retorna_503(client, headers, monkeypatch):
    """Un fallo real de S3 (no configuración) se traduce a 503 controlado."""
    monkeypatch.setenv("FACTORUNO_S3_BUCKET", "factoruno-respaldos")

    class FakeS3Roto(FakeS3):
        def put_object(self, Bucket, Key, Body, ContentType):
            raise RuntimeError("s3 no disponible")

    monkeypatch.setattr(aws_ext, "_cliente_s3", lambda: FakeS3Roto())

    _crear(client, headers, instrumento="EXPORT_FAIL")
    r = client.get("/api/exportar", params={"formato": "json"}, headers=headers)
    assert r.status_code == 503, r.text
