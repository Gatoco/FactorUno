"""Integration tests for authentication and authorization (rúbrica 2.1.5.10).

Public interface under test:
- POST /api/auth/login  -> {access_token, token_type, usuario, rol}
- GET  /api/auth/me     -> current authenticated user
- All /api/* endpoints require a Bearer token; write operations require
  role admin or analista; auditoria is not visible to consulta.
"""
import pytest
from fastapi.testclient import TestClient

from app import db
from app.main import app

ADMIN = {"usuario": "admin", "password": "Admin1234!"}
ANALISTA = {"usuario": "analista", "password": "Analista1234!"}
CONSULTA = {"usuario": "consulta", "password": "Consulta1234!"}

CALIFICACION = {
    "ejercicio": 2024,
    "mercado": "N",
    "instrumento": "TEST_AUTH",
    "fecha_pago": "2024-01-15",
    "secuencia": 1,
    "numero_dividendo": 0,
    "tipo_sociedad": "A",
    "montos": {8: 1.0},
}


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "test_auth.db")
    with TestClient(app) as c:
        yield c


def _login(client, credenciales):
    return client.post("/api/auth/login", json=credenciales)


def _headers(client, credenciales):
    r = _login(client, credenciales)
    assert r.status_code == 200, r.text
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


# --- authentication -------------------------------------------------------


def test_listar_sin_token_retorna_401(client):
    assert client.get("/api/calificaciones").status_code == 401


def test_login_con_password_incorrecta_retorna_401(client):
    r = _login(client, {"usuario": "admin", "password": "no-es-la-clave"})
    assert r.status_code == 401


def test_login_con_usuario_desconocido_retorna_401(client):
    r = _login(client, {"usuario": "nadie", "password": "x"})
    assert r.status_code == 401


@pytest.mark.parametrize("credenciales, rol", [
    (ADMIN, "admin"),
    (ANALISTA, "analista"),
    (CONSULTA, "consulta"),
])
def test_login_valido_devuelve_token_usuario_y_rol(client, credenciales, rol):
    r = _login(client, credenciales)
    assert r.status_code == 200
    body = r.json()
    assert body["token_type"] == "bearer"
    assert body["rol"] == rol
    assert body["usuario"] == credenciales["usuario"]
    assert body["access_token"]


def test_me_devuelve_usuario_autenticado(client):
    r = client.get("/api/auth/me", headers=_headers(client, ADMIN))
    assert r.status_code == 200
    assert r.json() == {"usuario": "admin", "rol": "admin"}


def test_token_invalido_retorna_401(client):
    r = client.get(
        "/api/calificaciones",
        headers={"Authorization": "Bearer token.falso.invalido"},
    )
    assert r.status_code == 401


# --- authorization by role ------------------------------------------------


def test_consulta_puede_listar_y_obtener(client):
    headers = _headers(client, CONSULTA)
    assert client.get("/api/calificaciones", headers=headers).status_code == 200


def test_consulta_no_puede_crear(client):
    r = client.post("/api/calificaciones", json=CALIFICACION,
                    headers=_headers(client, CONSULTA))
    assert r.status_code == 403


def test_consulta_no_puede_eliminar(client):
    r = client.delete("/api/calificaciones/1",
                      headers=_headers(client, CONSULTA))
    assert r.status_code == 403


def test_consulta_no_puede_ver_auditoria(client):
    r = client.get("/api/auditoria", headers=_headers(client, CONSULTA))
    assert r.status_code == 403


def test_consulta_no_puede_cargar_csv(client):
    r = client.post("/api/carga", files={"archivo": ("x.csv", "a,b\n1,2\n")},
                    headers=_headers(client, CONSULTA))
    assert r.status_code == 403


def test_analista_puede_crear_calcular_y_eliminar(client):
    headers = _headers(client, ANALISTA)
    r = client.post("/api/calificaciones", json=CALIFICACION, headers=headers)
    assert r.status_code == 201, r.text
    rid = r.json()["id"]
    assert client.post(f"/api/calificaciones/{rid}/calcular",
                       headers=headers).status_code == 200
    assert client.delete(f"/api/calificaciones/{rid}",
                         headers=headers).status_code == 204


def test_crear_sin_token_retorna_401(client):
    r = client.post("/api/calificaciones", json=CALIFICACION)
    assert r.status_code == 401


def test_admin_ve_auditoria_y_registra_usuario_real(client):
    headers_a = _headers(client, ANALISTA)
    r = client.post("/api/calificaciones", json=CALIFICACION, headers=headers_a)
    assert r.status_code == 201, r.text

    headers_adm = _headers(client, ADMIN)
    r = client.get("/api/auditoria", headers=headers_adm)
    assert r.status_code == 200
    registro = next(e for e in r.json() if e["accion"] == "INSERT")
    assert registro["usuario"] == "analista"
