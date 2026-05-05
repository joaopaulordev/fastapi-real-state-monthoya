from abc import ABC, abstractmethod

class ImovelDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, imovel_id: int) -> dict: pass