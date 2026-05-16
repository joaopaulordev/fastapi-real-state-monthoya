from typing import Dict, List
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from .interfaces.imovel_listar_controller import ImovelListarControllerInterface

class ImovelListarController(ImovelListarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self.__imovel_repository = imovel_repository

    async def listar(self, valor_inicial: float, valor_final: float, pretensao: int, finalidade: int, tipo_imovel: int, lancamento: bool, destaque: bool, ativo: bool) -> Dict:
        imoveis = await self.__busca_imoveis_db(valor_inicial, valor_final, pretensao, finalidade, tipo_imovel, lancamento, destaque, ativo)
        response = self.__format_response(imoveis)
        return response

    async def __busca_imoveis_db(self, valor_inicial: float, valor_final: float, pretensao: int, finalidade: int, tipo_imovel: int, lancamento: bool, destaque: bool, ativo: bool) -> List[Imovel]:
        imoveis = await self.__imovel_repository.listar_imoveis(valor_inicial, valor_final, pretensao, finalidade, tipo_imovel, lancamento, destaque, ativo)
        return imoveis

    def __format_response(self, imoveis: List[Imovel]) -> Dict:
        formatted_imoveis = [{ "id": imovel.id, "descricao": imovel.descricao, "ativo": imovel.ativo, "lancamento": imovel.lancamento, "destaque": imovel.destaque, "valor": imovel.valor, "visualizacoes": imovel.visualizacoes, "finalidade": imovel.finalidade, "tipo_imovel": imovel.tipo_imovel, "pretensao": imovel.pretensao, "estado": imovel.estado, "cidade": imovel.cidade, "endereco": imovel.endereco, "complemento": imovel.complemento, "sobre_imovel": imovel.sobre_imovel, "area_total": imovel.area_total, "area_construida": imovel.area_construida, "dormitorios": imovel.dormitorios, "banheiros": imovel.banheiros, "suites": imovel.suites, "vagas_garagem": imovel.vagas_garagem, "vagas_garagem_cobertas": imovel.vagas_garagem_cobertas, "vagas_garagem_descobertas": imovel.vagas_garagem_descobertas,
                              "caracteristicas": [{"id": caracteristica.id, "descricao": caracteristica.descricao} for caracteristica in imovel.caracteristicas],
                              "fotos": [{"id": foto.id, "caminho": foto.caminho, "imovel_id": foto.imovel_id} for foto in imovel.fotos],
                              "comentarios": [{"id": comentario.id, "texto": comentario.texto, "aprovado": comentario.aprovado, "imovel_id": comentario.imovel_id} for comentario in imovel.comentarios],
                              "interessados": [{"id": interessado.id, "nome": interessado.nome, "email": interessado.email, "telefone": interessado.telefone, "estado": interessado.estado, "cidade": interessado.cidade, "imovel_id": interessado.imovel_id} for interessado in imovel.interessados]
                            } for imovel in imoveis]
        return {
            "data": {
                "type": "Imoveis",
                "count": len(formatted_imoveis),
                "attributes": formatted_imoveis
            }
        }
