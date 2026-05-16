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
    ativo: Optional[bool] = True
    pretensao: int
    finalidade: int
    tipo_imovel: int    
    lancamento: Optional[bool] = False
    destaque: Optional[bool] = False
    valor_inicial: float
    valor_final: float

    class Config:
        from_attributes = True


class ComentarioSchema(BaseModel):
    texto: str
    aprovado: Optional[bool] = False

    class Config:
        from_attributes = True


class InteressadoSchema(BaseModel):
    nome: str
    email: str
    telefone: str
    estado: int
    cidade: str

    class Config:
        from_attributes = True

class CaracteristicasSchema(BaseModel):
    caracteristicas_id: Optional[List[int]]

    class Config:
        from_attributes = True