import json
import os
from typing import Dict, List, Union

import requests


def read_transaction_from_file_json(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """Читает транзакции из файла в формате JSON и возвращает список транзакций"""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.decoder.JSONDecodeError:
            return []


def get_transactions_money_from_rubles(transactions: Dict[str, Union[str, float]]) -> float:
    """Возвращает сумму транзакции в ряблях"""
    charge = transactions["charge"]
    currency = transactions.get("currency", "RUB")

    if currency != "RUB":
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/latest?access_key=zreg2uCOFNUBn4Or2wvNJ1VlpSF22ByN&base=RUB&symbols={currency}"
        )
        data = response.json()
        if data["success"]:
            rate = data["quotes"]["currency"]
            charge *= rate
        else:
            raise ValueError("Could not keyword")
    return float(charge)
