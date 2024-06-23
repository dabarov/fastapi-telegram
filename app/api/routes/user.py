from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.api.deps import CurrentUserDep, TelegramBotDep
from app.api.schemas.user import TelegramMessageRequest

router = APIRouter()


@router.get("/avatar")
async def get_current_user_avatar(current_user: CurrentUserDep) -> RedirectResponse:
    if current_user.photo_url:
        return RedirectResponse(current_user.photo_url)
    raise HTTPException(404, "Current user does not have avatar")


@router.post("/send-message")
async def send_message_to_current_user(
    message_request: TelegramMessageRequest,
    current_user: CurrentUserDep,
    telegram_bot: TelegramBotDep,
) -> None:
    await telegram_bot.send_message(current_user.user_id, message_request.message)
