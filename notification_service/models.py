# models.py
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:Mypostgresql#1016@postgres_db/notifications"
)

Base = declarative_base()


class UserPreferences(Base):
    __tablename__ = "user_preferences"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    prefers_email = Column(Boolean, default=True)
    prefers_sms = Column(Boolean, default=False)
    prefers_push = Column(Boolean, default=True)


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
