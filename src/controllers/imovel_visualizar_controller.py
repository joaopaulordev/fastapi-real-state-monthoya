from typing import Dict
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_visualizar_controller import ImovelVisualizarControllerInterface

class ImovelVisualizarController(ImovelVisualizarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def visualizar(self, imovel_id: int) -> Dict:
        imovel = await self.__busca_imovel_db(imovel_id)
        response = self.__format_response(imovel)
        return response

    async def __busca_imovel_db(self, imovel_id: int) -> Imovel:
        imovel = await self.__imovel_repository.visualizar_imoveis(imovel_id)
        return imovel

    def __format_response(self, imovel: Imovel) -> Dict:
        return {
            "data": {
                "type": "Imóvel",
                "count": 1,
                "attributes": {
                    "descricao": imovel.descricao,
                    "valor": imovel.valor,
                    "id": imovel.id
                }
            }
        }
