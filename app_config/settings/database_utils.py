from .database import SessionLocal, mongo_client
from contextlib import contextmanager

session= SessionLocal()

@contextmanager
def get_postgres_session():
    """Get a new PostgreSQL session."""
    try:
        yield session
    except Exception as exc:
        raise exc
    finally:
        session.close()

def get_mongo_database():
    """Get the MongoDB database instance."""
    return mongo_client