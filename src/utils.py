import json
import os
from typing import Any, Dict, List, Union

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("api_keys")


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


def get_transactions_rub_to_usd(currency: str) -> Any:
    """Получает курс валюты в рублях по отношению к USD и EUR"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        return response_data["rates"]["RUB"]
    except requests.exceptions.RequestException as ef:
        print(ef)
        return 1.0


def sum_amount(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    total = 0.0
    operation_sum = transaction.get("operationAmount", {})
    currency_code = operation_sum.get("currency", {}).get("code", "")
    amount = float(operation_sum.get("amount", 0.0))
    if currency_code in ["USD", "EUR"]:
        rate_to_rub = get_transactions_rub_to_usd(currency_code)
        total += amount * rate_to_rub
    elif currency_code == "RUB":
        total += amount
    return total


value = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
print(sum_amount(value))
