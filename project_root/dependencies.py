# dependencies.py

from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
from database.db_session import engine

# 🌀 Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🧩 Dependency function
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
