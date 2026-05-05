from typing import Dict, List
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_listar_controller import ImovelListarControllerInterface

class ImovelListarController(ImovelListarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def listar(self) -> Dict:
        imoveis = await self.__busca_imoveis_db()
        response = self.__format_response(imoveis)
        return response

    async def __busca_imoveis_db(self) -> List[Imovel]:
        imoveis = await self.__imovel_repository.listar_imoveis() 
        return imoveis

    def __format_response(self, imoveis: List[Imovel]) -> Dict:
        formatted_imoveis = []
        for imovel in imoveis:
            formatted_imoveis.append({ "descricao": imovel.descricao, "valor": imovel.valor, "id": imovel.id })

        return {
            "data": {
                "type": "Imoveis",
                "count": len(formatted_imoveis),
                "attributes": formatted_imoveis
            }
        }
