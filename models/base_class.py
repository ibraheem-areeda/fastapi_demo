from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .model_user import ModelUser