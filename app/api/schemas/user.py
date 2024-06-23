from datetime import datetime

from pydantic import BaseModel


class UserTelegramData(BaseModel):
    """Mutable fields for user model"""

    user_id: int
    first_name: str
    username: str
    photo_url: str
    auth_date: datetime


class TelegramMessageRequest(BaseModel):
    """Model for sending telegram message to current user"""

    message: str
