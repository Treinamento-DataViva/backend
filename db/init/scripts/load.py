import psycopg2
import geopandas as gp
from sqlalchemy import create_engine
from psycopg2.extras import execute_batch

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

