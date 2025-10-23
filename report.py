from fintracker.storage import load_expenses
from fintracker.models import Category

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