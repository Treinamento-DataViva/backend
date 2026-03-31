from sqlalchemy.orm import Session
import repositories.escola_repository as escola_repository


def listar(db: Session):
    return escola_repository.listar_escolas(db)

def buscar(db: Session, id_escola: int):
    return escola_repository.buscar_escola_por_id(db, id_escola)

def indicadores_por_municipio(db: Session, id_municipio: int):
    return escola_repository.contar_indicadores_por_municipio(db, id_municipio)

def agregar_por_municipio(db: Session, id_municipio: int):
    return escola_repository.buscar_escola_por_municipio(db, id_municipio)
    
