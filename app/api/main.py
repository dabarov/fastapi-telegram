from fastapi import APIRouter

from app.api.routes import auth, user

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/telegram/user", tags=["user-actions"])
