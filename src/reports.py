from datetime import timedelta
from typing import Any, Dict, Optional, Union

import pandas as pd

from src.utils import read_file_xls, setup_logger, write_data

# reader_operation = read_file_xls("../data/operation.xls")
logger = setup_logger()


def report_to_file() -> Any:
    """Функция, которая принимает на вход список транзакций
    и возвращает новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""

    def decorator(function: Any) -> Any:
        def wrapper(operation: pd.DataFrame, category: str, date: Optional[pd.Timestamp] = None) -> Any:
            try:
                data = function(operation, category, date)
                write_data("result.json", data)
                logger.info(f"Операция выполнена успешно! Result - {data}")
                return data
            except Exception as e:
                logger.error(f"Ошибка в функции {function.__name__}: {e}")
                return None

        return wrapper

    return decorator


@report_to_file()
def wastes_by_category(transactions: pd.DataFrame, category: str, date: Optional[pd.Timestamp] = None) -> Any:
    """Функция, которая принимает на вход список транзакций
    и возвращает новый список, содержащий только те словари, у которых ключ содержит переданное в функцию значение."""
    transactions = pd.DataFrame(transactions)
    if date is None:
        date = pd.to_datetime("today")
    else:
        date = pd.to_datetime(date)
    result: Dict[str, Union[Dict[Any, Any], str, float]] = {}
    three_months_ago = date - timedelta(days=90)
    transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"])
    total = -transactions[
        (transactions["Дата операции"] >= three_months_ago)
        & (transactions["Дата операции"] <= date)
        & (transactions["Категория"] == category)
    ]["Сумма операции"]
    if total.any():
        result["amount"] = total.to_dict()
        result["category"] = category
        result["total"] = total.sum()

    logger.info(f"Successfully operation! Result - {result}")
    return result
