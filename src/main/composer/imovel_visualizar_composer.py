from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_visualizar_controller import ImovelVisualizarController
from src.views.imovel_visualizar_view import ImovelVisualizarView
from sqlalchemy.orm import Session

def imovel_visualizar_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelVisualizarController(model)
    view = ImovelVisualizarView(controller)

    return view