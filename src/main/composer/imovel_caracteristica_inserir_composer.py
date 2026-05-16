from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_caracteristica_inserir_controller import ImovelCaracteristicaInserirController
from src.views.imovel_caracteristica_inserir_view import ImovelCaracteristicaInserirView
from sqlalchemy.orm import Session

def imovel_caracteristica_inserir_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelCaracteristicaInserirController(model)
    view = ImovelCaracteristicaInserirView(controller)
    return view