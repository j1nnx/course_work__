from datetime import datetime
from typing import Any

from src.reports import filter_transactions_by_category_and_date
from src.utils import read_file_xls, setup_logger, write_data

logger = setup_logger()


def filter_by_state(operation: Any) -> Any:
    """
    Функция принимает на вход список транзакций и возвращает новый список,
    содержащий только те словари, у которых ключ содержит переданное значение
    """
    data = []
    for transaction in operation:
        if "Переводы" in transaction["Категория"] and transaction["Описание"].endswith("."):
            data.append(transaction)
    logger.info("Функция filter_by_state работает успешно")
    write_data("results.json", data)
    return data


def main_services() -> None:
    """Главная функция в этом модуле"""
    read_operation = read_file_xls("../data/operation.xlsx")
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
    print(
        f"Отчеты о результатах: "
        f'{filter_transactions_by_category_and_date(read_file_xls(read_operation), "food", datetime(2024, 5, 10).strftime("%Y-%m-%d"))}'
    )
