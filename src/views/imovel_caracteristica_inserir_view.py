from src.controllers.interfaces.imovel_caracteristica_inserir_controller import ImovelCaracteristicaInserirControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from src.errors.error_handler import error_handler


class ImovelCaracteristicaInserirView:
    def __init__(self, controller: ImovelCaracteristicaInserirControllerInterface) -> None:
        self.__controller = controller

    async def handle_inserir_caracteristicas_imovel(self, http_request: HttpRequest) -> HttpResponse:
        try:
            imovel_data = {"imovel_id": http_request.param.get("imovel_id"), "caracteristicas_id": http_request.body.get("caracteristicas_id")}
            response = await self.__controller.inserir(imovel_data)
            return HttpResponse(body=response, status_code=201)
        except Exception as exception:
            error_handler(exception)