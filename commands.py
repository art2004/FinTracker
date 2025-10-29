from fintracker.storage import load_expenses, save_expenses
from fintracker.models import Expense
from datetime import datetime
from fintracker.report import generate_category_report, generate_monthly_report

def add_expense(category: str, amount: float):
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
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

def generate_report(report_type: str, output_file: str = None):
    if report_type == 'категории':
        report = generate_category_report()
    elif report_type == 'месячный':
        report = generate_monthly_report()
    else:
        report = "Неизвестный тип отчета"

    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(report)
            print(f"Отчет сохранён в {output_file}")
        except Exception as e:
            print(f"Ошибка при записи файла: {e}")
    else:
        print(report)

    return report