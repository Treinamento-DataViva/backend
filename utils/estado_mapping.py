"""Mapeamento de UF para código de estado IBGE e vice-versa."""

UF_TO_CODIGO = {
    "AC": 12,  # Acre
    "AL": 27,  # Alagoas
    "AP": 16,  # Amapá
    "AM": 13,  # Amazonas
    "BA": 29,  # Bahia
    "CE": 23,  # Ceará
    "DF": 53,  # Distrito Federal
    "ES": 32,  # Espírito Santo
    "GO": 52,  # Goiás
    "MA": 21,  # Maranhão
    "MT": 51,  # Mato Grosso
    "MS": 50,  # Mato Grosso do Sul
    "MG": 31,  # Minas Gerais
    "PA": 15,  # Pará
    "PB": 25,  # Paraíba
    "PR": 41,  # Paraná
    "PE": 26,  # Pernambuco
    "PI": 22,  # Piauí
    "RN": 24,  # Rio Grande do Norte
    "RS": 43,  # Rio Grande do Sul
    "RJ": 33,  # Rio de Janeiro
    "RO": 11,  # Rondônia
    "RR": 14,  # Roraima
    "SC": 42,  # Santa Catarina
    "SP": 35,  # São Paulo
    "SE": 28,  # Sergipe
    "TO": 17,  # Tocantins
}

CODIGO_TO_UF = {v: k for k, v in UF_TO_CODIGO.items()}


def get_uf_from_codigo(codigo_municipio: int) -> str | None:
    """Extrai a UF do código de município (primeiros 2 dígitos)."""
    codigo_estado = int(str(codigo_municipio)[:2])
    return CODIGO_TO_UF.get(codigo_estado)
