
from datetime import datetime, timedelta
from typing import Any, Union
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, OAuth2PasswordBearer
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, Request, status
from core.redis_service import  read_from_redis
from depends.get_db import get_db
from models.model_user import ModelUser
from schemas.schema_user import DataToken
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = "c304f5e9e155cbf8df50ddf770f16c77e85261c886df353fffe46507c5c1ae0c"  # created using  $ openssl rand -hex 32   
JWT_REFRESH_SECRET_KEY = "4281b6471be273e0c25594baf66550b8727a24aed792e71c4e937911cf698eea"  # created using  $ openssl rand -hex 32   
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
REFRESH_TOKEN_EXPIRE_MINUTES = 20


def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now()+ timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now()+ timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return encoded_jwt



def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        expire:datetime = datetime.strptime(payload.get("expire"), '%Y-%m-%d %H:%M:%S')

        if id is None:
            raise credentials_exception
        
        if expire < datetime.now():
            raise credentials_exception

    except JWTError as e:
        print(e)
        raise credentials_exception

    return payload

def get_current_user(token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not Validate Credentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    
    
    user_info = verify_token(token, credentials_exception)
    print(user_info)
    refresh_token = read_from_redis(user_info["user_id"])
    user_info["refresh_token"] = refresh_token
    user_info["access_token"] = token

    # user = db.query(ModelUser).filter(ModelUser.id == token.id).first()

    return user_info


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise error
            if not self.verify_jwt(credentials.credentials):
                raise error
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = jwt.decode(jwtoken, SECRET_KEY, algorithms=ALGORITHM)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
    
