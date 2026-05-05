from typing import Dict
from abc import ABC, abstractmethod

class ImovelAtualizarControllerInterface(ABC):

    @abstractmethod
    async def atualizar(self, imovel_id: int, imovel_data: dict) -> dict: pass