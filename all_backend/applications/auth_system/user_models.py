from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os


load_dotenv()

# Connection management
DATABASE_URL=f'postgresql://{os.getenv('POSTGRESQL_DATABASE_USER')}:' \
    f'{os.getenv('POSTGRESQL_DATABASE_PASSWORD')}@' \
    f'{os.getenv('POSTGRESQL_DATABASE_HOST')}:' \
    f'{os.getenv('POSTGRESQL_DATABASE_PORT')}/' \
    f'{os.getenv('POSTGRESQL_DATABASE_NAME')}'

engine=  create_engine(DATABASE_URL) # For database communications
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine) # Create sessions
Base= declarative_base()

# User model
class Employee(Base):
    __tablename__= 'users'

    id= Column(Integer, primary_key=True, index=True)
    username= Column(String, unique=True, nullable=False)
    email= Column(String, unique=True, nullable=False)
    password_hash= Column(String, nullable=False)

    is_active= Column(Boolean, default=False)

    def __repr__(self):
        return f'<User(username={self.username}, email={self.email})>'


# Create tables
Base.metadata.create_all(bind=engine)