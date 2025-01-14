# Connection management

import os
from mongoengine import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL=f'postgresql://{os.getenv('POSTGRESQL_DATABASE_USER')}:' \
    f'{os.getenv('POSTGRESQL_DATABASE_PASSWORD')}@' \
    f'{os.getenv('POSTGRESQL_DATABASE_HOST')}:' \
    f'{os.getenv('POSTGRESQL_DATABASE_PORT')}/' \
    f'{os.getenv('POSTGRESQL_DATABASE_NAME')}'

engine=  create_engine(DATABASE_URL) # For postgresql database communications
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine) # Create sessions

mongo_client= connect(
    db=os.getenv('MONGO_DATABASE_NAME'),
    host=os.getenv('MONGO_URI'),
    port= 27017,
)

