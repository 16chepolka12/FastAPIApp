from fastapi import APIRouter

from .users import router as user_router

main_router = APIRouter()  # Главный роутер, на него будем вешать другие роутеры
main_router.include_router(user_router)
