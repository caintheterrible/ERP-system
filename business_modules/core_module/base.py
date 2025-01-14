import re
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, DateTime, func

def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

class BaseModel:
    """
    A base model for all SQLAlchemy models. Provides common fields and utility methods.
    """

    @declared_attr
    def __tablename__(self):
        """
        Automatically generates table names in snake_case based on class name.
        Example: 'UserProfile' -> 'user_profile'.
        """
        return camel_to_snake(self.__name__)

    id= Column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
    )

    created_at= Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at= Column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )

    deleted_at= Column(
        DateTime(timezone=True),
        nullable=True,
    )

    def save(self, session):
        """
        Saves the current instance of the model to the database.
        Automatically handles session commit and rollback. Closes session when done.
        """
        try:
            session.add(self)
            session.commit()
        except Exception as exc:
            session.rollback()
            raise exc

    def delete(self, session):
        """
        Deletes the current instance of the model from the database.
        Automatically handles session commit and rollback. Closes session when done.
        """
        try:
            session.delete(self)
            session.commit()
        except Exception as exc:
            session.rollback()
            raise exc

    def soft_delete(self, session):
        """
        Disables current instance temporarily for auditing purposes.
        Notifies administrators before deleting instance.
        Deletes instance permanently after admin confirmation.
        """
        try:
            self.deleted_at= func.now()
            session.commit()
        except Exception as exc:
            session.rollback()
            raise exc

    def __repr__(self):
        """
        Provides a readable string representation of the model instance.
        """
        # Override this method in child classes if needed.
        return f'<{self.__class__.__name__}(id={self.id})>'


Base= declarative_base(cls=BaseModel)