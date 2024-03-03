import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)  # Замінюємо всі символи, крім цифр

    # Перевіряємо, чи номер починається на '38', інакше додаємо до номера '+'
    if cleaned_number.startswith('38'):
        cleaned_number = '+' + cleaned_number
    else:
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

normalized_numbers = [normalize_phone(number) for number in phone_numbers]
print("Нормалізовані номери:", normalized_numbers)