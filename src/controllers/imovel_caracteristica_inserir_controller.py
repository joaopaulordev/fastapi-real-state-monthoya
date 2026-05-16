from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.imovel_caracteristica_inserir_controller import ImovelCaracteristicaInserirControllerInterface
from src.models.entities.imovel import Imovel

class ImovelCaracteristicaInserirController(ImovelCaracteristicaInserirControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self._imovel_repository = imovel_repository

    async def inserir(self, imovel_data: dict) -> dict:
        if not imovel_data.get("caracteristicas_id"):
            raise HttpBadRequestError("Lista de características do imóvel é obrigatória.")
        
        imovel = await self.__inserir_caracteristicas_imovel(imovel_data)
        return self.__format__response(imovel)

    
        if not descricao:
            raise HttpBadRequestError("Descricao do imóvel é obrigatória.")
        
        valor = imovel_data["valor"]
        if not valor:
            raise HttpBadRequestError("Valor do imóvel é obrigatório.")
        if valor <= 0:
            raise HttpBadRequestError("Valor do imóvel deve ser positivo.")
        
        finalidade = imovel_data["finalidade"]
        if not finalidade:
            raise HttpBadRequestError("Finalidade do imóvel é obrigatória.")
        
        tipo_imovel = imovel_data["tipo_imovel"]
        if not tipo_imovel:
            raise HttpBadRequestError("Tipo do imóvel é obrigatório.")
        
        pretensao = imovel_data["pretensao"]
        if not pretensao:
            raise HttpBadRequestError("Pretensão do imóvel é obrigatória.") 
        
        estado = imovel_data["estado"]
        if not estado:
            raise HttpBadRequestError("Estado do imóvel é obrigatório.")
        
        cidade = imovel_data["cidade"]
        if not cidade:
            raise HttpBadRequestError("Cidade do imóvel é obrigatória.")
        
        endereco = imovel_data["endereco"]
        if not endereco:
            raise HttpBadRequestError("Endereço do imóvel é obrigatório.")

    async def __inserir_caracteristicas_imovel(self, imovel_data: dict) -> Imovel:
        imovel = await self._imovel_repository.inserir_caracteristicas_imovel(imovel_data)
        return imovel

    def __format__response(self, imovel: Imovel) -> dict:
        formatted_imovel = { "id_imovel": imovel.id, "caracteristicas": [{ "id": caracteristica.id, "descricao": caracteristica.descricao } for caracteristica in imovel.caracteristicas] }
        return {
            "type": "Imóvel Características Inseridas",
            "count": 1,
            "attributes": formatted_imovel
        }