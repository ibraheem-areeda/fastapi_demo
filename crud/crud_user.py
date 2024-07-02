from fastapi import Depends
from sqlalchemy import insert, select
from core.utils import hash_pass
from depends.get_db import get_db
from schemas.schema_user import UserBase, UserCreate, UserUpdate
from sqlalchemy.orm import Session
from models.model_user import ModelUser
from fastapi import HTTPException
class User():
    
    async def create_user(user:UserCreate,db:Session ):

        user.password = hash_pass(user.password)
        user_db = ModelUser(**user.model_dump())
        try:
            async with db.begin():
                    
                    db.add(user_db)
                    db.commit()
                    db.refresh(user_db)
        except:
            raise HTTPException(status_code=403, detail="User already exists")
        return user
    
    def get_all_users(db: Session):
        db_users = db.query(ModelUser).all()
        return db_users
    
    def update_user(user_id:str,db: Session,user: UserUpdate):
        db_user = db.query(ModelUser).filter(ModelUser.id == user_id).one_or_none()
        for key, value in user.model_dump().items():
            setattr(db_user, key, value) if value else None
        db.commit()
        db.refresh(db_user)

        return db_user
        
    def delete_user(user_id:str,db: Session):
        db_user = db.query(ModelUser).filter(ModelUser.id == user_id).one_or_none()
        db.delete(db_user)
        db.commit()
        return {"msg":f"the user with id = {user_id} has been deleted"}


