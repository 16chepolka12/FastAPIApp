# схема данных для юзеров

# DTO - Data Transfer Object
# POST -> GET

# id, username, age, gender
# UserPostDTO

from enum import Enum

from pydantic import BaseModel


class Gender(str, Enum):
    man = "man"
    woman = "woman"


class UserPostDTO(BaseModel):
    username: str
    age: int
    gender: Gender


class UserBaseDTO(UserPostDTO):
    id: int
