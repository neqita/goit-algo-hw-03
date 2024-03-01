from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        days_until_birthday = (birthday_date - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_date.weekday() in [5, 6]:
                next_monday = today + timedelta(days=(7 - today.weekday()) + 1)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": next_monday.strftime("%Y.%m.%d")})
            else:
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.03"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)