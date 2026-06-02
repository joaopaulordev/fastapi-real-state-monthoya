from typing import List
from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from src.models.entities.imovel import Finalidade
from .interfaces.finalidade_listar_controller import FinalidadeListarControllerInterface

class FinalidadeListarController(FinalidadeListarControllerInterface):
    def __init__(self, finalidade_repository: FinalidadeRepositoryInterface) -> None:
        self.__finalidade_repository = finalidade_repository

    async def listar(self) -> dict:    
        finalidades = await self.__buscar_finalidades_db()
        response = self.__format_response(finalidades)
        return response

    async def __buscar_finalidades_db(self) -> List[Finalidade]:
        finalidades = await self.__finalidade_repository.listar_finalidades()
        return finalidades

    def __format_response(self, finalidades: List[Finalidade]) -> dict:
        formatted_finalidades = [{ "id": finalidade.id, "descricao": finalidade.descricao} for finalidade in finalidades]
        return {
            "type": "Finalidades",
            "count": len(formatted_finalidades),
            "finalidades": formatted_finalidades            
        }
