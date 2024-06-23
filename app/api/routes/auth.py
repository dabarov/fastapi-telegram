import hmac
from datetime import datetime

import jwt
from fastapi import APIRouter, HTTPException, Query
from fastapi.requests import Request
from fastapi.responses import RedirectResponse

from app.api.deps import SessionDep
from app.api.schemas.user import UserTelegramData
from app.api.services.user import create_or_update_user
from app.core.config import settings

router = APIRouter()


def has_correct_hash(request: Request) -> bool:
    """More on this here: https://core.telegram.org/widgets/login#checking-authorization"""
    params = request.query_params._dict
    expected_hash = params.pop("hash")
    sorted_params = sorted(f"{x}={y}" for x, y in params.items())
    data_check_bytes = "\n".join(sorted_params).encode()
    computed_hash = hmac.new(settings.bot_token_hash_bytes, data_check_bytes, "sha256")
    return hmac.compare_digest(computed_hash.hexdigest(), expected_hash)


@router.get("/telegram/callback")
async def telegram_callback(
    session: SessionDep,
    request: Request,
    user_id: int = Query(alias="id"),
    first_name: str = Query(),
    username: str = Query(),
    photo_url: str = Query(),
    auth_date: datetime = Query(),
) -> RedirectResponse:
    if not has_correct_hash(request):
        raise HTTPException(401, detail="Authentication failed")

    await create_or_update_user(
        session,
        UserTelegramData(
            user_id=user_id,
            username=username,
            first_name=first_name,
            photo_url=photo_url,
            auth_date=auth_date,
        ),
    )
    await session.commit()
    token = jwt.encode({"user_id": user_id}, settings.SECRET_KEY, algorithm="HS256")
    response = RedirectResponse("/")
    response.set_cookie(key=settings.AUTH_COOKIE_NAME, value=token)
    return response


@router.get("/logout")
async def logout() -> RedirectResponse:
    response = RedirectResponse("/")
    response.delete_cookie(key=settings.AUTH_COOKIE_NAME)
    return response
