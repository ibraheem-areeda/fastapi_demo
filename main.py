from fastapi import FastAPI, APIRouter
from api.api import router as app_router

app = FastAPI()

app.include_router(app_router)




# @app.lifespan("startup")
# async def startup():
#     await database.connect()


# @app.lifespan("shutdown")
# async def shutdown():
#     await database.disconnect()