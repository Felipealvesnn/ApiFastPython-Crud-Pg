from fastapi import APIRouter
from api.v1 import curso

api_router = APIRouter()

api_router.include_router(curso.router, prefix="/curso", tags=["curso"])