import argparse
from fintracker.commands import add_expense, view_expenses, generate_report
def main():
    parser = argparse.ArgumentParser(description="Трекер личных финансов")
    parser.add_argument('--добавить', nargs=2, metavar=('КАТЕГОРИЯ', 'СУММА'), help='Добавить расход: категория сумма')
    parser.add_argument('--отчет', choices=['категории', 'месячный'],
                        help='Сгенерировать отчет: категории или месячный')
    parser.add_argument('--просмотр', choices=['день', 'месяц', 'все'], help='Просмотреть расходы: день, месяц или все')
    parser.add_argument('--вывод', help='Файл для сохранения отчета')
    args = parser.parse_args()
    try:
        if args.добавить:
            category, amount = args.добавить
            add_expense(category, float(amount))
            print(f"Добавлен расход: {category} - {amount} руб.")
        if args.просмотр:
            expenses = view_expenses(args.просмотр)
            for expense in expenses:
                print(f"{expense['date']} - {expense['category']}: {expense['amount']} руб.")
        if args.отчет:
            report = generate_report(args.отчет, args.вывод)
    except ValueError as e:
        print(f"Ошибка: Неверный формат суммы - {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
if __name__ == "__main__":
    main()