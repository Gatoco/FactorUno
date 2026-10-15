"""API REST del Mantenedor de Calificaciones Tributarias (nuam)."""
import os

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from . import auth, aws_ext, servicio
from .db import init_db

app = FastAPI(title="Mantenedor de Calificaciones Tributarias", version="0.1.0")


def _cors_origins() -> list[str]:
    env = os.environ.get("FACTORUNO_CORS_ORIGINS", "")
    return [o.strip() for o in env.split(",") if o.strip()] or [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins(),
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)


@app.on_event("startup")
def _startup() -> None:
    init_db()


class CalificacionIn(BaseModel):
    ejercicio: int = Field(ge=2000, le=2100)
    mercado: str = Field(min_length=1, max_length=3)
    instrumento: str = Field(min_length=1, max_length=50)
    fecha_pago: str
    secuencia: int = Field(ge=0)
    numero_dividendo: int = Field(ge=0)
    tipo_sociedad: str = Field(pattern="^[AaCc]$")
    valor_historico: float = 0.0
    isfut: bool = False
    origen: str = Field(default="corredor", pattern="^(corredor|entidad)$")
    montos: dict[int, float] = {}
    factores: dict[int, float] | None = None


class CalificacionUpdate(CalificacionIn):
    ejercicio: int | None = None
    mercado: str | None = None
    instrumento: str | None = None
    fecha_pago: str | None = None
    secuencia: int | None = None
    numero_dividendo: int | None = None
    tipo_sociedad: str | None = None
    valor_historico: float | None = None
    isfut: bool | None = None
    origen: str | None = None


class LoginIn(BaseModel):
    usuario: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1, max_length=128)


@app.post("/api/auth/login")
def login(data: LoginIn):
    user = auth.autenticar(data.usuario, data.password)
    if not user:
        raise HTTPException(401, "Credenciales invalidas")
    return {
        "access_token": auth.crear_token(user["usuario"], user["rol"]),
        "token_type": "bearer",
        "usuario": user["usuario"],
        "rol": user["rol"],
    }


@app.get("/api/auth/me")
def me(user: dict = Depends(auth.get_current_user)):
    return user


@app.get("/api/calificaciones")
def listar(mercado: str | None = None, origen: str | None = None,
           periodo: int | None = None,
           user: dict = Depends(auth.get_current_user)):
    return servicio.listar_calificaciones(mercado, origen, periodo)


@app.get("/api/calificaciones/{registro_id}")
def obtener(registro_id: int, user: dict = Depends(auth.get_current_user)):
    d = servicio.obtener_calificacion(registro_id)
    if not d:
        raise HTTPException(404, "Calificacion no encontrada")
    return d


@app.post("/api/calificaciones", status_code=201)
def crear(data: CalificacionIn,
          user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    return servicio.crear_calificacion(data.model_dump(), usuario=user["usuario"])


@app.put("/api/calificaciones/{registro_id}")
def modificar(registro_id: int, data: CalificacionUpdate,
              user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    d = servicio.modificar_calificacion(registro_id, data.model_dump(exclude_unset=True),
                                        usuario=user["usuario"])
    if not d:
        raise HTTPException(404, "Calificacion no encontrada")
    return d


@app.delete("/api/calificaciones/{registro_id}", status_code=204)
def eliminar(registro_id: int,
             user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    if not servicio.eliminar_calificacion(registro_id, usuario=user["usuario"]):
        raise HTTPException(404, "Calificacion no encontrada")


@app.post("/api/calificaciones/{registro_id}/calcular")
def calcular(registro_id: int,
             user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    d = servicio.calcular_por_registro(registro_id, usuario=user["usuario"])
    if not d:
        raise HTTPException(404, "Calificacion no encontrada")
    return d


@app.post("/api/carga")
async def carga(archivo: UploadFile = File(...), tipo: str = "montos",
                user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    contenido = (await archivo.read()).decode("utf-8-sig")
    try:
        return servicio.cargar_csv(contenido, tipo, usuario=user["usuario"])
    except ValueError as e:
        raise HTTPException(400, str(e))


@app.get("/api/auditoria")
def auditoria(limite: int = 100,
              user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    return servicio.listar_auditoria(limite)


@app.get("/api/exportar")
def exportar(formato: str = "json",
             user: dict = Depends(auth.requiere_rol("admin", "analista"))):
    """Genera un respaldo (JSON/CSV) y lo sube a S3 con URL prefirmada."""
    if formato not in ("json", "csv"):
        raise HTTPException(400, "formato debe ser 'json' o 'csv'")
    contenido, nombre, content_type = servicio.construir_exportacion(formato)
    try:
        return aws_ext.exportar_a_s3(contenido, nombre, content_type)
    except (ValueError, aws_ext.AlmacenamientoNoDisponible) as e:
        raise HTTPException(503, str(e))
