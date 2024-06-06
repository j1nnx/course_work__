import json
from pathlib import Path
from typing import Any, Dict, List

from src.external_api import get_currency_rate
from src.logger import setup_logger

logger = setup_logger()


def read_transaction_from_file_json(file_path: Path) -> List[Dict[str, Any]]:
    """Считывает транзакции из JSON-файла."""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        else:
            return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Ошибка при чтении JSON-файла: {e}")
        return []


def sum_amount(transaction: Dict[str, Any]) -> float:
    """Возвращает сумму транзакции в рублях."""
    total = 0.0
    operation_sum = transaction.get("operationAmount", {})
    currency_code = operation_sum.get("currency", {}).get("code", "")
    amount = float(operation_sum.get("amount", 0.0))
    if currency_code in ["USD", "EUR"]:
        rate_to_rub = get_currency_rate(currency_code)
        total += amount * rate_to_rub
    elif currency_code == "RUB":
        total += amount
        logger.info("Function sum_amount completed successfully")
        return total
    else:
        logger.error("Something went wrong with the sum_amount function: %(error)s")
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

sum_amount(value)
