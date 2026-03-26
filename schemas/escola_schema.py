from pydantic import BaseModel


class EscolaResponse(BaseModel):
    id_escola: int
    ano: int | None = None
    nome_escola: str | None = None
    sigla_uf: str | None = None
    rede: str | None = None

    agua_potavel: bool | None = None
    agua_inexistente: bool | None = None
    energia_inexistente: bool | None = None
    esgoto_inexistente: bool | None = None
    tratamento_lixo_inexistente: bool | None = None
    banheiro: bool | None = None
    biblioteca: bool | None = None
    cozinha: bool | None = None
    dormitorio_aluno: bool | None = None
    laboratorio_informatica: bool | None = None
    laboratorio_ciencias: bool | None = None
    quadra_esportes: bool | None = None
    refeitorio: bool | None = None
    alimentacao: bool | None = None

    class Config:
        from_attributes = True


class EscolaAggregatedUFResponse(BaseModel):
    sigla_uf: str | None = None
    total_escolas: int
    agua_potavel: int
    agua_inexistente: int
    energia_inexistente: int
    esgoto_inexistente: int
    tratamento_lixo_inexistente: int
    banheiro: int
    biblioteca: int
    cozinha: int
    dormitorio_aluno: int
    laboratorio_informatica: int
    laboratorio_ciencias: int
    quadra_esportes: int
    refeitorio: int
    alimentacao: int

    class Config:
        from_attributes = True
