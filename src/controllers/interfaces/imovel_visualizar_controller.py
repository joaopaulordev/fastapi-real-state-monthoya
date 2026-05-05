from typing import Dict
from abc import ABC, abstractmethod

class ImovelVisualizarControllerInterface(ABC):

    @abstractmethod
    async def visualizar(self, imovel_id: int) -> Dict: pass