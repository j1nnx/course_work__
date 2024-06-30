from typing import Any

from src.utils import setup_logger, write_data

logger = setup_logger()


def filter_by_state(operation: Any) -> Any:
    """
    Функция принимает на вход список транзакций и возвращает новый список,
    содержащий только новый список, содержащий только те словари, у которых ключ содержит переданное значение
    """
    data = []
    for transaction in operation:
        if "Переводы" in transaction["Категория"] and transaction["Описание"].endswith("."):
            data.append(transaction)
    logger.info("Функция filter_by_state работает успешно")
    write_data("results.json", data)
    return data
