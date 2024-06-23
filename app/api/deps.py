from typing import Annotated, AsyncGenerator

import jwt
from aiogram import Bot
from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.api.services.user import get_user_by_user_id
from app.core.config import settings
from app.models import User

engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI), echo=True)
SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_db)]


async def get_current_user(request: Request, session: SessionDep) -> User:
    auth_exception = HTTPException(401, "Authentication is required")
    if not (token := request.cookies.get(settings.AUTH_COOKIE_NAME)):
        raise auth_exception
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        raise auth_exception
    if not (user_id := payload.get("user_id")):
        raise auth_exception
    if not (user := await get_user_by_user_id(session, user_id)):
        raise auth_exception
    return user


CurrentUserDep = Annotated[User, Depends(get_current_user)]


async def get_telegram_bot() -> AsyncGenerator[Bot, None]:
    async with Bot(token=settings.BOT_TOKEN) as bot:
        yield bot


TelegramBotDep = Annotated[Bot, Depends(get_telegram_bot)]
