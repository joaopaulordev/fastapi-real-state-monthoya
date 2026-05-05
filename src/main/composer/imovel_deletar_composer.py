from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_deletar_controller import ImovelDeletarController
from src.views.imovel_deletar_view import ImovelDeletarView
from sqlalchemy.orm import Session

def imovel_deletar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelDeletarController(model)
    view = ImovelDeletarView(controller)

    return view