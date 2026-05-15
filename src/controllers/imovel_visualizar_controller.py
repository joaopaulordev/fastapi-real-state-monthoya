from typing import Dict
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_visualizar_controller import ImovelVisualizarControllerInterface

class ImovelVisualizarController(ImovelVisualizarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def visualizar(self, imovel_id: int) -> Dict:
        imovel = await self.__busca_imovel_db(imovel_id)
        response = self.__format_response(imovel)
        return response

    async def __busca_imovel_db(self, imovel_id: int) -> Imovel:
        imovel = await self.__imovel_repository.visualizar_imoveis(imovel_id)
        return imovel

    def __format_response(self, imovel: Imovel) -> Dict:
        formatted_imovel = { "id": imovel.id, "descricao": imovel.descricao, "ativo": imovel.ativo, "lancamento": imovel.lancamento, "destaque": imovel.destaque, "valor": imovel.valor, "visualizacoes": imovel.visualizacoes, "finalidade": imovel.finalidade, "tipo_imovel": imovel.tipo_imovel, "pretensao": imovel.pretensao, "estado": imovel.estado, "cidade": imovel.cidade, "endereco": imovel.endereco, "complemento": imovel.complemento, "sobre_imovel": imovel.sobre_imovel, "area_total": imovel.area_total, "area_construida": imovel.area_construida, "dormitorios": imovel.dormitorios, "banheiros": imovel.banheiros, "suites": imovel.suites, "vagas_garagem": imovel.vagas_garagem, "vagas_garagem_cobertas": imovel.vagas_garagem_cobertas, "vagas_garagem_descobertas": imovel.vagas_garagem_descobertas}
        return {
            "data": {
                "type": "Imóvel",
                "count": 1,
                "attributes": formatted_imovel
            }
        }
        
