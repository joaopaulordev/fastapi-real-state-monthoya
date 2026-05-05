from typing import List
from abc import ABC, abstractmethod
from src.models.entities.imovel import Imovel

class ImovelRepositoryInterface(ABC):

    @abstractmethod
    async def listar_imoveis(self) -> List[Imovel]: pass

    @abstractmethod
    async def inserir_imovel(self, imovel_info: dict) -> None: pass

    @abstractmethod
    async def visualizar_imoveis(self, imovel_id: int) -> Imovel: pass

    @abstractmethod
    async def atualizar_imovel(self, imovel_info: dict) -> None: pass

    @abstractmethod    
    async def deletar_imovel(self, imovel_id: int) -> None: pass 