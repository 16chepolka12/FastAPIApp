from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from crud import users
from core.schemas import UserBaseDTO, UserPostDTO, UserPatchDTO
from core.database import database_helper

router = APIRouter()


@router.get("")
async def get_all_users(
        session: AsyncSession = Depends(database_helper.session_getter)
) -> list[UserBaseDTO] | list:
    return await users.get_users(session)


@router.post("")
async def create_user(
        user: UserPostDTO,
        session: AsyncSession = Depends(database_helper.session_getter)
) -> UserBaseDTO:
    return await users.create_user(user, session)


@router.delete("/{user_id}")
async def pop_user(
        user_id: int,
        session: AsyncSession = Depends(database_helper.session_getter)
) -> bool:
    return await users.delete_user(user_id, session)


@router.get("/{user_id}")
async def get_user_by_id(
        user_id: int,
        session: AsyncSession = Depends(database_helper.session_getter)
) -> UserBaseDTO | None:
    return await users.get_user_by_id(user_id, session)


@router.patch("/{user_id}")
async def update_user(
        user_id: int,
        data: UserPatchDTO,
        session: AsyncSession = Depends(database_helper.session_getter)
) -> UserBaseDTO | None:
    return await users.update_user(user_id, data, session)
