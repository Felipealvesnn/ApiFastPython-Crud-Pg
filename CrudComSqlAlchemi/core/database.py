from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from core.configs import Settings


engine: AsyncEngine = create_async_engine(Settings.DB_URL, echo=True)

Session: AsyncSession = sessionmaker(
   bind= engine, class_=AsyncSession, expire_on_commit=False,
    autoflush=False, autocommit=False
)
