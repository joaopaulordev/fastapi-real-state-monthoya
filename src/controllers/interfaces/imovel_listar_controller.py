from typing import Dict
from abc import ABC, abstractmethod

class ImovelListarControllerInterface(ABC):

    @abstractmethod
    async def listar(self, imovel_data: dict) -> Dict:
        pass
