import json
import os
from fintracker.models import Expense

DATA_FILE = 'expenses.json'

def load_expenses():
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return [Expense(**item) for item in data]
    except json.JSONDecodeError:
        print("Ошибка: Поврежденный JSON-файл. Начинаем с пустых данных.")
        return []
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump([expense.to_dict() for expense in expenses], f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")