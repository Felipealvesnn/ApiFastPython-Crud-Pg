# models/curso_model.py
from sqlmodel import SQLModel, Field

class CursoModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    titulo: str
    descricao: str
    carga_horaria: int
