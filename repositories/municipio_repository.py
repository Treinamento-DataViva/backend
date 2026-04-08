from sqlalchemy.orm import Session
from models.municipio_model import Municipio
import unicodedata

def normalizar_texto(texto: str) -> str:
    """Normaliza o texto: remove acentos e converte para minúsculo."""
    return unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('ascii').lower()

def buscar_codigos_por_nome(db: Session, nome_municipio: str, codigo_estado: int | None = None) -> list[int]:
    """Retorna todos os códigos que batem exatamente com o nome normalizado."""
    nome_normalizado = normalizar_texto(nome_municipio).strip()
    codigos = []

    for municipio in db.query(Municipio).all():
        if normalizar_texto(municipio.ds_municipio).strip() != nome_normalizado:
            continue

        if codigo_estado is not None:
            estado_prefixo = str(codigo_estado).zfill(2)
            if not str(municipio.cd_estado_municipio).startswith(estado_prefixo):
                continue

        codigos.append(municipio.cd_estado_municipio)

    return codigos

def buscar_codigo_por_nome(db: Session, nome_municipio: str, codigo_estado: int | None = None) -> int | None:
    """Retorna o código quando há apenas um match exato."""
    codigos = buscar_codigos_por_nome(db, nome_municipio, codigo_estado)
    return codigos[0] if len(codigos) == 1 else None