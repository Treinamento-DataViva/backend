from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.connection import get_db
from controllers import escola_controller
from schemas import escola_schema as escola

router = APIRouter()


@router.get("/", response_model=list[escola.EscolaResponse])
def listar_escolas(db: Session = Depends(get_db)):
    return escola_controller.listar(db)

@router.get("/municipios/{id_municipio}/indicadores", response_model = escola.IndicadoresMunicipioResponse)
def indicadores_por_municipio(id_municipio: int, db: Session = Depends(get_db)):
    return escola_controller.indicadores_por_municipio(db, id_municipio)

@router.get("/municipios/{id_municipio}", response_model = list[escola.EscolaMunicipioItemResponse])
def buscar_escolas_municipio(id_municipio: int, db: Session = Depends(get_db)):
    # escolas = escola_controller.agregar_por_municipio(db, id_municipio) 

    # if not escolas:
    #     raise HTTPException(status_code = 404, detail= "Nenhuma e
    # scola encontrada para esse município")
    # #Corrigir tratamento dos erros -> Municipio Inexistente != Municipio sem Escola

    # return escolas 
    return escola_controller.agregar_por_municipio(db, id_municipio)

@router.get("/{id_escola}", response_model= escola.EscolaResponse)
def buscar_escola(id_escola: int, db: Session = Depends(get_db)):
    escola = escola_controller.buscar(db, id_escola)

    if not escola:
        raise HTTPException(status_code=404, detail="Escola não encontrada")

    return escola