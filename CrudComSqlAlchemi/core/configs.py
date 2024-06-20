from typing import List
from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg//felipe:123456@localhost:5432/teste"
    DBBasemodel = declarative_base()

    class Config:
        case_sensitive = True