from fastapi import APIRouter

from crud import users
from core.schemas import UserBaseDTO, UserPostDTO

router = APIRouter()


@router.get("")
async def get_all_users() -> list[UserBaseDTO] | list:
    return await users.get_users()


@router.post("")
async def create_user(user: UserPostDTO) -> UserBaseDTO:
    return await users.create_user(user)


@router.delete("")
async def pop_user(id: int) -> bool:
    return await users.delete_user(id)
