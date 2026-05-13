from pydantic import BaseModel
from typing import Optional, List

class ImovelSchema(BaseModel):
    descricao: str
    ativo: Optional[bool] = True
    lancamento: Optional[bool] = False
    destaque: Optional[bool] = False
    valor: float
    visualizacoes: Optional[int] = 0
    finalidade: int
    tipo_imovel: int
    pretensao: int
    estado: int 
    cidade: str
    endereco: str
    complemento: Optional[str] = None
    sobre_imovel: Optional[str] = None
    area_total: Optional[float] = None
    area_construida: Optional[float] = None 
    dormitorios: Optional[int] = None
    banheiros: Optional[int] = None
    suites: Optional[int] = None
    vagas_garagem: Optional[int] = None
    vagas_garagem_cobertas: Optional[int] = None
    vagas_garagem_descobertas: Optional[int] = None

    class Config:
        from_attributes = True


class BuscaImovelSchema(BaseModel):
    valor_inicial: float
    valor_final: float

    class Config:
        from_attributes = True