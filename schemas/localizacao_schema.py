from pydantic import BaseModel

class LocalizacaoResponse(BaseModel):
    id_escola: int
    latitude: float | None = None
    longitude: float | None = None
    geometry: str | None = None

    class Config:
        from_attributes = True