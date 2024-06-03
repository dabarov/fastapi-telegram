from sqlalchemy import BigInteger, Column, DateTime, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    user_id = Column(BigInteger, unique=True, nullable=False, index=True)
    first_name = Column(String(100), nullable=True)
    photo_url = Column(Text, nullable=True)
    auth_date = Column(DateTime(timezone=True), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
