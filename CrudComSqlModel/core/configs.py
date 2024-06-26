from  pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://felipe:123456@localhost:5432/teste"
    
    class Config:
        case_sensitive = True


settings = Settings()