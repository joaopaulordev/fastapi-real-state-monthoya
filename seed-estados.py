estados = {
('AC', 'Acre'),
('AL', 'Alagoas'),
('AP', 'Amapá'),
('AM', 'Amazonas'),
('BA', 'Bahia'),
('CE', 'Ceará'),
('DF', 'Distrito Federal'),
('ES', 'Espírito Santo'),
('GO', 'Goiás'),
('MA', 'Maranhão'),
('MT', 'Mato Grosso'),
('MS', 'Mato Grosso do Sul'),
('MG', 'Minas Gerais'),
('PA', 'Pará'),
('PB', 'Paraíba'),
('PR', 'Paraná'),
('PE', 'Pernambuco'),
('PI', 'Piauí'),
('RJ', 'Rio de Janeiro'),
('RN', 'Rio Grande do Norte'),
('RS', 'Rio Grande do Sul'),
('RO', 'Rondônia'),
('RR', 'Roraima'),
('SC', 'Santa Catarina'),
('SP', 'São Paulo'),
('SE', 'Sergipe'),
('TO', 'Tocantins')
}

from src.models.entities.imovel import Estado

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db = create_engine("sqlite:///monthoya.db")

def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

db_session = next(get_session_db())
ordered = sorted(estados, key=lambda x: x[0])
for sigla, nome in ordered:
    estado = Estado(descricao=f"{sigla} - {nome}")
    db_session.add(estado)
    db_session.commit()  

print("Estados inseridos com sucesso!")