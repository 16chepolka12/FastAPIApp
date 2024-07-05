from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
async def get_all_users() -> dict:
    return {
        "key": "privet"
    }
