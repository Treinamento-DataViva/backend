from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.connection import get_db
from controllers import escola_controller
from schemas import escola_schema as escola
from schemas.escola_schema import EscolaResponse, EscolaAggregatedUFResponse
from schemas.municipio_schema import OpcaoMunicipioResponse
from repositories.municipio_repository import buscar_codigos_por_nome, buscar_opcoes_por_nome

router = APIRouter()

@router.get("/", response_model=list[escola.EscolaResponse])
def listar_escolas(db: Session = Depends(get_db)):
    return escola_controller.listar(db)

@router.get("/municipios/opcoes/{nome_municipio}", response_model=list[OpcaoMunicipioResponse])
def opcoes_municipio(nome_municipio: str, db: Session = Depends(get_db)):
    """Retorna opções de município quando há ambiguidade de nome."""
    opcoes = buscar_opcoes_por_nome(db, nome_municipio)
    if not opcoes:
        raise HTTPException(status_code=404, detail="Município não encontrado")
    return opcoes

@router.get("/municipios/{id_municipio}/indicadores", response_model = escola.IndicadoresMunicipioResponse)
def indicadores_por_municipio(
    id_municipio: str, 
    ano: int | None = Query(default = None),
    codigo_estado: int | None = Query(default = None),
    db: Session = Depends(get_db)
    ):
    
    # Verificar se id_municipio é numérico (código) ou nome
    if id_municipio.isdigit():
        codigo = int(id_municipio)
    else:
        # É nome, fazer lookup exato e tratar ambiguidade
        codigos = buscar_codigos_por_nome(db, id_municipio, codigo_estado)
        if not codigos:
            raise HTTPException(status_code=404, detail="Município não encontrado")
        if len(codigos) > 1:
            raise HTTPException(
                status_code=409,
                detail=f"Nome de município ambíguo. Possíveis códigos: {codigos}"
            )
        codigo = codigos[0]
    
    indicadores =  escola_controller.indicadores_por_municipio(db, codigo, ano)   

    return indicadores

@router.get("/municipios/{id_municipio}", response_model = list[escola.EscolaMunicipioItemResponse])
def buscar_escolas_municipio(
    id_municipio: str,
    ano: int | None = Query(default = None),
    codigo_estado: int | None = Query(default = None),
    db: Session = Depends(get_db)
    ):

    # Verificar se id_municipio é numérico (código) ou nome
    if id_municipio.isdigit():
        codigo = int(id_municipio)
    else:
        # É nome, fazer lookup exato e tratar ambiguidade
        codigos = buscar_codigos_por_nome(db, id_municipio, codigo_estado)
        if not codigos:
            raise HTTPException(status_code=404, detail="Município não encontrado")
        if len(codigos) > 1:
            raise HTTPException(
                status_code=409,
                detail=f"Nome de município ambíguo. Possíveis códigos: {codigos}"
            )
        codigo = codigos[0]

    escolas = escola_controller.agregar_por_municipio(db, codigo, ano) 

    if not escolas:
        raise HTTPException(status_code = 404, detail= "Nenhuma escola encontrada para esse município")
    #Corrigir tratamento dos erros -> Municipio Inexistente != Municipio sem Escola

    return escolas 

@router.get("/{id_escola}", response_model= escola.EscolaResponse)
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

@router.get("/uf/{sigla_uf}/anos", response_model=list[int])
def listar_anos_por_uf(
    sigla_uf: str,
    db: Session = Depends(get_db),
):
    sigla_uf = sigla_uf.upper()
    anos = escola_controller.listar_anos_por_uf(db, sigla_uf)

    if not anos:
        raise HTTPException(status_code=404, detail="Nenhum ano encontrado para a UF informada")

    return anos


@router.get("/{id_escola}", response_model=EscolaResponse)
def buscar_escola(id_escola: int, db: Session = Depends(get_db)):
    escola = escola_controller.buscar(db, id_escola)

    if not escola:
        raise HTTPException(status_code=404, detail="Escola não encontrada")

    return escola
