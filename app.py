from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.escola_routes import router as escola_router

app = FastAPI(title="Censo Escolar API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(escola_router, prefix="/escolas", tags=["Escolas"])


@app.get("/")
def root():
    return {"message": "API do Censo Escolar funcionando com sucesso"}
