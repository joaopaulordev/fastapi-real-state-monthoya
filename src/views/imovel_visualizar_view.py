from src.errors.error_handler import error_handler
from src.controllers.interfaces.imovel_visualizar_controller import ImovelVisualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ImovelVisualizarView:
    def __init__(self, controller: ImovelVisualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_visualizar_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_id = http_request.param.get("imovel_id")
            body_response = await self.__controller.visualizar(imovel_id)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
