import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.escola_routes import router as escola_router

app = FastAPI(title="Censo Escolar API")


# def get_allowed_origins() -> list[str]:
#     default_origins = [
#         "http://localhost:5173",
#         "http://127.0.0.1:5173",
#         "http://localhost:5174",
#         "http://127.0.0.1:5174",
#     ]
#     extra_origins = [
#         origin.strip()
#         for origin in os.getenv("FRONTEND_ORIGINS", "").split(",")
#         if origin.strip()
#     ]

#     return list(dict.fromkeys([*default_origins, *extra_origins]))

app.add_middleware(
    CORSMiddleware,
    #allow_origins=get_allowed_origins(),
    allow_origins = ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(escola_router, prefix="/escolas", tags=["Escolas"])


@app.get("/")
def root():
    return {"message": "API do Censo Escolar funcionando com sucesso"}
