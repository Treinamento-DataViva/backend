import psycopg2
import geopandas as gp
from sqlalchemy import create_engine
from psycopg2.extras import execute_batch
import pandas as pd

# Configurações de conexão com o PostgreSQL
PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "censo_escolar", 
    "user": "admin",
    "password": "admin",
}

# Cria a engine do SQLAlchemy para facilitar a inserção de dados
engine = create_engine( "postgresql+psycopg2://admin:admin@localhost:5432/censo_escolar")

def load_data(df):
    """Carrega os dados nas tabelas escola e localizacao no PostgreSQL."""

    # Cria a extensão PostGIS se ainda não existir
    conn = psycopg2.connect(**PG_CONFIG)
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    conn.commit()
    cur.close()
    conn.close()

    df_escola = df[["id_escola","id_municipio","ano","id_escola_nome",
                    "sigla_uf", "rede", "agua_potavel",
                    "agua_inexistente", "energia_inexistente",
                    "esgoto_inexistente", "tratamento_lixo_inexistente",
                    "banheiro","biblioteca", "cozinha", "dormitorio_aluno",
                     "laboratorio_ciencias", "laboratorio_informatica",
                     "quadra_esportes", "refeitorio", "alimentacao"]]
    
    df_escola = df_escola.rename(columns={
        "id_escola_nome": "nome_escola"
    })
    
    df_loc = df[["id_escola","id_escola_latitude","id_escola_longitude"]].drop_duplicates()

    # Cria um GeoDataFrame para a tabela de localização
    gdf_loc = gp.GeoDataFrame(df_loc, 
            geometry= gp.points_from_xy(df_loc["id_escola_longitude"], df_loc["id_escola_latitude"]),
            crs="EPSG:4326"
    )

    gdf_loc = gdf_loc.rename(columns={
        "id_escola_latitude": "latitude",
        "id_escola_longitude": "longitude"
    })

    df_escola.to_sql("escola", engine, if_exists="append", index=False)
    gdf_loc.to_postgis("localizacao", engine, if_exists="append", index=False)

    print("Dados carregados com sucesso!")

def load_lookup_table():
    """Carrega a tabela de consulta de municípios a partir do arquivo Excel."""
    
    # Lê o arquivo Excel, pulando as linhas de cabeçalho
    df_municipios = pd.read_excel("RELATORIO_DTB_BRASIL_2024_MUNICIPIOS.xls", skiprows=5, header=0)
    
    # Remove a última coluna se for NaN
    df_municipios = df_municipios.dropna(axis=1, how='all')
    
    # Renomeia as colunas para nomes mais limpos
    df_municipios = df_municipios.rename(columns={
        'UF': 'uf',
        'Nome_UF': 'nome_uf',
        'Região Geográfica Intermediária': 'regiao_intermediaria',
        'Nome Região Geográfica Intermediária': 'nome_regiao_intermediaria',
        'Região Geográfica Imediata': 'regiao_imediata',
        'Nome Região Geográfica Imediata': 'nome_regiao_imediata',
        'Município': 'codigo_municipio',
        'Código Município Completo': 'id_municipio',
        'Nome_Município': 'nome_municipio'
    })
    
    # Carrega no banco
    df_municipios.to_sql("municipios", engine, if_exists="replace", index=False)
    
    print("Tabela de consulta de municípios carregada com sucesso!")

