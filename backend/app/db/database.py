import os
from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "opspilot")

_password_fragment = f":{quote_plus(DB_PASSWORD)}" if DB_PASSWORD else ""
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}{_password_fragment}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, future=True)


def create_database_if_needed():
    admin_db = "postgres"
    admin_url = f"postgresql+psycopg2://{DB_USER}{_password_fragment}@{DB_HOST}:{DB_PORT}/{admin_db}"
    admin_engine = create_engine(admin_url, future=True)

    with admin_engine.connect() as conn:
        conn.execute(text("COMMIT"))
        result = conn.execute(text("SELECT 1 FROM pg_database WHERE datname = :name"), {"name": DB_NAME})
        if not result.scalar():
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
            print(f"Created database: {DB_NAME}")


def get_engine(url: str = DATABASE_URL):
    return create_engine(url, future=True)


if __name__ == "__main__":
    try:
        create_database_if_needed()
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Database Connected")
    except OperationalError as exc:
        print("Database connection failed:", exc)
        raise
