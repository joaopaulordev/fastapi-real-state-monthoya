from typing import List
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped

Base = declarative_base()

class Finalidade(Base):
    __tablename__ = "finalidades"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f"Finalidade [descricao={self.descricao}]"


class TipoImovel(Base):
    __tablename__ = "tipos_imovel"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f"TipoImovel [descricao={self.descricao}]"


class Pretensao(Base):
    __tablename__ = "pretensoes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f"Pretensao [descricao={self.descricao}]"
    

class Estado(Base):
    __tablename__ = "estados"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)

    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f"Estado [descricao={self.descricao}]"



caracteristica_imovel_association = Table(
    "caracteristica_imovel_association",
    Base.metadata,
    Column("caracteristica_id", Integer, ForeignKey("caracteristicas.id"), primary_key=True),
    Column("imovel_id", Integer, ForeignKey("imoveis.id"), primary_key=True),
)


class Caracteristica(Base):
    __tablename__ = "caracteristicas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    descricao = Column("descricao", String, nullable=False)
    imoveis = relationship("Imovel", secondary=caracteristica_imovel_association, back_populates="caracteristicas")
    
    def __init__(self, descricao):
        self.descricao = descricao

    def __repr__(self):
        return f"Caracteristica [descricao={self.descricao}]"


class Imovel(Base):
    __tablename__ = "imoveis"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    descricao = Column("descricao", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=True, default=True)
    lancamento = Column("lancamento", Boolean, nullable=True, default=False)
    destaque = Column("destaque", Boolean, nullable=True, default=False)
    valor = Column("valor", Float, nullable=False)
    visualizacoes = Column("visualizacoes", Integer, nullable=True, default=0)
    finalidade = Column("finalidade", Integer, ForeignKey("finalidades.id"))
    tipo_imovel = Column("tipo_imovel", Integer, ForeignKey("tipos_imovel.id"))
    pretensao = Column("pretensao", Integer, ForeignKey("pretensoes.id"))
    estado = Column("estado", Integer, ForeignKey("estados.id"))
    cidade = Column("cidade", String, nullable=True)
    endereco = Column("endereco", String, nullable=True)
    complemento = Column("complemento", String, nullable=True)
    sobre_imovel = Column("sobre_imovel", String, nullable=True)
    caracteristicas = relationship("Caracteristica", secondary=caracteristica_imovel_association, back_populates="imoveis")
    area_total = Column("area_total", Float, nullable=True)
    area_construida = Column("area_construida", Float, nullable=True)
    dormitorios = Column("dormitorios", Integer, nullable=True)
    banheiros = Column("banheiros", Integer, nullable=True)
    suites = Column("suites", Integer, nullable=True)
    vagas_garagem = Column("vagas_garagem", Integer, nullable=True)
    vagas_garagem_cobertas = Column("vagas_garagem_cobertas", Integer, nullable=True)
    vagas_garagem_descobertas = Column("vagas_garagem_descobertas", Integer, nullable=True)
    fotos: Mapped[List["Foto"]] = relationship(back_populates="imovel")
    comentarios: Mapped[List["Comentario"]] = relationship(back_populates="imovel")
    interessados: Mapped[List["Interessado"]] = relationship(back_populates="imovel")

    
    def __init__(self, descricao, ativo, lancamento, destaque, valor, visualizacoes, finalidade, tipo_imovel, pretensao, estado, cidade, endereco, complemento, sobre_imovel, area_total, area_construida, dormitorios, banheiros, suites, vagas_garagem, vagas_garagem_cobertas, vagas_garagem_descobertas):
        self.descricao = descricao
        self.ativo = ativo
        self.lancamento = lancamento
        self.destaque = destaque
        self.valor = valor
        self.visualizacoes = visualizacoes
        self.finalidade = finalidade
        self.tipo_imovel = tipo_imovel
        self.pretensao = pretensao
        self.estado = estado
        self.cidade = cidade
        self.endereco = endereco
        self.complemento = complemento
        self.sobre_imovel = sobre_imovel
        self.area_total = area_total
        self.area_construida = area_construida
        self.dormitorios = dormitorios
        self.banheiros = banheiros
        self.suites = suites
        self.vagas_garagem = vagas_garagem
        self.vagas_garagem_cobertas = vagas_garagem_cobertas
        self.vagas_garagem_descobertas = vagas_garagem_descobertas

    def __repr__(self):
        return f"Imovel [descricao={self.descricao}, ativo={self.ativo}, lancamento={self.lancamento}, destaque={self.destaque}, valor={self.valor}, visualizacoes={self.visualizacoes}, finalidade={self.finalidade}, tipo_imovel={self.tipo_imovel}, pretensao={self.pretensao}, estado={self.estado}, cidade={self.cidade}, endereco={self.endereco}, complemento={self.complemento}, sobre_imovel={self.sobre_imovel}, area_total={self.area_total}, area_construida={self.area_construida}, dormitorios={self.dormitorios}, banheiros={self.banheiros}, suites={self.suites}, vagas_garagem={self.vagas_garagem}, vagas_garagem_cobertas={self.vagas_garagem_cobertas}, vagas_garagem_descobertas={self.vagas_garagem_descobertas}]"


class Foto(Base):
    __tablename__ = "fotos"

    id: Mapped[int] = mapped_column(primary_key=True)
    caminho = Column("caminho", String, nullable=False)    
    capa = Column("capa", Boolean, nullable=True, default=False)
    imovel_id: Mapped[int] = mapped_column(ForeignKey("imoveis.id"))
    imovel: Mapped["Imovel"] = relationship(back_populates="fotos")
    
    def __init__(self, caminho, imovel):
        self.caminho = caminho
        self.imovel = imovel

    def __repr__(self):
        return f"Foto [caminho={self.caminho}, imovel={self.imovel}]"
    

class Comentario(Base):
    __tablename__ = "comentarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    texto = Column("texto", String, nullable=False)
    aprovado = Column("aprovado", Boolean, nullable=False, default=False)
    imovel_id: Mapped[int] = mapped_column(ForeignKey("imoveis.id"))
    imovel: Mapped["Imovel"] = relationship(back_populates="comentarios")
    
    def __init__(self, texto, imovel):
        self.texto = texto
        self.imovel = imovel

    def __repr__(self):
        return f"Comentario [texto={self.texto}, imovel={self.imovel}]"
    

class Interessado(Base):
    __tablename__ = "interessados"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    telefone = Column("telefone", String, nullable=False)
    estado = Column("estado", Integer, ForeignKey("estados.id"))    
    cidade = Column("cidade", String, nullable=False)
    imovel_id: Mapped[int] = mapped_column(ForeignKey("imoveis.id"))
    imovel: Mapped["Imovel"] = relationship(back_populates="interessados")
    
    def __init__(self, nome, email, telefone, estado, cidade, imovel):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.estado = estado
        self.cidade = cidade
        self.imovel = imovel

    def __repr__(self):
        return f"Interessado [nome={self.nome}, email={self.email}, telefone={self.telefone}, estado={self.estado}, cidade={self.cidade}, imovel={self.imovel}]"