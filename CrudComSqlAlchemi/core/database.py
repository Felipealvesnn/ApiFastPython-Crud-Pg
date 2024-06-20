from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from core.configs import settings  # Importe a instância, não a classe


engine: AsyncEngine = create_async_engine(settings.DB_URL, echo=True)

Session: sessionmaker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)
