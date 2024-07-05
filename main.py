import uvicorn

from app import app

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=True  # автоматический перезапуск при изменении любого файла в проекте
    )
