# функции для пользователей
from database import database_list
from core.schemas import UserPostDTO, UserBaseDTO

counter = 0


async def get_users():
    # from core.schemas import UserBaseDTO
    # database_list.append(
    #     UserBaseDTO(
    #         id=1,
    #         username="16chepolka12",
    #         age=17,
    #         gender='woman'
    #     )
    # )
    return database_list


async def create_user(user: UserPostDTO):
    global counter
    post_user = user.model_dump()
    post_user["id"] = counter + 1
    counter += 1
    user_full_model = UserBaseDTO.model_validate(
        post_user,
    )
    database_list.append(user_full_model)
    return user_full_model


async def delete_user(id: int):
    for user in database_list:
        if user.id == id:
            database_list.pop(database_list.index(user))
            return True
    return False
