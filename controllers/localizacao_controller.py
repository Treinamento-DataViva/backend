from sqlalchemy.orm import Session
from repositories.localizacao_repository import (
    listar_localizacoes,
    buscar_localizacao_por_id_escola,
    listar_localizacoes_por_municipio
)
from repositories.municipio_repository import buscar_codigo_por_nome

def listar(db: Session):
    return listar_localizacoes(db)

def buscar(db: Session, id_escola: int):
    return buscar_localizacao_por_id_escola(db, id_escola)

def buscar_por_municipio(db: Session, nome_municipio: str):
    codigo = buscar_codigo_por_nome(db, nome_municipio)
    if not codigo:
        return []
    return listar_localizacoes_por_municipio(db, codigo)