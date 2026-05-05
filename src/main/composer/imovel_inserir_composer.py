from src.models.repositories.imovel_repository import ImovelRepository
from src.controllers.imovel_inserir_controller import ImovelInserirController
from src.views.imovel_inserir_view import ImovelInserirView
from sqlalchemy.orm import Session

def imovel_inserir_composer(db: Session):
    model = ImovelRepository(db)
    controller = ImovelInserirController(model)
    view = ImovelInserirView(controller)
    return view