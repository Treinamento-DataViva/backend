import basedosdados as bd

censo_escolar = "seu-projeto-id"  # Substitua pelo ID do seu projeto no Google Cloud    

def extract_data():
    """Extrai dados do Censo Escolar 2024 via BigQuery."""
   
    query = """
    WITH 
    dicionario_rede AS (
    SELECT
        chave AS chave_rede,
        valor AS descricao_rede
    FROM `basedosdados.br_inep_censo_escolar.dicionario`
    WHERE
        TRUE
        AND nome_coluna = 'rede'
        AND id_tabela = 'escola'
    )
    SELECT
        dados.ano as ano,
        dados.sigla_uf as sigla_uf,
        dados.id_escola as id_escola,
        diretorio_id_escola.nome AS id_escola_nome,
        diretorio_id_escola.latitude AS id_escola_latitude,
        diretorio_id_escola.longitude AS id_escola_longitude,
        descricao_rede AS rede,
        dados.agua_potavel as agua_potavel,
        dados.agua_inexistente as agua_inexistente,
        dados.energia_inexistente as energia_inexistente,
        dados.esgoto_inexistente as esgoto_inexistente,
        dados.tratamento_lixo_inexistente as tratamento_lixo_inexistente,
        dados.banheiro as banheiro,
        dados.biblioteca as biblioteca,
        dados.cozinha as cozinha,
        dados.dormitorio_aluno as dormitorio_aluno,
        dados.laboratorio_ciencias as laboratorio_ciencias,
        dados.laboratorio_informatica as laboratorio_informatica,
        dados.patio_coberto as patio_coberto,
        dados.patio_descoberto as patio_descoberto,
        dados.quadra_esportes as quadra_esportes,
        dados.refeitorio as refeitorio,
        dados.alimentacao as alimentacao,
        dados.acessibilidade_corrimao as acessibilidade_corrimao,
        dados.acessibilidade_elevador as acessibilidade_elevador,
        dados.acessibilidade_pisos_tateis as acessibilidade_pisos_tateis,
        dados.acessibilidade_vao_livre as acessibilidade_vao_livre,
        dados.acessibilidade_rampas as acessibilidade_rampas,
        dados.acessibilidade_sinal_sonoro as acessibilidade_sinal_sonoro,
        dados.acessibilidade_sinal_tatil as acessibilidade_sinal_tatil,
        dados.acessibilidade_sinal_visual as acessibilidade_sinal_visual,
        dados.acessibilidade_inexistente as acessibilidade_inexistente
    FROM `basedosdados.br_inep_censo_escolar.escola` AS dados
    LEFT JOIN `dicionario_rede`
        ON dados.rede = chave_rede
    LEFT JOIN (SELECT DISTINCT id_escola,nome,latitude,longitude  FROM basedosdados.br_bd_diretorios_brasil.escola) AS diretorio_id_escola
    ON dados.id_escola = diretorio_id_escola.id_escola
    WHERE
        TRUE
        AND diretorio_id_escola.nome IS NOT NULL
        AND diretorio_id_escola.latitude IS NOT NULL
        AND diretorio_id_escola.longitude IS NOT NULL
        AND agua_potavel IS NOT NULL
        AND agua_inexistente IS NOT NULL
        AND dados.energia_inexistente IS NOT NULL
        AND dados.esgoto_inexistente IS NOT NULL
        AND dados.tratamento_lixo_inexistente IS NOT NULL
        AND dados.banheiro IS NOT NULL
        AND biblioteca IS NOT NULL
        AND dados.cozinha IS NOT NULL
        AND dados.dormitorio_aluno IS NOT NULL
        AND dados.laboratorio_ciencias IS NOT NULL
        AND dados.laboratorio_informatica IS NOT NULL
        AND dados.patio_coberto IS NOT NULL
        AND dados.patio_descoberto IS NOT NULL
        AND dados.quadra_esportes IS NOT NULL
        AND dados.refeitorio IS NOT NULL
        AND alimentacao IS NOT NULL
        AND dados.acessibilidade_corrimao IS NOT NULL
        AND dados.acessibilidade_elevador IS NOT NULL
        AND dados.acessibilidade_pisos_tateis IS NOT NULL
        AND dados.acessibilidade_vao_livre IS NOT NULL
        AND dados.acessibilidade_rampas IS NOT NULL
        AND dados.acessibilidade_sinal_sonoro IS NOT NULL
        AND dados.acessibilidade_sinal_tatil IS NOT NULL
        AND dados.acessibilidade_sinal_visual IS NOT NULL
        AND dados.acessibilidade_inexistente IS NOT NULL
    """
    
    df = bd.read_sql(query, billing_project_id=censo_escolar)
    print("Dados extraídos com sucesso!")

    return df

