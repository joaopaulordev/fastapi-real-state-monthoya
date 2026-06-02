from src.models.interfaces.pretensao_repository import PretensaoRepositoryInterface
from src.models.entities.imovel import Pretensao
from .interfaces.pretensao_visualizar_controller import PretensaoVisualizarControllerInterface

class PretensaoVisualizarController(PretensaoVisualizarControllerInterface):
    def __init__(self, pretensao_repository: PretensaoRepositoryInterface) -> None:
        self.__pretensao_repository = pretensao_repository

    async def visualizar(self, pretensao_id: int) -> dict:    
        pretensao = await self.__busca_pretensao_db(pretensao_id)
        response = self.__format_response(pretensao)
        return response

    async def __busca_pretensao_db(self, pretensao_id: int) -> Pretensao:
        pretensao = await self.__pretensao_repository.visualizar_pretensao(pretensao_id)
        return pretensao

    def __format_response(self, pretensao: Pretensao) -> dict:
        formatted_pretensao = { "id": pretensao.id, "descricao": pretensao.descricao }
        return {
            "type": "Pretensao",
            "count": 1,
            "pretensao": formatted_pretensao            
        }