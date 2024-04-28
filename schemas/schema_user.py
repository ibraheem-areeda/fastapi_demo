from uuid import UUID
from pydantic import BaseModel


class UserBase(BaseModel):
    id:UUID 
    name: str
    email: str
    phone: str
    username: str
    timezone: str = 'Universal'
    access_token: str | None =  None
    refresh_token: str | None = None

class UserCreate(BaseModel):
    name: str
    email: str
    phone: str
    username: str
    timezone: str = 'Universal'
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

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class DataToken(BaseModel):
    id: str | None = None   

class RefreshToken(BaseModel):
    refresh_token:str 

class UserDetails(BaseModel):
    username: str | None = None
    password: str | None = None