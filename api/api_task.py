from fastapi import APIRouter, Depends

from core.security import JWTBearer 

router = APIRouter()

@router.get("/all")
async def get_all_users(token=Depends(JWTBearer())):
    
    return {"Hello":"ibraheem"}