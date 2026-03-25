from sqlalchemy.orm import Session
from models.localizacao_model import Localizacao

def listar_localizacoes(db: Session):
    return db.query(Localizacao).limit(100).all()

def buscar_localizacao_por_id_escola(db: Session, id_escola: int):
    return db.query(Localizacao).filter(Localizacao.id_escola == id_escola).first()