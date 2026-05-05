from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_atualizar_controller import ImovelAtualizarController
from src.views.imovel_atualizar_view import ImovelAtualizarView
from sqlalchemy.orm import Session

def imovel_atualizar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelAtualizarController(model)
    view = ImovelAtualizarView(controller)
    return view