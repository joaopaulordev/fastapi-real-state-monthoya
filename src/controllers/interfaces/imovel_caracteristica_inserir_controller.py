from abc import ABC, abstractmethod
from src.models.entities.imovel import Imovel

class ImovelCaracteristicaInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, imovel_data: dict) -> dict: pass