from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from src.main.routes.schemas import CaracteristicasSchema, ImovelSchema, ListarImovelSchema
from src.models.settings.dependencies import get_session_db
from src.main.composer.imovel_listar_composer import imovel_listar_composer
from src.main.composer.imovel_inserir_composer import imovel_inserir_composer
from src.main.composer.imovel_visualizar_composer import imovel_visualizar_composer
from src.main.composer.imovel_atualizar_composer import imovel_atualizar_composer
from src.main.composer.imovel_deletar_composer import imovel_deletar_composer
from src.main.composer.imovel_caracteristica_inserir_composer import imovel_caracteristica_inserir_composer
from src.main.composer.imovel_caracteristica_deletar_composer import imovel_caracteristica_deletar_composer
from src.main.composer.imovel_caracteristica_atualizar_composer import imovel_caracteristica_atualizar_composer
from src.views.http_types.http_request import HttpRequest

from src.models.entities.imovel import Imovel


imoveis_routes = APIRouter(tags=["Imóveis"])

@imoveis_routes.post("/imoveis/caracteristicas/adicionar/{imovel_id}")
async def inserir_caracteristicas_imovel(imovel_id: int, body: CaracteristicasSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"imovel_id": imovel_id})
    imovel_caracteristica_inserir = imovel_caracteristica_inserir_composer(db)

    http_response = await imovel_caracteristica_inserir.handle_inserir_caracteristicas_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@imoveis_routes.post("/imoveis/caracteristicas/atualizar/{imovel_id}")
async def atualizar_caracteristicas_imovel(imovel_id: int, body: CaracteristicasSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"imovel_id": imovel_id})
    imovel_caracteristica_atualizar = imovel_caracteristica_atualizar_composer(db)

    http_response = await imovel_caracteristica_atualizar.handle_atualizar_caracteristicas_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@imoveis_routes.post("/imoveis/caracteristicas/deletar/{imovel_id}")
async def deletar_caracteristicas_imovel(imovel_id: int, body: CaracteristicasSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"imovel_id": imovel_id})
    imovel_caracteristica_deletar = imovel_caracteristica_deletar_composer(db)

    http_response = await imovel_caracteristica_deletar.handle_deletar_caracteristica_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@imoveis_routes.post("/imoveis")
async def criar_imovel(body: ImovelSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body))
    imovel_inserir = imovel_inserir_composer(db)

    http_response = await imovel_inserir.handle_inserir_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@imoveis_routes.post("/imoveis/listar")
async def listar_imoveis(body: ListarImovelSchema, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(body=dict(body))
    view = imovel_listar_composer(db)

    http_response = await view.handle_listar_imoveis(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        

        
@imoveis_routes.get("/imoveis/visualizar/{imovel_id}")
async def visualizar_imovel(imovel_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"imovel_id": imovel_id})
    view = imovel_visualizar_composer(db)

    http_response = await view.handle_visualizar_imovel(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        


@imoveis_routes.put("/imoveis/atualizar/{imovel_id}")
async def atualizar_imovel(imovel_id: int, body: ImovelSchema, db: Session = Depends(get_session_db)):
    http_request = HttpRequest(body=dict(body), param={"imovel_id": imovel_id})
    imovel_atualizar = imovel_atualizar_composer(db)

    http_response = await imovel_atualizar.handle_atualizar_imovel(http_request)
    
    return JSONResponse(
        content=http_response.body,
        status_code=http_response.status_code
    )


@imoveis_routes.delete("/imoveis/deletar/{imovel_id}")
async def deletar_imovel(imovel_id: int, db: Session = Depends(get_session_db)):    
    http_request = HttpRequest(param={"imovel_id": imovel_id})
    view = imovel_deletar_composer(db)

    http_response = await view.handle_deletar_imovel(http_request)

    return JSONResponse(
        content=http_response.body, 
        status_code=http_response.status_code
    )        
