import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("Erro: a variável DATABASE_URL não foi encontrada no arquivo .env")

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
except SQLAlchemyError as e:
    raise Exception(f"Erro ao configurar a conexão com o banco de dados: {e}")


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao acessar o banco de dados: {str(e)}"
        )
    finally:
        if db is not None:
            db.close()
