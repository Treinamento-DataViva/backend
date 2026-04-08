from sqlalchemy import Column, Integer, Text
from db.connection import Base

class Municipio(Base):
    __tablename__ = "municipios"

    cd_estado_municipio = Column(Integer, primary_key=True, index=True)
    ds_municipio = Column(Text, nullable=False)