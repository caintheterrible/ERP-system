from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from dotenv import load_dotenv
from app_config.settings.database import engine
from app_config.settings.database_utils import get_postgres_session
from business_modules.core_module.base import Base

load_dotenv()
session= get_postgres_session()


class Employee(Base):
    """
    Base model extension for all Employee model extensions.
    """

    first_name= Column(String, nullable=False)
    last_name= Column(String, nullable=False)
    username= Column(String, unique=True, nullable=False)
    email= Column(String, unique=True, nullable=False)
    password_hash= Column(String, nullable=False)

    employee_id= Column(Integer, unique=True, index=True)

    department_id= Column(Integer, ForeignKey('departments.id'), nullable=True)
    manager_id= Column(Integer, ForeignKey('managers.id'), nullable=False)

    is_active= Column(Boolean, default=False)

    department= relationship('Department', back_populates='employee')

    def __repr__(self):
        return f'<Employee (username={self.username}, email={self.email})>'



# Create all tables
Base.metadata.create_all(bind=engine)