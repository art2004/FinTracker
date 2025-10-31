"""
Модели данных для финансового трекера.
"""
from dataclasses import dataclass

@dataclass
class Expense:
    """
    Представляет одну запись о расходе.

    Attributes:
        category (str): Категория расхода (например, "еда", "транспорт").
        amount (float): Сумма расхода в рублях.
        date (str): Дата и время в формате ISO (например, "2025-10-29T12:30:00").
    """
    category: str
    amount: float
    date: str

    def to_dict(self):
        """
        Преобразует объект Expense в словарь для сохранения в JSON.

        Returns:
            dict: Словарь с ключами 'category', 'amount', 'date'.
        """
        return {
            'category': self.category,
            'amount': self.amount,
            'date': self.date
        }

@dataclass
class Category:
    """
    Представляет категорию расходов с накопленной суммой.

    Attributes:
        name (str): Название категории.
        total (float): Общая сумма расходов по категории (по умолчанию 0.0).
    """
    name: str
    total: float = 0.0

    def add_expense(self, amount):
        """
        Добавляет сумму к общей сумме категории.

        Args:
            amount (float): Сумма расхода для добавления.
        """
        self.total += amount