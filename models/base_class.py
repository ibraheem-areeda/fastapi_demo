from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

class Base(DeclarativeBase,AsyncAttrs):
    def asdict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}