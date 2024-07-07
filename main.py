import uvicorn
from asyncio import run

from app import app
from core.database import database_helper
from core.database.models import Base


async def create_tables():
    async with database_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    run(create_tables())
    uvicorn.run(
        "main:app",
        reload=True  # автоматический перезапуск при изменении любого файла в проекте
    )

