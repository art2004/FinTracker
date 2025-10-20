from dataclasses import dataclass

@dataclass
class Expense:
    category: str
    amount: float
    date: str

    def to_dict(self):
        return {
            'category': self.category,
            'amount': self.amount,
            'date': self.date
        }

@dataclass
class Category:
    name: str
    total: float = 0.0

    def add_expense(self, amount):
        self.total += amount