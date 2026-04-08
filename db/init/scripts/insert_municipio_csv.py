import pandas as pd
import sys
import os

# Adicionar o diretório raiz ao sys.path para importar db
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from db.connection import engine

# Caminho para o CSV
csv_path = os.path.join(os.path.dirname(__file__), 'metadado_municipio.csv')

# Ler o CSV
try:
    df = pd.read_csv(csv_path, sep=';')
    print(f"CSV lido com sucesso. Colunas: {list(df.columns)}. Shape: {df.shape}")
except Exception as e:
    print(f"Erro ao ler CSV: {e}")
    exit(1)

# Inserir no banco de dados PostgreSQL
try:
    df.to_sql('municipios', engine, if_exists='replace', index=False)
    print("Dados inseridos com sucesso na tabela 'municipios'")
except Exception as e:
    print(f"Erro ao inserir no banco: {e}")
    exit(1)