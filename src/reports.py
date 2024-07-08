from datetime import datetime, timedelta

import pandas as pd

from src.utils import setup_logger

logger = setup_logger()


def read_transactions_xlsx(file_path: str) -> pd.DataFrame:
    """
    Чтение финансовых операций из XLSX-файла.
    """
    logger.info(f"Чтение данных из файла {file_path}")
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        return pd.DataFrame()


def filter_transactions(transactions: pd.DataFrame, category: str, start_date: str) -> pd.DataFrame:
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
    pass
