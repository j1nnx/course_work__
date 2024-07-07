from datetime import datetime, timedelta
from typing import Any, Optional
from src.utils import read_file_xls
import pandas as pd

from src.utils import setup_logger, write_data

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


def filter_transactions(
    transactions: pd.DataFrame, category: str, start_date: str
) -> pd.DataFrame:
    """
    Фильтрация транзакций по категории и дате.
    """
    end_date = datetime.strptime(start_date, "%d.%m.%Y") + timedelta(days=90)
    filtered_transactions = transactions[
        (transactions["category"] == category)
        & (transactions["data_payment"] >= start_date)
        & (transactions["data_payment"] < end_date.strftime("d.%m.%Y"))
    ]
    return filtered_transactions.to_dict("records")


def main_reports() -> None:
    read_operation = read_file_xls("../data/operation.xlsx")
    print(
        f"Отчеты о результатах: "
        f'{filter_transactions(read_file_xls(read_operation), "food", datetime(2024, 5, 10).strftime("%Y-%m-%d"))}'
    )
