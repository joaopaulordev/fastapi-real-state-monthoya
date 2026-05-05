from fastapi import FastAPI
from src.main.routes.imoveis_routes import imoveis_routes

app = FastAPI()

app.include_router(imoveis_routes)