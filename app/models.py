from sqlalchemy import BigInteger, DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """Base for models"""


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    username = mapped_column(String(100), unique=True, nullable=False, index=True)
    user_id = mapped_column(BigInteger, unique=True, nullable=False, index=True)
    first_name = mapped_column(String(100), nullable=True)
    photo_url = mapped_column(Text, nullable=True)
    auth_date = mapped_column(DateTime(timezone=True), nullable=False)
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
