from typing import List
from sqlalchemy.orm import Session
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.errors.types.http_bad_request_error import HttpBadRequestError


class ImovelRepository(ImovelRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def listar_imoveis(self, valor_inicial: float, valor_final: float) -> List[Imovel]:
        if valor_final < valor_inicial:
            raise HttpBadRequestError("Valor final deve ser maior que o valor inicial.")
        
        if valor_inicial < 0 or valor_final < 0:
            raise HttpBadRequestError("Valores devem ser positivos.")
        
        if valor_inicial == 0 and valor_final == 0:
             imoveis = self.__db_session.query(Imovel).all()
             return imoveis
        
        if valor_inicial == 0:
             imoveis = self.__db_session.query(Imovel).filter(Imovel.valor <= valor_final).all()
             return imoveis
        
        imoveis = self.__db_session.query(Imovel).filter(Imovel.valor >= valor_inicial, Imovel.valor <= valor_final).all()
        return imoveis


    async def inserir_imovel(self, imovel_info: dict) -> Imovel:
        try:
            imovel = Imovel(**imovel_info)
            self.__db_session.add(imovel)
            self.__db_session.commit()
            return imovel
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def visualizar_imoveis(self, imovel_id: int) -> Imovel:
        imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
        if not imovel:
            raise HttpNotFoundError("Imóvel não encontrado.")
        return imovel


    async def atualizar_imovel(self, imovel_info: dict) -> Imovel:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("id")).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")

            imovel.descricao = imovel_info.get("descricao")
            imovel.ativo = imovel_info.get("ativo")
            imovel.lancamento = imovel_info.get("lancamento")
            imovel.destaque = imovel_info.get("destaque")
            imovel.valor = imovel_info.get("valor")
            imovel.visualizacoes = imovel_info.get("visualizacoes")
            imovel.finalidade = imovel_info.get("finalidade")
            imovel.tipo_imovel = imovel_info.get("tipo_imovel")
            imovel.pretensao = imovel_info.get("pretensao")
            imovel.estado = imovel_info.get("estado")
            imovel.cidade = imovel_info.get("cidade")
            imovel.endereco = imovel_info.get("endereco")
            imovel.complemento = imovel_info.get("complemento")
            imovel.sobre_imovel = imovel_info.get("sobre_imovel")
            imovel.area_total = imovel_info.get("area_total")
            imovel.area_construida = imovel_info.get("area_construida")
            imovel.dormitorios = imovel_info.get("dormitorios")
            imovel.banheiros = imovel_info.get("banheiros")
            imovel.suites = imovel_info.get("suites")
            imovel.vagas_garagem = imovel_info.get("vagas_garagem")
            imovel.vagas_garagem_cobertas = imovel_info.get("vagas_garagem_cobertas")
            imovel.vagas_garagem_descobertas = imovel_info.get("vagas_garagem_descobertas")

            self.__db_session.commit()
            return await self.visualizar_imoveis(imovel.id)
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def deletar_imovel(self, imovel_id: int) -> None:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")
            
            self.__db_session.delete(imovel)
            self.__db_session.commit()
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        