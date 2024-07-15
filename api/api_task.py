from fastapi import APIRouter, Depends

from core.security import JWTBearer
from proj import tasks 
from schemas.schema_user import Masssage 

router = APIRouter()

@router.get("/all")
async def get_all_users(token=Depends(JWTBearer())):
    return {"Hello":"ibraheem"}

@router.post("/send/whatsapp")
async def get_all_users(msg:Masssage,token=Depends(JWTBearer())):
    recever_name = msg.recever_name
    phone_number = msg.phone_number
    msg_body = msg.msg_body

    task = tasks.send_to_whatsapp.delay(recever_name,phone_number,msg_body)
    # print(task.status)
    # while True:
    #     print(task.status)
    #     if task.ready():
    #         break
    return task.id