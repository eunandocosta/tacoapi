from sqlalchemy import Column, Integer, String, Float
from database import Base

class Alimento(Base):
    __tablename__ = 'alimentos'

    id = Column(Integer, primary_key=True, index=True)
    Nome = Column(String(255), index=True)
    Umidade = Column(Float)
    Energia_kcal = Column(Float)
    Energia_kj = Column(Float)
    Proteina = Column(Float)
    Lipideos = Column(Float)
    Colesterol = Column(Float)
    Carboidrato = Column(Float)
    Fibra_Alimentar = Column(Float)
    Cinzas = Column(Float)
    Calcio = Column(Float)
    Magnesio = Column(Float)
