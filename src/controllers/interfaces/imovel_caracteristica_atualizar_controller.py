from abc import ABC, abstractmethod

class ImovelCaracteristicaAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, imovel_data: dict) -> dict: pass