from uuid import UUID
from pydantic import BaseModel


class UserBase(BaseModel, extra='forbid'):
    id:UUID 
    name: str
    email: str
    phone: str
    username: str
    timezone: str = 'Universal'

class UserCreate(UserBase):
    password: str
    is_super_admin: bool
    is_active:bool

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    username: str | None = None
    timezone: str | None = None
    password: str | None = None
    is_super_admin: bool | None = None
    is_active:bool | None = None
