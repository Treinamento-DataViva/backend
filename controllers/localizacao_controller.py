from sqlalchemy.orm import Session
from repositories.localizacao_repository import (
    listar_localizacoes,
    buscar_localizacao_por_id_escola
)

def listar(db: Session):
    return listar_localizacoes(db)

def buscar(db: Session, id_escola: int):
    return buscar_localizacao_por_id_escola(db, id_escola)