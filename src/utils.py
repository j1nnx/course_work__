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
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}'
    headers = {'apikey': API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        return response_data['rates']['RUB']
    except requests.exceptions.RequestException as ef:
        print(ef)
        return 1.0


def sum_amount_from_transactions(transactions: List[Dict]) -> float:
    """Returns the sum if transactions in Rub"""
    total = 0.0
    for transact in transactions:
        operation_sum = transact.get('operationAmount', {})
        currency_code = operation_sum.get('currency', {}).get('code', '')
        amount = float(operation_sum.get('amount', 0.0))
        if currency_code in ['USD', 'EUR']:
            rate_to_rub = get_transactions_rub_to_usd(currency_code)
            total += amount * rate_to_rub
        elif currency_code == 'RUB':
            total += amount
    return total


