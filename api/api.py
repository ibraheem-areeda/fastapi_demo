from fastapi import APIRouter
from api.api_user import router as user_router
router = APIRouter()
router.include_router(user_router,tags=["user"],prefix="/user")
