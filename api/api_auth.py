
from fastapi.security import OAuth2PasswordRequestForm
from core.redis_service import read_from_redis, write_to_redis
from core.security import JWTBearer, create_access_token, create_refresh_token, get_current_user, verify_token_access
from core.utils import verify_password
from depends.get_db import get_db
from models.model_user import ModelUser
from schemas.schema_user import DataToken, RefreshToken, Token
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session


router = APIRouter()

@router.post('/login', response_model=Token)
async def login(userdetails: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(ModelUser).filter(ModelUser.username == userdetails.username).first()  
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="the user not exists")
    
    if not verify_password(userdetails.password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="the password is wrong")
    
    access_token = create_access_token(data={"user_id":str(user.id),
                                             "user_name":user.username,
                                             "user_fullname":user.name,
                                             "user_phone":user.phone,
                                             "is_super_admin":user.is_super_admin
                                             })
    
    refresh_token = create_refresh_token(data={"user_id":str(user.id),
                                            "user_name":user.username,
                                            "user_fullname":user.name,
                                            "user_phone":user.phone,
                                            "is_super_admin":user.is_super_admin
                                            })
    write_to_redis(str(user.id), refresh_token)

    return {"access_token":access_token,"refresh_token":refresh_token,"token_type":"bearer"}

@router.get('/currentUser')
async def get_currentUser(token=Depends(JWTBearer())):

    decoded_token = get_current_user(token)
    return decoded_token


@router.get('/refreshToken', response_model=Token)
async def create_refreshToken(token):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could not Validate Credentials",
                            headers={"WWW-Authenticate": "Bearer"})


    user_info = verify_token_access(token,error)
    server_refresh_token = read_from_redis(user_info["user_id"])


    if not token:
        error

    if token != server_refresh_token:
        error
    
    print(555555555555,user_info)
    access_token = create_access_token(data={"user_id":user_info["user_id"],
                                             "user_name":user_info["user_name"],
                                             "user_fullname":user_info["user_fullname"],
                                             "user_phone":user_info["user_phone"],
                                             "is_super_admin":user_info["is_super_admin"]
                                             })
    
    refresh_token = create_refresh_token(data={"user_id":user_info["user_id"],
                                            "user_name":user_info["user_name"],
                                            "user_fullname":user_info["user_fullname"],
                                            "user_phone":user_info["user_phone"],
                                            "is_super_admin":user_info["is_super_admin"]
                                            })
    
    write_to_redis(str(user_info["user_id"]), refresh_token)


    return {"access_token":access_token,"refresh_token":refresh_token,"token_type":"bearer"}