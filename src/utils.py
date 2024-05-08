import json
import os
from typing import Dict, List, Union, Any
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('api_keys')


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


def get_transactions_rub_too_usd(currency: str) -> Any:
    """Получаает курс валюты в рублях по отношения к USD и EUR"""
    url = f'https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}'
    try:
        response = requests.get(url, headers={'apikey': API_KEY}, timeout=5)
        response.raise_for_status()
        response_data = response.json()
        return response_data['rates']['RUB']
    except requests.exceptions.RequestException as ef:
        print(ef)
        return 1.0


def sum_amount_from_transactions(transactions: List[Dict]) -> float:
    total = 0.0
    for transact in transactions:
        operation_sum = transact.get('operationAmount', {})
        currency_ = operation_sum.get('currency', {}).get("code")
        amount = float(operation_sum.get('amoumt', 0))
        if currency_ == 'RUB':
            total += amount
        elif currency_ in ['USD', 'EUR']:
            rate = get_transactions_rub_too_usd(currency_)
            total += amount * rate
        else:
            print(f'Валюта не известна: {currency_}')
    return total


value = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }

print(get_transactions_rub_too_usd(value('currency')))









