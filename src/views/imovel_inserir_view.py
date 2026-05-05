from src.controllers.interfaces.imovel_inserir_controller import ImovelInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ImovelInserirView:
    def __init__(self, controller: ImovelInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_data = http_request.body
            response = await self.__controller.inserir(imovel_data)
            return HttpResponse(body=response, status_code=201)
        except Exception as exception:
            error_handler(exception)