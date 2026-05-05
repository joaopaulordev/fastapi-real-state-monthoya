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