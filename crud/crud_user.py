from schemas.schema_user import UserBase, UserUpdate
from sqlalchemy.orm import session
from models.model_user import ModelUser

class User():
    
    def create_user(db: session, user: UserBase):
        user = ModelUser(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_all_users(db: session):
        db_users = db.query(ModelUser).all()
        return db_users
    
    def update_user(user_id:str,db: session,user: UserUpdate):
        db_user = db.query(ModelUser).filter(ModelUser.id == user_id).one_or_none()
        for key, value in user.model_dump().items():
            setattr(db_user, key, value) if value else None
        db.commit()
        db.refresh(db_user)
        return db_user
        
    def delete_user(user_id:str,db: session):
        db_user = db.query(ModelUser).filter(ModelUser.id == user_id).one_or_none()
        db.delete(db_user)
        db.commit()
        return {"msg":f"the user with id = {user_id} has been deleted"}


