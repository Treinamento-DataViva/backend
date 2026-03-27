#!/bin/bash

set -e

echo "🔹 Ativando ambiente virtual..."
source venv/bin/activate

echo "🔹 Subindo banco com Docker..."
cd db || exit
docker compose down
docker compose up -d
cd ..

echo "🔹 Instalando dependências..."
pip install -r requirements.txt

echo "🔹 Iniciando FastAPI..."
python -m uvicorn app:app --reload