# schemas/curso_schema.py
from typing import Optional
from sqlmodel import SQLModel

class CursoSchema(SQLModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    carga_horaria: int
