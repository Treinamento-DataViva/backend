from sqlalchemy.orm import Session
import repositories.escola_repository as escola_repository
from repositories.escola_repository import (
    listar_escolas,
    buscar_escola_por_id,
    agregar_escolas_por_uf_filtrado,
)


def listar(db: Session):
    return escola_repository.listar_escolas(db)

def buscar(db: Session, id_escola: int):
    return escola_repository.buscar_escola_por_id(db, id_escola)

def indicadores_por_municipio(db: Session, id_municipio: int, ano : int | None = None):
    return escola_repository.contar_indicadores_por_municipio(db, id_municipio, ano)

def agregar_por_municipio(db: Session, id_municipio: int, ano: int | None = None):
    return escola_repository.buscar_escola_por_municipio(db, id_municipio, ano)
    
    return buscar_escola_por_id(db, id_escola)


def agregar_por_uf_filtrado(db: Session, sigla_uf: str, ano: int | None = None):
    return agregar_escolas_por_uf_filtrado(db, sigla_uf, ano)
