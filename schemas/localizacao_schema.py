from pydantic import BaseModel

class LocalizacaoResponse(BaseModel):
    id_escola: int
    latitude: str | None = None
    longitude: str | None = None
    geometry: str | None = None

    class Config:
        from_attributes = True