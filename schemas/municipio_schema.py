from pydantic import BaseModel

class OpcaoMunicipioResponse(BaseModel):
    codigo: int
    nome: str
    uf: str | None
