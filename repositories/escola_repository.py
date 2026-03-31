from sqlalchemy.orm import Session
from sqlalchemy import func
from models.escola_model import Escola
from models.localizacao_model import Localizacao

def listar_escolas(db: Session):
    return db.query(Escola).limit(100).all()


def buscar_escola_por_id(db: Session, id_escola: int):
    return db.query(Escola).filter(Escola.id_escola == id_escola).first()

def buscar_escola_por_municipio(db: Session, id_municipio: int):

    escolas_municipio = (
            db.query(Escola,Localizacao)
            .outerjoin(Localizacao, Escola.id_escola == Localizacao.id_escola)
            .filter(Escola.id_municipio == id_municipio)
            .all()
    )
    
    if not escolas_municipio:
        return None

    escolas = []

    for escola_item, localizacao in escolas_municipio:
        escolas.append({
            "id_escola": escola_item.id_escola,
            "geometry": str(localizacao.geometry) if localizacao else None,
            "ano": escola_item.ano,
            "nome_escola": escola_item.nome_escola,
            "sigla_uf": escola_item.sigla_uf,
            "rede": escola_item.rede,
            "agua_potavel": escola_item.agua_potavel,
            "agua_inexistente": escola_item.agua_inexistente,
            "energia_inexistente": escola_item.energia_inexistente,
            "esgoto_inexistente": escola_item.esgoto_inexistente,
            "tratamento_lixo_inexistente": escola_item.tratamento_lixo_inexistente,
            "banheiro": escola_item.banheiro,
            "biblioteca": escola_item.biblioteca,
            "cozinha": escola_item.cozinha,
            "dormitorio_aluno": escola_item.dormitorio_aluno,
            "laboratorio_informatica": escola_item.laboratorio_informatica,
            "laboratorio_ciencias": escola_item.laboratorio_ciencias,
            "quadra_esportes": escola_item.quadra_esportes,
            "refeitorio": escola_item.refeitorio,
            "alimentacao": escola_item.alimentacao
        })
    
    return escolas

def contar_indicadores_por_municipio(db: Session, id_municipio: int):
    ultimo_ano = (db.query
                  (Escola.id_escola.label("id_escola"), func.max(Escola.ano).label("ano"))
                  .filter(Escola.id_municipio == id_municipio)
                  .group_by(Escola.id_escola)
                  .subquery()
    )

    indicadores = (
        db.query(
        func.count(Escola.id_escola).label("total_escolas"),
        func.count().filter(Escola.agua_potavel == True).label("agua_potavel"),
        func.count().filter(Escola.agua_inexistente == True).label("agua_inexistente"),
        func.count().filter(Escola.energia_inexistente == True).label("energia_inexistente"),
        func.count().filter(Escola.esgoto_inexistente == True).label("esgoto_inexistente"),
        func.count().filter(Escola.tratamento_lixo_inexistente == True).label("tratamento_lixo_inexistente"),
        func.count().filter(Escola.banheiro == True).label("banheiro"),
        func.count().filter(Escola.biblioteca == True).label("biblioteca"),
        func.count().filter(Escola.cozinha == True).label("cozinha"),
        func.count().filter(Escola.dormitorio_aluno == True).label("dormitorio_aluno"),
        func.count().filter(Escola.laboratorio_informatica == True).label("laboratorio_informatica"),
        func.count().filter(Escola.laboratorio_ciencias == True).label("laboratorio_ciencias"),
        func.count().filter(Escola.quadra_esportes == True).label("quadra_esportes"),
        func.count().filter(Escola.refeitorio == True).label("refeitorio"),
        func.count().filter(Escola.alimentacao == True).label("alimentacao"))
    .join(ultimo_ano, (Escola.id_escola == ultimo_ano.c.id_escola) & (Escola.ano == ultimo_ano.c.ano))
    .filter(Escola.id_municipio == id_municipio)
    .first()
    )
    
    return indicadores
    
