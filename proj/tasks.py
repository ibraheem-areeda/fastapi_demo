import asyncio
from twilio.rest import Client

from core.config import Settings
from schemas.schema_user import Masssage
from .custom_task import CustomTask
from proj.celery import app



async def async_send_to_whatsapp(recever_name,phone_number,msg_body):
    account_sid = Settings().ACCOUNT_SID
    auth_token = Settings().AUTH_TOKEN

    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='whatsapp:+14155238886',
    body=f"hello {recever_name}  {msg_body}",
    to=f'whatsapp:{phone_number}'
    )
    await asyncio.sleep(5)

    print(message.sid)
    

    
@app.task(bind=True, base=CustomTask)
def send_to_whatsapp(self,recever_name,phone_number,msg_body):
    asyncio.run(async_send_to_whatsapp(recever_name,phone_number,msg_body))

