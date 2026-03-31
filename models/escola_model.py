from sqlalchemy import Column, Integer, Text, Boolean
from db.connection import Base


class Escola(Base):
    __tablename__ = "escola"

    id_escola = Column(Integer, primary_key=True, index=True)
    id_municipio = Column(Integer,nullable= False)

    ano = Column(Integer, nullable=True)
    nome_escola = Column(Text, nullable=True)
    sigla_uf = Column(Text, nullable=True)
    rede = Column(Text, nullable=True)

    agua_potavel = Column(Boolean, nullable=True)
    agua_inexistente = Column(Boolean, nullable=True)
    energia_inexistente = Column(Boolean, nullable=True)
    esgoto_inexistente = Column(Boolean, nullable=True)
    tratamento_lixo_inexistente = Column(Boolean, nullable=True)
    banheiro = Column(Boolean, nullable=True)
    biblioteca = Column(Boolean, nullable=True)
    cozinha = Column(Boolean, nullable=True)
    dormitorio_aluno = Column(Boolean, nullable=True)
    laboratorio_informatica = Column(Boolean, nullable=True)
    laboratorio_ciencias = Column(Boolean, nullable=True)
    quadra_esportes = Column(Boolean, nullable=True)
    refeitorio = Column(Boolean, nullable=True)
    alimentacao = Column(Boolean, nullable=True)