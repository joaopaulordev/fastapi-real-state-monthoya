from typing import List
from sqlalchemy.orm import Session
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Caracteristica, Imovel
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.errors.types.http_bad_request_error import HttpBadRequestError


class ImovelRepository(ImovelRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def inserir_caracteristicas_imovel(self, imovel_info: dict) -> Imovel:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("imovel_id")).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")

            list_caracteristicas_id = imovel_info.get("caracteristicas_id", [])
            for caracteristica_id in list_caracteristicas_id:
                caracteristica = self.__db_session.query(Caracteristica).filter(Caracteristica.id == caracteristica_id).first()
                imovel.caracteristicas.append(caracteristica)

            self.__db_session.commit()
            return imovel
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        
        
    async def atualizar_caracteristicas_imovel(self, imovel_info: dict) -> Imovel:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("imovel_id")).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")

            list_caracteristicas_id = imovel_info.get("caracteristicas_id", [])
            caracteristicas = self.__db_session.query(Caracteristica).filter(Caracteristica.id.in_(list_caracteristicas_id)).all()
            imovel.caracteristicas = caracteristicas

            self.__db_session.commit()
            return imovel
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

        
    async def deletar_caracteristicas_imovel(self, imovel_info: dict) -> None:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("imovel_id")).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")
            
            list_caracteristicas_id = imovel_info.get("caracteristicas_id", [])
            for caracteristica_id in list_caracteristicas_id:
                caracteristica = self.__db_session.query(Caracteristica).filter(Caracteristica.id == caracteristica_id).first()
                imovel.caracteristicas.remove(caracteristica)
                        
            self.__db_session.commit()
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        


    async def listar_imoveis(self, imovel_info: dict) -> List[Imovel]:
        imoveis = None
        if imovel_info.get("valor_final") < imovel_info.get("valor_inicial"):
            raise HttpBadRequestError("Valor final deve ser maior que o valor inicial.")
        
        if imovel_info.get("valor_inicial") < 0 or imovel_info.get("valor_final") < 0:
            raise HttpBadRequestError("Valores devem ser positivos.")
        
        if imovel_info.get("valor_inicial") == 0 and imovel_info.get("valor_final") == 0:
             imoveis = self.__db_session.query(Imovel).all()             
        elif imovel_info.get("valor_inicial") == 0:
             imoveis = self.__db_session.query(Imovel).filter(Imovel.valor <= imovel_info.get("valor_final")).all()
        else:
            imoveis = self.__db_session.query(Imovel).filter(Imovel.valor >= imovel_info.get("valor_inicial"), Imovel.valor <= imovel_info.get("valor_final")).all()

        if imovel_info.get("pretensao"):
            imoveis = [imovel for imovel in imoveis if imovel.pretensao == imovel_info.get("pretensao")]

        if imovel_info.get("finalidade"):
            imoveis = [imovel for imovel in imoveis if imovel.finalidade == imovel_info.get("finalidade")]

        if imovel_info.get("tipo_imovel"):
            imoveis = [imovel for imovel in imoveis if imovel.tipo_imovel == imovel_info.get("tipo_imovel")]
        
        imoveis = [imovel for imovel in imoveis if imovel.lancamento == imovel_info.get("lancamento")]

        imoveis = [imovel for imovel in imoveis if imovel.destaque == imovel_info.get("destaque")]

        imoveis = [imovel for imovel in imoveis if imovel.ativo == imovel_info.get("ativo")]

        if imovel_info.get("dormitorios") and imovel_info.get("dormitorios") >= 5:
            imoveis = [imovel for imovel in imoveis if imovel.dormitorios >= imovel_info.get("dormitorios")]
        elif imovel_info.get("dormitorios") and imovel_info.get("dormitorios") < 5:
            imoveis = [imovel for imovel in imoveis if imovel.dormitorios == imovel_info.get("dormitorios")]
        
        if imovel_info.get("banheiros") and imovel_info.get("banheiros") >= 5:
            imoveis = [imovel for imovel in imoveis if imovel.banheiros >= imovel_info.get("banheiros")]
        elif imovel_info.get("banheiros") and imovel_info.get("banheiros") < 5:
            imoveis = [imovel for imovel in imoveis if imovel.banheiros == imovel_info.get("banheiros")]

        if imovel_info.get("suites") and imovel_info.get("suites") >= 5:
            imoveis = [imovel for imovel in imoveis if imovel.suites == imovel_info.get("suites")]
        elif imovel_info.get("suites") and imovel_info.get("suites") < 5:
            imoveis = [imovel for imovel in imoveis if imovel.suites == imovel_info.get("suites")]

        if imovel_info.get("vagas_garagem") and imovel_info.get("vagas_garagem") >= 5:
            imoveis = [imovel for imovel in imoveis if imovel.vagas_garagem >= imovel_info.get("vagas_garagem")]
        elif imovel_info.get("vagas_garagem") and imovel_info.get("vagas_garagem") < 5:
            imoveis = [imovel for imovel in imoveis if imovel.vagas_garagem == imovel_info.get("vagas_garagem")]

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
        
        imovel.visualizacoes += 1
        self.__db_session.commit()

        return imovel


    async def atualizar_imovel(self, imovel_info: dict) -> Imovel:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("id")).first()
            if not imovel:
                raise HttpNotFoundError("Imóvel não encontrado.")

            imovel.descricao = imovel_info.get("descricao") if imovel_info.get("descricao") else imovel.descricao
            imovel.ativo = imovel_info.get("ativo") if imovel_info.get("ativo") is not None else imovel.ativo
            imovel.lancamento = imovel_info.get("lancamento") if imovel_info.get("lancamento") is not None else imovel.lancamento
            imovel.destaque = imovel_info.get("destaque") if imovel_info.get("destaque") is not None else imovel.destaque
            imovel.valor = imovel_info.get("valor") if imovel_info.get("valor") is not None else imovel.valor
            imovel.finalidade = imovel_info.get("finalidade") if imovel_info.get("finalidade") != 0 else imovel.finalidade
            imovel.tipo_imovel = imovel_info.get("tipo_imovel") if imovel_info.get("tipo_imovel") != 0 else imovel.tipo_imovel
            imovel.pretensao = imovel_info.get("pretensao") if imovel_info.get("pretensao") != 0 else imovel.pretensao
            imovel.estado = imovel_info.get("estado") if imovel_info.get("estado") != 0 else imovel.estado
            imovel.cidade = imovel_info.get("cidade") if imovel_info.get("cidade") is not None else imovel.cidade
            imovel.endereco = imovel_info.get("endereco") if imovel_info.get("endereco") is not None else imovel.endereco
            imovel.complemento = imovel_info.get("complemento") if imovel_info.get("complemento") is not None else imovel.complemento
            imovel.sobre_imovel = imovel_info.get("sobre_imovel") if imovel_info.get("sobre_imovel") is not None else imovel.sobre_imovel
            imovel.area_total = imovel_info.get("area_total") if imovel_info.get("area_total") != 0 else imovel.area_total
            imovel.area_construida = imovel_info.get("area_construida") if imovel_info.get("area_construida") != 0 else imovel.area_construida
            imovel.dormitorios = imovel_info.get("dormitorios") if imovel_info.get("dormitorios") != 0 else imovel.dormitorios
            imovel.banheiros = imovel_info.get("banheiros") if imovel_info.get("banheiros") != 0 else imovel.banheiros
            imovel.suites = imovel_info.get("suites") if imovel_info.get("suites") != 0 else imovel.suites
            imovel.vagas_garagem = imovel_info.get("vagas_garagem") if imovel_info.get("vagas_garagem") != 0 else imovel.vagas_garagem
            imovel.vagas_garagem_cobertas = imovel_info.get("vagas_garagem_cobertas") if imovel_info.get("vagas_garagem_cobertas") != 0 else imovel.vagas_garagem_cobertas
            imovel.vagas_garagem_descobertas = imovel_info.get("vagas_garagem_descobertas") if imovel_info.get("vagas_garagem_descobertas") != 0 else imovel.vagas_garagem_descobertas

            self.__db_session.commit()
            return imovel
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
        