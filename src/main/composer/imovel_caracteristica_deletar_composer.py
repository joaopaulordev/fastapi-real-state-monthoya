from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_caracteristica_deletar_controller import ImovelCaracteristicaDeletarController
from src.views.imovel_caracteristica_deletar_view import ImovelCaracteristicaDeletarView
from sqlalchemy.orm import Session

def imovel_caracteristica_deletar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelCaracteristicaDeletarController(model)
    view = ImovelCaracteristicaDeletarView(controller)
    return view