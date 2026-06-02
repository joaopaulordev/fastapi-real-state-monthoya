from typing import List
from src.models.interfaces.tipo_imovel_repository import TipoImovelRepositoryInterface
from src.models.entities.imovel import TipoImovel
from .interfaces.tipo_imovel_listar_controller import TipoImovelListarControllerInterface

class TipoImovelListarController(TipoImovelListarControllerInterface):
    def __init__(self, tipo_imovel_repository: TipoImovelRepositoryInterface) -> None:
        self.__tipo_imovel_repository = tipo_imovel_repository

    async def listar(self) -> dict:        
        tipo_imovels = await self.__buscar_tipo_imovels_db()
        response = self.__format_response(tipo_imovels)
        return response

    async def __buscar_tipo_imovels_db(self) -> List[TipoImovel]:
        tipo_imovels = await self.__tipo_imovel_repository.listar_tipo_imovels()
        return tipo_imovels

    def __format_response(self, tipo_imovels: List[TipoImovel]) -> dict:
        formatted_tipo_imovels = [{ "id": tipo_imovel.id, "descricao": tipo_imovel.descricao} for tipo_imovel in tipo_imovels]
        return {            
            "type": "TipoImoveis",
            "count": len(formatted_tipo_imovels),
            "tipoImoveis": formatted_tipo_imovels        
        }
