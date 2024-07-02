from functools import lru_cache
from sqlalchemy.orm import sessionmaker
from core.config import Settings
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession

@lru_cache()
def __get_connection_string():
    settings = Settings()
    return (
        f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@localhost:5432/"
        f"{settings.DB_NAME}"
    )


SQLALCHEMY_DATABASE_URL = __get_connection_string()

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession)

