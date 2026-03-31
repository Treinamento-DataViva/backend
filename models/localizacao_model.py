from sqlalchemy import Column, Integer, Float, Text
from geoalchemy2 import Geometry
from db.connection import Base

class Localizacao(Base):
    __tablename__ = "localizacao"

    id_escola = Column(Integer, primary_key=True, index=True)
    latitude = Column(Text, nullable=True)
    longitude = Column(Text, nullable=True)
    geometry = Column(Geometry(geometry_type="POINT",srid= 4326), nullable=True)