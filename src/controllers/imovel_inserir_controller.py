from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.imovel_inserir_controller import ImovelInserirControllerInterface

class ImovelInserirController(ImovelInserirControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self._imovel_repository = imovel_repository

    async def inserir(self, imovel_data: dict) -> dict:
        self._validate_imovel_data(imovel_data)
        await self.__inserir_imovel(imovel_data)
        return self.__format__response(imovel_data)

    def _validate_imovel_data(self, imovel_data: dict) -> None:
        descricao = imovel_data["descricao"]
        if not descricao:
            raise HttpBadRequestError("Descricao do imóvel é obrigatória.")

    async def __inserir_imovel(self, imovel_data: dict) -> None:
        await self._imovel_repository.inserir_imovel(imovel_data)

    def __format__response(self, imovel_data: dict) -> dict:
        return {
            "type": "Imóvel",
            "count": 1,
            "attributes": imovel_data
        }