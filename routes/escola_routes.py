from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.connection import get_db
from controllers import escola_controller
from schemas.escola_schema import EscolaResponse, EscolaAggregatedUFResponse

router = APIRouter()


@router.get("/", response_model=list[EscolaResponse])
def listar_escolas(db: Session = Depends(get_db)):
    return escola_controller.listar(db)


@router.get("/uf/{sigla_uf}", response_model=EscolaAggregatedUFResponse)
def agregar_escolas_por_uf(
    sigla_uf: str,
    ano: int | None = Query(default=None),
    db: Session = Depends(get_db),
):
    sigla_uf = sigla_uf.upper()
    agregado = escola_controller.agregar_por_uf_filtrado(db, sigla_uf, ano)

    if not agregado:
        raise HTTPException(status_code=404, detail="Nenhuma escola encontrada para a UF informada")

    return agregado


@router.get("/{id_escola}", response_model=EscolaResponse)
def buscar_escola(id_escola: int, db: Session = Depends(get_db)):
    escola = escola_controller.buscar(db, id_escola)

    if not escola:
        raise HTTPException(status_code=404, detail="Escola não encontrada")

    return escola
