from fintracker.storage import load_expenses, save_expenses
from fintracker.models import Expense
from datetime import datetime

def add_expense(category: str, amount: float):
    expenses = load_expenses()
    expense = Expense(category=category, amount=amount, date=datetime.now().isoformat())
    expenses.append(expense)
    save_expenses(expenses)
def view_expenses(period: str):
    expenses = load_expenses()
    today = datetime.now().date()
    if period == 'день':
        return [e.to_dict() for e in expenses if datetime.fromisoformat(e.date).date() == today]
    elif period == 'месяц':
        return [e.to_dict() for e in expenses if datetime.fromisoformat(e.date).date().month == today.month]
    return [e.to_dict() for e in expenses]