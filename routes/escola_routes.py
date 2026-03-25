from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connection import get_db
from controllers import escola_controller
from schemas.escola_schema import EscolaResponse

router = APIRouter()


@router.get("/", response_model=list[EscolaResponse])
def listar_escolas(db: Session = Depends(get_db)):
    return escola_controller.listar(db)


@router.get("/{id_escola}", response_model=EscolaResponse)
def buscar_escola(id_escola: int, db: Session = Depends(get_db)):
    escola = escola_controller.buscar(db, id_escola)

    if not escola:
        raise HTTPException(status_code=404, detail="Escola não encontrada")

    return escola