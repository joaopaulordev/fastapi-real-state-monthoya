from src.controllers.interfaces.imovel_caracteristica_atualizar_controller import ImovelCaracteristicaAtualizarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ImovelCaracteristicaAtualizarView:
    def __init__(self, controller: ImovelCaracteristicaAtualizarControllerInterface) -> None:
        self.__controller = controller

    async def handle_atualizar_caracteristicas_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_data = {"imovel_id": http_request.param.get("imovel_id"), "caracteristicas_id": http_request.body.get("caracteristicas_id")}
            response = await self.__controller.atualizar(imovel_data)
            return HttpResponse(body=response, status_code=200)
        except Exception as exception:
            error_handler(exception)