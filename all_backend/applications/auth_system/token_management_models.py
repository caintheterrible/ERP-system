from sqlalchemy import Column, Integer, String, Datetime, Boolean
from sqlalchemy.orm import sessionmaker

from all_backend.applications.auth_system.user_models import SessionLocal
from user_models import Base
import datetime


class RevokedToken(Base):
    __tablename__='revoked_tokens'

    id= Column(Integer, primary_key=True, index=True)
    token= Column(String, nullable=False)
    revoked_at= Column(Datetime, default=  datetime.datetime.now)


# Revoke token
def revoke_token(token:str):
    session= SessionLocal()
    try:
        revoked_token= RevokedToken(
            token=token,
        )
        session.add(revoked_token)
        session.commit()
    finally:
        session.close()

# Check if token is revoked or not
def is_token_revoked(token:str)-> bool:
    session= SessionLocal()
    try:
        revoked_token= session.query(RevokedToken).filter(RevokedToken.token== token)
        return revoked_token is not None
    finally:
        session.close()