from sqlalchemy import Column, Integer, Float, Text
from db.connection import Base

class Localizacao(Base):
    __tablename__ = "localizacao"

    id_escola = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    geometry = Column(Text, nullable=True)