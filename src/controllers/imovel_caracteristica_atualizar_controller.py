from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.imovel_caracteristica_atualizar_controller import ImovelCaracteristicaAtualizarControllerInterface
from src.models.entities.imovel import Imovel

class ImovelCaracteristicaAtualizarController(ImovelCaracteristicaAtualizarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self._imovel_repository = imovel_repository

    async def atualizar(self, imovel_data: dict) -> dict:
        if not imovel_data.get("caracteristicas_id"):
            raise HttpBadRequestError("Lista de características do imóvel é obrigatória.")
        
        imovel = await self.__atualizar_caracteristicas_imovel(imovel_data)
        return self.__format__response(imovel)    
    

    async def __atualizar_caracteristicas_imovel(self, imovel_data: dict) -> Imovel:
        imovel = await self._imovel_repository.atualizar_caracteristicas_imovel(imovel_data)
        return imovel

    def __format__response(self, imovel: Imovel) -> dict:
        formatted_imovel = { "id_imovel": imovel.id, "caracteristicas": [{ "id": caracteristica.id, "descricao": caracteristica.descricao } for caracteristica in imovel.caracteristicas] }
        return {
            "type": "Imóvel Características Atualizadas",
            "count": 1,
            "attributes": formatted_imovel
        }