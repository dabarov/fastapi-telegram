from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas.user import UserTelegramData
from app.models import User


async def get_user_by_user_id(session: AsyncSession, user_id: int) -> User | None:
    """Returns a single user object or none if not found"""
    query = select(User).where(User.user_id == user_id)
    return (await session.execute(query)).scalar_one_or_none()


async def create_or_update_user(
    session: AsyncSession,
    user_data: UserTelegramData,
) -> None:
    """
    User is created if doesn't exist based on user_id.
    If exists check whether there are modified values.
    Updates modified values.
    """
    if (user := await get_user_by_user_id(session, user_data.user_id)) is None:
        session.add(User(**user_data.model_dump()))
        return
    db_values = user.__dict__
    if values_to_update := {
        key: value
        for key, value in user_data.model_dump().items()
        if db_values[key] != value
    }:
        await session.execute(
            update(User)
            .where(User.user_id == user_data.user_id)
            .values(values_to_update)
        )
