from datetime import datetime

from src.reports import wastes_by_category
from src.services import filter_by_state
from src.utils import read_file_xls, write_data
from src.views import (
    get_greeting,
    card_number,
    total_sum_amount,
    cashback,
    top_transaction,
    get_currency,
    get_stock_currency,
    create_operations,
)


def main() -> None:
    """Отвечате за основную логику проекта с пользователем"""
    read_operation = read_file_xls("../data/operation.xls")
    user_currency = input('Какую валюту вы хотели бы добавить к файлу?').split(", ")
    user_stock = input("Какие материалы вы хотели бы добавить к файлу?").split(", ")
    data = {'currency': user_currency, "stock": user_stock}
    write_data("user_settings.json", data)
    time = input('Напишите дату и время(Формат - DD.MM.YYYY HH:MM):')
    greeting = get_greeting(time if time else None)
    card_numbers = card_number(read_file_xls("../data/operation.xls"))
    total_sum = total_sum_amount(read_file_xls("../data/operation.xls"), card_numbers)
    cashbacks = cashback(total_sum)
    top = top_transaction(read_file_xls("../data/operation.xls"))
    created = create_operations(greeting, card_numbers, total_sum, cashbacks, top)
    write_data("new.json", created)

    transaction = filter_by_state(
        [
            {
                "Дата операции": "20.06.2024 13:28:27",
                "Дата платежа": "20.06.2024",
                "Номер карты": "*1781",
                "Статус": "OK",
                "Сумма операции": 1020.0,
                "Валюта операции": "RUB",
                "Сумма платежа": 1020.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": 10,
                "Категория": "Фастфуд",
                "MCC": 5814,
                "Описание": "Wilco Food",
                "Бонусы (включая кэшбэк)": 10.00,
                "Округление на инвесткопилку": 0.0,
                "Сумма операции с округлением": 1020.0,
            },
            {
                "Дата операции": "12.06.2024 14:20:34",
                "Дата платежа": "12.06.2024",
                "Номер карты": "*1781",
                "Статус": "OK",
                "Сумма операции": 2000.0,
                "Валюта операции": "RUB",
                "Сумма платежа": 2000.0,
                "Валюта платежа": "RUB",
                "Кэшбэк": None,
                "Категория": "Переводы",
                "MCC": None,
                "Описание": "Алексей П.",
                "Бонусы (включая кэшбэк)": 0,
                "Округление на инвесткопилку": 0.0,
                "Сумма операции с округлением": 2000.0,
            },
        ]
    )
    print(f"Результат просмотра:\n{read_file_xls('new.json')}")
    print(f"Результат обслуживания: \n{transaction}")
    print(f'Отчеты о результатах: \n{wastes_by_category(read_file_xls(read_operation), "food", datetime(2022, 4, 10))}')


if __name__ == "__main__":
    main()
