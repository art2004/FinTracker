"""
Хранилище теперь работает с PostgreSQL.
"""

from typing import List
from fintracker.database import SessionLocal, ExpenseDB, init_db
from fintracker.models import Expense
from datetime import datetime


def _db_to_model(db_expense: ExpenseDB) -> Expense:
    return Expense(
        category=db_expense.category,
        amount=db_expense.amount,
        date=db_expense.date.isoformat()
    )


def _model_to_db(expense: Expense) -> ExpenseDB:
    return ExpenseDB(
        category=expense.category,
        amount=expense.amount,
        date=datetime.fromisoformat(expense.date)
    )


def load_expenses() -> List[Expense]:
    init_db()  # создаём таблицы, если их нет
    with SessionLocal() as db:
        db_expenses = db.query(ExpenseDB).all()
        return [_db_to_model(exp) for exp in db_expenses]


def save_expenses(expenses: List[Expense]) -> None:
    init_db()
    with SessionLocal() as db:
        # Очищаем таблицу и заливаем заново (простой способ)
        db.query(ExpenseDB).delete()
        for exp in expenses:
            db.add(_model_to_db(exp))
        db.commit()