from src.errors.error_handler import error_handler
from src.controllers.interfaces.imovel_listar_controller import ImovelListarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ImovelListarView:
    def __init__(self, controller: ImovelListarControllerInterface) -> None:
        self.__controller = controller

    async def handle_listar_imoveis(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_data = http_request.body
            body_response = await self.__controller.listar(imovel_data)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
