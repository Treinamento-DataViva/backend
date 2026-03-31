from sqlalchemy import case, func, literal
from sqlalchemy.orm import Session
from models.escola_model import Escola


def listar_escolas(db: Session):
    return db.query(Escola).limit(100).all()


def buscar_escola_por_id(db: Session, id_escola: int):
    return db.query(Escola).filter(Escola.id_escola == id_escola).first()

def agregar_escolas_por_uf_filtrado(db: Session, sigla_uf: str, ano: int | None = None):
    def count_true(col):
        return func.sum(case((col.is_(True), 1), else_=0))

    sigla_uf_label = literal("BR") if sigla_uf == "BR" else Escola.sigla_uf
    query = db.query(
        sigla_uf_label.label("sigla_uf"),
        func.count().label("total_escolas"),
        count_true(Escola.agua_potavel).label("agua_potavel"),
        count_true(Escola.agua_inexistente).label("agua_inexistente"),
        count_true(Escola.energia_inexistente).label("energia_inexistente"),
        count_true(Escola.esgoto_inexistente).label("esgoto_inexistente"),
        count_true(Escola.tratamento_lixo_inexistente).label("tratamento_lixo_inexistente"),
        count_true(Escola.banheiro).label("banheiro"),
        count_true(Escola.biblioteca).label("biblioteca"),
        count_true(Escola.cozinha).label("cozinha"),
        count_true(Escola.dormitorio_aluno).label("dormitorio_aluno"),
        count_true(Escola.laboratorio_informatica).label("laboratorio_informatica"),
        count_true(Escola.laboratorio_ciencias).label("laboratorio_ciencias"),
        count_true(Escola.quadra_esportes).label("quadra_esportes"),
        count_true(Escola.refeitorio).label("refeitorio"),
        count_true(Escola.alimentacao).label("alimentacao"),
    )

    if ano is not None:
        query = query.filter(Escola.ano == ano)

    if sigla_uf != "BR":
        query = query.filter(Escola.sigla_uf == sigla_uf).group_by(Escola.sigla_uf)

    return query.first()
