from fastapi import APIRouter
from api.v1.endpoints import users, fk_ekonomi

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(fk_ekonomi.router)

# Tambahkan router untuk fakultas lainnya di sini