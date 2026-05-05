from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_deletar_controller import ImovelDeletarControllerInterface

class ImovelDeletarController(ImovelDeletarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def deletar(self, imovel_id: int) -> dict:        
        await self.__imovel_repository.deletar_imovel(imovel_id)
        return {
            "message": f"Imóvel {imovel_id} deletado com sucesso."
        }
        

