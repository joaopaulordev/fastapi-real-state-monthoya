from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_listar_controller import ImovelListarController
from src.views.imovel_listar_view import ImovelListarView
from sqlalchemy.orm import Session

def imovel_listar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelListarController(model)
    view = ImovelListarView(controller)

    return view