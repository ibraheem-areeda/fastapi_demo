from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from depends.get_db import get_db
from schemas.schema_user import UserBase,UserCreate, UserReturn, UserUpdate
from crud.crud_user import User
from typing import Annotated
from core.security import JWTBearer, get_current_user, oauth2_scheme


router = APIRouter()

@router.get("/all", response_model=list[UserBase])
async def get_all_users(token: Annotated[str, Depends(JWTBearer())],db: Session = Depends(get_db)):
    return User.get_all_users(db)

@router.post("/create",response_model=UserReturn)
async def create_user(user:UserCreate,  db: Session = Depends(get_db)):
    return await User.create_user(db=db, user=user)

@router.put("/update/{user_id}",response_model=UserBase)
async def update_user(user_id:str,user:UserUpdate,db:Session = Depends(get_db)):
    return User.update_user(user_id,db,user)

@router.delete("/delete/{user_id}")
async def delete_user(user_id:str,db:Session = Depends(get_db)):
    return User.delete_user(user_id,db)