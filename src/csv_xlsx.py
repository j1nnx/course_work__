from typing import Dict, List
import pandas as pd


def read_file_from_file_csv(filename: str) -> list:
    """Читает file scv и возвращает список"""
    if filename.endswith(".csv"):
        df = pd.read_csv(filename, encoding="utf-8")
        transactions = df.to_dict(orient="records")
        return transactions
    else:
        return []


def read_file_from_file_xlsx(filename: str) -> List[Dict]:
    """Читает file xlsx и возвращает список"""
    data = pd.read_excel(filename)
    return data.to_dict("records")


# Проверка
print(read_file_from_file_csv('../data/transactions.csv'))
print(read_file_from_file_xlsx('../data/transactions_excel.xlsx'))
