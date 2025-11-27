"""
Модуль для работы с PostgreSQL через SQLAlchemy.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Настройки подключения (можно вынести в .env потом)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:1224@localhost:5432/finance_tracker"
)

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class ExpenseDB(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    amount = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)


# Создаём таблицы при первом запуске
def init_db():
    Base.metadata.create_all(bind=engine)