from fintracker.storage import load_expenses
from fintracker.models import Category
from datetime import datetime
def generate_category_report():
    expenses = load_expenses()
    categories = {}
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = Category(name=expense.category)
        categories[expense.category].add_expense(expense.amount)
    report = "Отчет по категориям:\n"
    for category in categories.values():
        report += f"{category.name}: {category.total:.2f} руб.\n"
    return report

def generate_monthly_report():
    expenses = load_expenses()
    months = {}
    for expense in expenses:
        date = datetime.fromisoformat(expense.date)
        month_key = f"{date.year}-{date.month:02d}"
        if month_key not in months:
            months[month_key] = 0.0
        months[month_key] += expense.amount
    report = "Месячный отчет:\n"
    for month, total in months.items():
        report += f"{month}: {total:.2f} руб.\n"
    return report