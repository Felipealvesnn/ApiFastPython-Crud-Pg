from typing import Optional
from pydantic import BaseModel as SCbaseModel

class CursoSchema(SCbaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True

cursobase = CursoSchema()