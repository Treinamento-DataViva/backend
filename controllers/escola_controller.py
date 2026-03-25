from sqlalchemy.orm import Session
from repositories.escola_repository import listar_escolas, buscar_escola_por_id


def listar(db: Session):
    return listar_escolas(db)


def buscar(db: Session, id_escola: int):
    return buscar_escola_por_id(db, id_escola)