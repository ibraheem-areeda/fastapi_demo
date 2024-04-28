from fastapi import FastAPI, APIRouter
from api.api import router as app_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(app_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.lifespan("startup")
# async def startup():
#     await database.connect()


# @app.lifespan("shutdown")
# async def shutdown():
#     await database.disconnect()