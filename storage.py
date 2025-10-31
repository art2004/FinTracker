"""
Модуль для работы с файлом хранения расходов (expenses.json).
"""
import json
import os
from typing import List
from fintracker.models import Expense

DATA_FILE = 'expenses.json'

def load_expenses() -> List[Expense]:
    """
    Загружает список расходов из файла expenses.json.

    Returns:
        List[Expense]: Список объектов Expense. Пустой список, если файл не существует
                           или повреждён.

    Raises:
        json.JSONDecodeError: Если JSON повреждён — возвращается пустой список.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Expense(**item) for item in data]
    except json.JSONDecodeError:
        print("Ошибка: Поврежденный JSON-файл. Начинаем с пустых данных.")
        return []
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
        return []
def save_expenses(expenses: List[Expense]) -> None:
    """
    Сохраняет список расходов в файл expenses.json.

    Args:
        expenses (List[Expense]): Список объектов Expense для сохранения.

    Raises:
        Exception: При ошибке записи выводится сообщение, но программа не падает.
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump([expense.to_dict() for expense in expenses], f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")