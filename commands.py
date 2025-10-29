from fintracker.storage import load_expenses, save_expenses
from fintracker.models import Expense
from datetime import datetime
from fintracker.report import generate_category_report

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

def generate_report(report_type: str):
    if report_type == 'категории':
        return generate_category_report()
    return "Неизвестный тип отчета"