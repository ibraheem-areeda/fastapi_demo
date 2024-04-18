from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import Settings


@lru_cache()
def __get_connection_string():
    settings = Settings()
    return (
        f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@localhost:5432/"
        f"{settings.DB_NAME}"
    )


SQLALCHEMY_DATABASE_URL = __get_connection_string()

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
