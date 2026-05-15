from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.errors.types.http_bad_request_error import HttpBadRequestError
from .interfaces.imovel_atualizar_controller import ImovelAtualizarControllerInterface
from src.models.entities.imovel import Imovel

class ImovelAtualizarController(ImovelAtualizarControllerInterface):
    def __init__(self, imovel_repository: ImovelRepositoryInterface) -> None:
        self._imovel_repository = imovel_repository

    async def atualizar(self, imovel_data: dict) -> dict:
        self._validate_imovel_data(imovel_data)
        imovel = await self.__atualizar_imovel(imovel_data)
        return self.__format__response(imovel)

    def _validate_imovel_data(self, imovel_data: dict) -> None:
        descricao = imovel_data["descricao"]
        if not descricao:
            raise HttpBadRequestError("Descricao do imóvel é obrigatória.")
        
        valor = imovel_data["valor"]
        if not valor:
            raise HttpBadRequestError("Valor do imóvel é obrigatório.")
        if valor <= 0:
            raise HttpBadRequestError("Valor do imóvel deve ser positivo.")
        
        finalidade = imovel_data["finalidade"]
        if not finalidade:
            raise HttpBadRequestError("Finalidade do imóvel é obrigatória.")
        
        tipo_imovel = imovel_data["tipo_imovel"]
        if not tipo_imovel:
            raise HttpBadRequestError("Tipo do imóvel é obrigatório.")
        
        pretensao = imovel_data["pretensao"]
        if not pretensao:
            raise HttpBadRequestError("Pretensão do imóvel é obrigatória.") 
        
        estado = imovel_data["estado"]
        if not estado:
            raise HttpBadRequestError("Estado do imóvel é obrigatório.")
        
        cidade = imovel_data["cidade"]
        if not cidade:
            raise HttpBadRequestError("Cidade do imóvel é obrigatória.")
        
        endereco = imovel_data["endereco"]
        if not endereco:
            raise HttpBadRequestError("Endereço do imóvel é obrigatório.")

    async def __atualizar_imovel(self, imovel_data: dict) -> Imovel:
        return await self._imovel_repository.atualizar_imovel(imovel_data)

    def __format__response(self, imovel: Imovel) -> dict:
        formatted_imovel = { "id": imovel.id, "descricao": imovel.descricao, "ativo": imovel.ativo, "lancamento": imovel.lancamento, "destaque": imovel.destaque, "valor": imovel.valor, "visualizacoes": imovel.visualizacoes, "finalidade": imovel.finalidade, "tipo_imovel": imovel.tipo_imovel, "pretensao": imovel.pretensao, "estado": imovel.estado, "cidade": imovel.cidade, "endereco": imovel.endereco, "complemento": imovel.complemento, "sobre_imovel": imovel.sobre_imovel, "area_total": imovel.area_total, "area_construida": imovel.area_construida, "dormitorios": imovel.dormitorios, "banheiros": imovel.banheiros, "suites": imovel.suites, "vagas_garagem": imovel.vagas_garagem, "vagas_garagem_cobertas": imovel.vagas_garagem_cobertas, "vagas_garagem_descobertas": imovel.vagas_garagem_descobertas}
        return {
            "type": "Imóvel",
            "count": 1,
            "attributes": formatted_imovel
        }