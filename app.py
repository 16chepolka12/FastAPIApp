# Инициализация объектов FastAPI
from fastapi import FastAPI

from api import main_router

app = FastAPI(
    title="My FastAPI app",
    description="by 16chepolka12"
)
app.include_router(main_router)
