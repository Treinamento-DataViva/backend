csv_pathfrom sqlalchemy.orm import Session
from models.localizacao_model import Localizacao

def listar_localizacoes(db: Session):
    return db.query(Localizacao).limit(100).all()

def buscar_localizacao_por_id_escola(db: Session, id_escola: int):
    return db.query(Localizacao).filter(Localizacao.id_escola == id_escola).first()

def listar_localizacoes_por_municipio(db: Session, id_municipio: int):
    from models.escola_model import Escola
    # Join com escola para filtrar por municipio
    return db.query(Localizacao).join(Escola, Localizacao.id_escola == Escola.id_escola).filter(Escola.id_municipio == id_municipio).all()