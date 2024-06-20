from core.configs import Settings

from sqlalchemy import Column, Integer, String


class CursoModel(Settings.DBBasemodel):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(100))
    aulas = Column(Integer)
    horas:int = Column(Integer)

