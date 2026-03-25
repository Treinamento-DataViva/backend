from sqlalchemy.orm import Session
from models.escola_model import Escola


def listar_escolas(db: Session):
    return db.query(Escola).limit(100).all()


def buscar_escola_por_id(db: Session, id_escola: int):
    return db.query(Escola).filter(Escola.id_escola == id_escola).first()