from sqlmodel import SQLModel, Field, create_engine, Session, select
from core.configs import settings


engine = create_engine(settings.DB_URL)