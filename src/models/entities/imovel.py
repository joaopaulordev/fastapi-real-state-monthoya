from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)
    valor = Column("valor", Float, nullable=False)
    
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor        

    def __repr__(self):
        return f"Imovel [descricao={self.descricao}, valor={self.valor}]"
