from abc import ABC, abstractmethod

class ImovelCaracteristicaDeletarControllerInterface(ABC):

    @abstractmethod
    async def deletar(self, imovel_info: dict) -> dict: pass    