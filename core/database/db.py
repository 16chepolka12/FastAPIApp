# подключение к базе данных
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker


class Database:
    # подключение к базе через асинхронный движок
    def __init__(self):
        self.engine: AsyncEngine = create_async_engine(
            url="postgresql+asyncpg://polina:1234@localhost:5432/test_db",
            echo=True
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,  # подключаем session maker к подключении к базе данных
            autocommit=False,  # автоматический коммит после завершения операции отключен
            expire_on_commit=False  # Когда закомичу в бд не закроется пока не выйду из контекст менеджера
        )

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session
