from sqlalchemy.orm import Session
from repositories.escola_repository import (
    listar_escolas,
    buscar_escola_por_id,
    agregar_escolas_por_uf_filtrado,
)


def listar(db: Session):
    return listar_escolas(db)


def buscar(db: Session, id_escola: int):
    return buscar_escola_por_id(db, id_escola)


def agregar_por_uf_filtrado(db: Session, sigla_uf: str):
    return agregar_escolas_por_uf_filtrado(db, sigla_uf)
