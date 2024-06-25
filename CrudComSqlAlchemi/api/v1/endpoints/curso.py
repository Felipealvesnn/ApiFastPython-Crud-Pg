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
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos = result.scalars().all()
        return cursos
    
@router.get("/{curso_id}", response_model=CursoSchema)
async def buscar_curso(curso_id: int, db: AsyncSession = Depends(get_sesion)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none().first()
        if not curso:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        return curso
    
@router.put("/{curso_id}", response_model=CursoSchema)
async def atualizar_curso(curso_id: int, curso: CursoSchema, db: AsyncSession = Depends(get_sesion)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        curso_db = await session.execute(query)
        curso_db = curso_db.scalar_one_or_none()
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        for campo, valor in curso.dict().items():
            setattr(curso_db, campo, valor)
        await db.commit()
        return curso_db
    
@router.delete("/{curso_id}", response_class=responses.Response)
async def deletar_curso(curso_id: int, db: AsyncSession = Depends(get_sesion)):
    async with db as session:
        query = select(CursoModel).filter(CursoModel.id == curso_id)
        curso_db = await session.execute(query)
        curso_db = curso_db.scalar_one_or_none()
        if not curso_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
        await db.delete(curso_db)
        await db.commit()
        return responses.Response(status_code=status.HTTP_204_NO_CONTENT)