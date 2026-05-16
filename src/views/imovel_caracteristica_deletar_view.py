from src.errors.error_handler import error_handler
from src.controllers.interfaces.imovel_caracteristica_deletar_controller import ImovelCaracteristicaDeletarControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class ImovelCaracteristicaDeletarView:
    def __init__(self, controller: ImovelCaracteristicaDeletarControllerInterface) -> None:
        self.__controller = controller

    async def handle_deletar_caracteristica_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_data = {"imovel_id": http_request.param.get("imovel_id"), "caracteristicas_id": http_request.body.get("caracteristicas_id")}
            body_response = await self.__controller.deletar(imovel_data)
            return HttpResponse(status_code=200, body=body_response)
        except Exception as exception:
            error_handler(exception)
