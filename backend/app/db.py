"""SQLite schema and connection helpers."""
import os
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "mantenedor.db"

SCHEMA = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS calificaciones (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    ejercicio        INTEGER NOT NULL,
    mercado          TEXT    NOT NULL,
    instrumento      TEXT    NOT NULL,
    fecha_pago       TEXT    NOT NULL,          -- ISO YYYY-MM-DD
    secuencia        INTEGER NOT NULL,
    numero_dividendo INTEGER NOT NULL,
    tipo_sociedad    TEXT    NOT NULL CHECK (tipo_sociedad IN ('A','C')),
    valor_historico  REAL    NOT NULL DEFAULT 0,
    isfut            INTEGER NOT NULL DEFAULT 0,
    origen           TEXT    NOT NULL DEFAULT 'corredor'
                     CHECK (origen IN ('corredor','entidad')),
    fuente           TEXT    NOT NULL DEFAULT 'manual'
                     CHECK (fuente IN ('manual','archivo','sistema')),
    fecha_creacion   TEXT    NOT NULL DEFAULT (datetime('now','localtime')),
    fecha_modificacion TEXT  NOT NULL DEFAULT (datetime('now','localtime'))
);

-- Llave de negocio (historia 10): actualiza si existe, agrega si no.
CREATE UNIQUE INDEX IF NOT EXISTS uq_calificacion_llave
ON calificaciones (ejercicio, mercado, instrumento, fecha_pago,
                   secuencia, numero_dividendo, tipo_sociedad);

CREATE TABLE IF NOT EXISTS montos (
    calificacion_id INTEGER NOT NULL REFERENCES calificaciones(id) ON DELETE CASCADE,
    columna         INTEGER NOT NULL CHECK (columna BETWEEN 8 AND 37),
    monto           REAL    NOT NULL,
    PRIMARY KEY (calificacion_id, columna)
);

CREATE TABLE IF NOT EXISTS factores (
    calificacion_id INTEGER NOT NULL REFERENCES calificaciones(id) ON DELETE CASCADE,
    columna         INTEGER NOT NULL CHECK (columna BETWEEN 8 AND 37),
    factor          REAL    NOT NULL,
    PRIMARY KEY (calificacion_id, columna)
);

CREATE TABLE IF NOT EXISTS auditoria (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    accion       TEXT NOT NULL,                 -- INSERT / UPDATE / DELETE / CALCULAR / CARGA
    registro_id  INTEGER,
    detalle      TEXT NOT NULL DEFAULT '',
    usuario      TEXT NOT NULL DEFAULT 'corredor',
    fecha        TEXT NOT NULL DEFAULT (datetime('now','localtime'))
);

CREATE TABLE IF NOT EXISTS usuarios (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario        TEXT    NOT NULL UNIQUE,
    password_hash  TEXT    NOT NULL,
    rol            TEXT    NOT NULL CHECK (rol IN ('admin','analista','consulta')),
    activo         INTEGER NOT NULL DEFAULT 1,
    fecha_creacion TEXT    NOT NULL DEFAULT (datetime('now','localtime'))
);
"""


def get_conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def _seed_usuarios(conn: sqlite3.Connection) -> None:
    """Crea los usuarios base (admin/analista/consulta) si la tabla esta vacia."""
    from . import auth  # import tardio: auth importa get_conn de este modulo

    total = conn.execute("SELECT COUNT(*) FROM usuarios").fetchone()[0]
    if total:
        return
    for usuario, (env_var, default) in auth.USUARIOS_SEED.items():
        password = os.environ.get(env_var, default)
        conn.execute(
            "INSERT INTO usuarios (usuario, password_hash, rol) VALUES (?,?,?)",
            (usuario, auth.hash_password(password), usuario),
        )


def init_db() -> None:
    with get_conn() as conn:
        conn.executescript(SCHEMA)
        _seed_usuarios(conn)


def audit(conn: sqlite3.Connection, accion: str, registro_id: int | None,
          detalle: str, usuario: str = "corredor") -> None:
    cur = conn.execute(
        "INSERT INTO auditoria (accion, registro_id, detalle, usuario) VALUES (?,?,?,?)",
        (accion, registro_id, detalle, usuario),
    )
    # Espejo best-effort a DynamoDB (rúbrica 2.1.4.9); no-op sin tabla configurada.
    try:
        from . import aws_ext

        fila = conn.execute(
            "SELECT fecha FROM auditoria WHERE id=?", (cur.lastrowid,)
        ).fetchone()
        aws_ext.espejar_auditoria({
            "accion": accion,
            "registro_id": registro_id,
            "detalle": detalle,
            "usuario": usuario,
            "fecha": fila["fecha"] if fila else "",
        })
    except Exception:
        pass
