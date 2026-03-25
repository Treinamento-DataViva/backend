from fastapi import FastAPI

from routes.escola_routes import router as escola_router

app = FastAPI(title="Censo Escolar API")

app.include_router(escola_router, prefix="/escolas", tags=["Escolas"])


@app.get("/")
def root():
    return {"message": "API do Censo Escolar funcionando com sucesso"}