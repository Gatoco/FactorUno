"""Autenticacion (JWT + bcrypt) y autorizacion por roles (rubrica 2.1.5.10).

Politica de acceso:
- consulta: solo lectura (GET /api/calificaciones y /api/calificaciones/{id}).
- analista: lectura + escritura (crear/modificar/eliminar/calcular/carga).
- admin: todo lo anterior + consulta de la auditoria.
"""
import os
import time

import bcrypt
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt.exceptions import PyJWTError

from .db import get_conn

SECRET = os.environ.get("FACTORUNO_SECRET", "")
if not SECRET:
    raise RuntimeError(
        "FACTORUNO_SECRET debe estar definido (clave HS256 para los tokens JWT); "
        "no hay valor por defecto. Genera uno con 'openssl rand -hex 32' "
        "y exportalo antes de iniciar el servicio."
    )
ALGORITHM = "HS256"
TOKEN_HORAS = int(os.environ.get("FACTORUNO_TOKEN_HORAS", "8"))

# usuario -> variable de entorno que debe contener su password al sembrar.
# Sin valores por defecto publicados: sin la variable, el usuario no se crea.
USUARIOS_SEED = {
    "admin": "FACTORUNO_ADMIN_PASSWORD",
    "analista": "FACTORUNO_ANALISTA_PASSWORD",
    "consulta": "FACTORUNO_CONSULTA_PASSWORD",
}


def seed_demo_activo() -> bool:
    """Indica si el sembrado de usuarios demo esta habilitado (FACTORUNO_SEED_DEMO)."""
    valor = os.environ.get("FACTORUNO_SEED_DEMO", "")
    return valor.strip().lower() in ("1", "true", "si", "sí")

_bearer = HTTPBearer(auto_error=False)


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, password_hash: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))
    except ValueError:
        return False


def autenticar(usuario: str, password: str) -> dict | None:
    """Valida credenciales contra la tabla usuarios. Devuelve {usuario, rol} o None."""
    with get_conn() as conn:
        row = conn.execute(
            "SELECT usuario, password_hash, rol FROM usuarios WHERE usuario=? AND activo=1",
            (usuario,),
        ).fetchone()
    if not row or not verify_password(password, row["password_hash"]):
        return None
    return {"usuario": row["usuario"], "rol": row["rol"]}


def crear_token(usuario: str, rol: str) -> str:
    ahora = int(time.time())
    payload = {"sub": usuario, "rol": rol, "iat": ahora, "exp": ahora + TOKEN_HORAS * 3600}
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)


def get_current_user(
    credenciales: HTTPAuthorizationCredentials | None = Depends(_bearer),
) -> dict:
    """Dependencia: exige un token Bearer valido y devuelve {usuario, rol}."""
    if credenciales is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "No autenticado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        payload = jwt.decode(credenciales.credentials, SECRET, algorithms=[ALGORITHM])
    except PyJWTError:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Token invalido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    usuario = payload.get("sub")
    rol = payload.get("rol")
    if not usuario or rol not in ("admin", "analista", "consulta"):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            "Token invalido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"usuario": usuario, "rol": rol}


def requiere_rol(*roles: str):
    """Dependencia-fabrica: exige que el rol del token este dentro de `roles`."""
    def verificar(user: dict = Depends(get_current_user)) -> dict:
        if user["rol"] not in roles:
            raise HTTPException(
                status.HTTP_403_FORBIDDEN,
                "No autorizado para esta operacion",
            )
        return user

    return verificar
