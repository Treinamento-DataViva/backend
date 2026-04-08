from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from controllers import localizacao_controller
from schemas.localizacao_schema import LocalizacaoResponse

router = APIRouter()

@router.get("/", response_model=list[LocalizacaoResponse])
def listar_localizacoes(db: Session = Depends(get_db)):
    return localizacao_controller.listar(db)

@router.get("/{id_escola}", response_model=LocalizacaoResponse)
def buscar_localizacao(id_escola: int, db: Session = Depends(get_db)):
    localizacao = localizacao_controller.buscar(db, id_escola)
    if not localizacao:
        raise HTTPException(status_code=404, detail="Localização não encontrada")
    return localizacao

@router.get("/municipio/{nome_municipio}", response_model=list[LocalizacaoResponse])
def buscar_localizacoes_por_municipio(nome_municipio: str, db: Session = Depends(get_db)):
    return localizacao_controller.buscar_por_municipio(db, nome_municipio)