from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, responses
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.curso_model import CursoModel

from schemas.curso_schema import CursoSchema
from core.deps import get_sesion

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def criar_curso(curso: CursoSchema, db: AsyncSession = Depends(get_sesion)):
    novo_curso = CursoModel(**curso.dict())
    db.add(novo_curso)
    await db.commit()
    return novo_curso

@router.get("/", response_model=List[CursoSchema])
async def listar_cursos(db: AsyncSession = Depends(get_sesion)):
    consulta = await db.execute(select(CursoModel))
    return consulta.scalars().all()