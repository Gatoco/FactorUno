"""Configuracion de pytest: variables de entorno antes de importar la app.

El backend exige FACTORUNO_SECRET (sin valor por defecto) y el sembrado de
usuarios demo es opt-in (FACTORUNO_SEED_DEMO). Este conftest fija esos
valores para la suite, antes de que los modulos de prueba importen la app.
"""
import os

os.environ.setdefault("FACTORUNO_SECRET", "test-secret-pytest-0123456789abcdef0123456789abcdef")
os.environ.setdefault("FACTORUNO_SEED_DEMO", "1")
os.environ.setdefault("FACTORUNO_ADMIN_PASSWORD", "Admin1234!")
os.environ.setdefault("FACTORUNO_ANALISTA_PASSWORD", "Analista1234!")
os.environ.setdefault("FACTORUNO_CONSULTA_PASSWORD", "Consulta1234!")
