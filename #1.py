from datetime import datetime as dtdt


def get_days_from_today(date):
    try:
        input_date = dtdt.strptime(date, '%Y-%m-%d')

        current_date = dtdt.today()

        difference = (current_date - input_date).days

        return difference
    except ValueError:
        return "Неправильний формат дати. Використовуйте 'РРРР-ММ-ДД'."


today = dtdt.today().strftime('%Y-%m-%d')
result = get_days_from_today("2018-07-11")
print(f"Різниця у днях: {result}")