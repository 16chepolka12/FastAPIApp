# функции для пользователей
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update

from core.schemas import UserPostDTO, UserBaseDTO, UserPatchDTO
from core.database.models import User

counter = 0


async def get_users(session: AsyncSession):
    stmt = select(User)  # запрос в базу данных = select * from users
    result = await session.scalars(stmt)  # выполнение запроса в базу данных
    return [UserBaseDTO.model_validate(model, from_attributes=True) for model in result]


async def create_user(user: UserPostDTO, session: AsyncSession):
    user_object = User(**user.model_dump())  # превратит модель в ключ значение
    session.add(user_object)
    await session.commit()
    await session.refresh(user_object)  # обновляем данные о пользователе в переменной user_object
    return UserBaseDTO.model_validate(user_object, from_attributes=True)


async def delete_user(id: int, session: AsyncSession):
    if not await get_user_by_id(id, session):
        return False
    stmt = delete(User).where(User.id == id)
    # stmt = "DELETE * FROM users WHERE id = ?"
    await session.execute(stmt)
    await session.commit()
    return True


async def get_user_by_id(id: int, session: AsyncSession, alchemy_model: bool = False):
    stmt = select(User).where(User.id == id)
    result = await session.scalar(stmt)
    if result:
        if alchemy_model:
            return result
        return UserBaseDTO.model_validate(result, from_attributes=True)
    return None


async def update_user(id: int, data: UserPatchDTO, session: AsyncSession):
    user = await get_user_by_id(id, session, alchemy_model=True)
    if not user:
        return None

    stmt = update(User).values(**data.model_dump(exclude_none=True))
    await session.execute(stmt)
    await session.commit()
    await session.refresh(user)
    return UserBaseDTO.model_validate(user, from_attributes=True)
