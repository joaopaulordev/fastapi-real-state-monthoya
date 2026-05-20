from pydantic import BaseModel
from typing import Optional, List


class FinalidadeSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class TipoImovelSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class PretensaoSchema(BaseModel):
    descricao: str
    
    class Config:
        from_attributes = True


class ImovelSchema(BaseModel):
    descricao: Optional[str] = None
    ativo: Optional[bool] = None
    lancamento: Optional[bool] = None
    destaque: Optional[bool] = None
    valor: Optional[float] = None
    visualizacoes: Optional[int] = 0
    finalidade: Optional[int] = 0
    tipo_imovel: Optional[int] = 0
    pretensao: Optional[int] = 0
    estado: Optional[int] = 18 
    cidade: Optional[str] = None
    endereco: Optional[str] = None
    complemento: Optional[str] = None
    sobre_imovel: Optional[str] = None
    area_total: Optional[float] = 0
    area_construida: Optional[float] = 0 
    dormitorios: Optional[int] = 0
    banheiros: Optional[int] = 0
    suites: Optional[int] = 0
    vagas_garagem: Optional[int] = 0
    vagas_garagem_cobertas: Optional[int] = 0
    vagas_garagem_descobertas: Optional[int] = 0

    class Config:
        from_attributes = True


class ListarImovelSchema(BaseModel):
    ativo: Optional[bool] = True
    pretensao: Optional[int] = None
    finalidade: Optional[int] = None
    tipo_imovel: Optional[int] = None    
    lancamento: Optional[bool] = False
    destaque: Optional[bool] = False
    valor_inicial: Optional[float] = 0
    valor_final: Optional[float] = 0
    dormitorios: Optional[int] = 0
    banheiros: Optional[int] = 0    
    suites: Optional[int] = 0
    vagas_garagem: Optional[int] = 0

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