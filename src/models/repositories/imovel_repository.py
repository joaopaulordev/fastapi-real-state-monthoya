from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from src.models.interfaces.imovel_repository import ImovelRepositoryInterface
from src.models.entities.imovel import Imovel
from src.errors.types.http_bad_request_error import HttpBadRequestError

class ImovelRepository(ImovelRepositoryInterface):
    def __init__(self, db: Session) -> None:
        self.__db_session = db


    async def listar_imoveis(self) -> List[Imovel]:
        imoveis = self.__db_session.query(Imovel).all()
        return imoveis


    async def inserir_imovel(self, imovel_info: dict) -> None:
        try:
            imovel = Imovel(**imovel_info)
            self.__db_session.add(imovel)
            self.__db_session.commit()
        except Exception as exception:
            self.__db_session.rollback()
            raise exception


    async def visualizar_imoveis(self, imovel_id: int) -> Imovel:
        imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
        if not imovel:
            raise HttpBadRequestError("Imóvel não encontrado.")
        return imovel


    async def atualizar_imovel(self, imovel_info: dict) -> None:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_info.get("id")).first()
            if not imovel:
                raise HttpBadRequestError("Imóvel não encontrado.")
            
            imovel.descricao = imovel_info.get("descricao")
            imovel.valor = imovel_info.get("valor")
            
            self.__db_session.commit()
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        

    async def deletar_imovel(self, imovel_id: int) -> None:
        try:
            imovel = self.__db_session.query(Imovel).filter(Imovel.id == imovel_id).first()
            if not imovel:
                raise HttpBadRequestError("Imóvel não encontrado.")
            
            self.__db_session.delete(imovel)
            self.__db_session.commit()
        except Exception as exception:
            self.__db_session.rollback()
            raise exception
        