from fastapi import APIRouter

from app.auth.routes import router as auth_routes


api_router = APIRouter()
api_router.include_router(auth_routes)
