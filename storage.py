import json
import os
from fintracker.models import Expense

DATA_FILE = 'expenses.json'

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        return [Expense(**item) for item in data]

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump([expense.to_dict() for expense in expenses], f, indent=2, ensure_ascii=False)