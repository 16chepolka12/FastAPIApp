from sqlalchemy import Column, Integer, String #объявление таблицы юзеров

from .base import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, unique=True, nullable=False)
    age: int = Column(Integer, nullable=False)
    gender: str = Column(String, nullable=False)
