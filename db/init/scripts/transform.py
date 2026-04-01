
def transform_data(df):
    """Converte tipos de dados para compatibilidade com o PostgreSQL."""
    
    df["id_escola"] = df["id_escola"].astype(int)
    df["id_municipio"] = df["id_municipio"].astype(int)

    bools_data = [
        "agua_potavel","agua_inexistente","energia_inexistente",
        "esgoto_inexistente","tratamento_lixo_inexistente","banheiro",
        "biblioteca","cozinha","dormitorio_aluno","laboratorio_ciencias",
        "laboratorio_informatica","patio_coberto","patio_descoberto",
        "quadra_esportes","refeitorio","alimentacao","acessibilidade_corrimao",
        "acessibilidade_elevador","acessibilidade_pisos_tateis","acessibilidade_vao_livre",
        "acessibilidade_rampas","acessibilidade_sinal_sonoro","acessibilidade_sinal_tatil",
        "acessibilidade_sinal_visual","acessibilidade_inexistente"
    ]
    
    df[bools_data] = df[bools_data].astype("boolean")
    print("Dados tratados com sucesso!")

    return df

