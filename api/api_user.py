from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}")
async def user_info(user_id:int):
    return {"user_id": user_id}

@router.post("/create")
async def create_user():
    pass
