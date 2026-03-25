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