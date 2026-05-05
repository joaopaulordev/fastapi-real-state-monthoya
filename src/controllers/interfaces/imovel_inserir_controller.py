from typing import Dict
from abc import ABC, abstractmethod

class ImovelInserirControllerInterface(ABC):

    @abstractmethod
    async def inserir(self, imovel_data: Dict) -> Dict: pass