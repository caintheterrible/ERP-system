from sqlalchemy import Column, Integer, String, DateTime
from .models.base import Base
import datetime


class RevokedToken(Base):
    __tablename__='revoked_tokens'

    id= Column(Integer, primary_key=True, index=True)
    token= Column(String, nullable=False)
    revoked_at= Column(DateTime, default=  datetime.datetime.now)