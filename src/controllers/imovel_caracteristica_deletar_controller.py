from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_caracteristica_deletar_controller import ImovelCaracteristicaDeletarControllerInterface

class ImovelCaracteristicaDeletarController(ImovelCaracteristicaDeletarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def deletar(self, imovel_info: dict) -> dict: 
        if not imovel_info.get("caracteristicas_id"):
            raise HttpBadRequestError("Lista de características do imóvel é obrigatória.")     
          
        await self.__imovel_repository.deletar_caracteristicas_imovel(imovel_info)
        return {
            "message": f"Características do imóvel {imovel_info.get('imovel_id')} deletada com sucesso."
        }
        

