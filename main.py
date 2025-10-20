import argparse
from fintracker.commands import add_expense
def main():
    parser = argparse.ArgumentParser(description="Трекер личных финансов")
    parser.add_argument('--добавить', nargs=2, metavar=('КАТЕГОРИЯ', 'СУММА'), help='Добавить расход: категория сумма')
    args = parser.parse_args()
    if args.добавить:
        category, amount = args.добавить
        add_expense(category, float(amount))
        print(f"Добавлен расход: {category} - {amount} руб.")

if __name__ == "__main__":
    main()