from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_caracteristica_atualizar_controller import ImovelCaracteristicaAtualizarController
from src.views.imovel_caracteristica_atualizar_view import ImovelCaracteristicaAtualizarView
from sqlalchemy.orm import Session

def imovel_caracteristica_atualizar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelCaracteristicaAtualizarController(model)
    view = ImovelCaracteristicaAtualizarView(controller)
    return view