from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.main.routes.imoveis_routes import imoveis_routes
from src.main.routes.fotos_routes import fotos_routes
from src.main.routes.comentarios_routes import comentario_routes
from src.main.routes.interessados_routes import interessado_routes
from src.main.routes.finalidades_routes import finalidade_routes
from src.main.routes.tipo_imoveis_routes import tipo_imovel_routes
from src.main.routes.pretensoes_routes import pretensao_routes

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'uploads' folder to the '/uploads' URL path
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(finalidade_routes)
app.include_router(tipo_imovel_routes)
app.include_router(pretensao_routes)
app.include_router(imoveis_routes)
app.include_router(fotos_routes)
app.include_router(comentario_routes)
app.include_router(interessado_routes)
