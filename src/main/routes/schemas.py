from pydantic import BaseModel
from typing import Optional, List

class ImovelSchema(BaseModel):
    descricao: str
    valor: float

    class Config:
        from_attributes = True

