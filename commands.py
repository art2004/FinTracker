from fintracker.storage import load_expenses, save_expenses
from fintracker.models import Expense
from datetime import datetime

def add_expense(category: str, amount: float):
    expenses = load_expenses()
    expense = Expense(category=category, amount=amount, date=datetime.now().isoformat())
    expenses.append(expense)
    save_expenses(expenses)