from src.models.interfaces.finalidade_repository import FinalidadeRepositoryInterface
from src.models.entities.imovel import Finalidade
from .interfaces.finalidade_visualizar_controller import FinalidadeVisualizarControllerInterface

class FinalidadeVisualizarController(FinalidadeVisualizarControllerInterface):
    def __init__(self, finalidade_repository: FinalidadeRepositoryInterface) -> None:
        self.__finalidade_repository = finalidade_repository

    async def visualizar(self, finalidade_id: int) -> dict:    
        finalidade = await self.__busca_finalidade_db(finalidade_id)
        response = self.__format_response(finalidade)
        return response

    async def __busca_finalidade_db(self, finalidade_id: int) -> Finalidade:
        finalidade = await self.__finalidade_repository.visualizar_finalidade(finalidade_id)
        return finalidade

    def __format_response(self, finalidade: Finalidade) -> dict:
        formatted_finalidade = { "id": finalidade.id, "descricao": finalidade.descricao }
        return {            
            "type": "Finalidade",
            "count": 1,
            "finalidade": formatted_finalidade        
        }