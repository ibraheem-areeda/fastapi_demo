from fastapi import APIRouter
from api.api_user import router as user_router
from api.api_auth import router as auth_router
from api.api_task import router as task_router

router = APIRouter()
router.include_router(auth_router,tags=["Auth"],prefix="/auth")
router.include_router(user_router,tags=["user"],prefix="/user")
router.include_router(task_router,tags=["task"],prefix="/task")