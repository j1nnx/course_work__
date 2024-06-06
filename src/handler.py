import json
import re
from collections import Counter
from typing import Any, Dict, List


def search_transactions(transactions_1: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Функция проверяющая наличие строки поиска в описании"""
    return [
        transaction
        for transaction in transactions_1
        if "description" in transaction and re.search(search_string, transaction["description"])
    ]


def categorize_transactions(transactions_2: List[Dict[str, Any]], categories_2: Dict[str, List[str]]) -> Dict[str, int]:
    """Подсчет операций в каждой категории"""
    category_counts_2: Dict[str, int] = Counter()

    for transaction in transactions_2:
        if "description" in transaction:
            for category, keywords in categories_2.items():
                if any(keyword.lower() in transaction["description"].lower() for keyword in keywords):
                    category_counts_2[category] += 1
                    break

    return dict(category_counts_2)


def read_transactions_from_json(filename: str) -> Any:
    """Чтение транзакций из json файла"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


transactions = read_transactions_from_json("data/operatione.json")

categories = {"Перевод": ["Перевод организации", "Перевод частному лицу"]}

category_counts = categorize_transactions(transactions, categories)

transactions_ = [
    {"description": "Оплата за интернет"},
    {"description": "Покупка продуктов в магазине"},
    {"description": "Перевод денег другу"},
    {"description": "Оплата за мобильную связь"},
    {"description": "Покупка билетов на концерт"},
]

categories_ = {
    "Интернет": ["интернет", "онлайн"],
    "Продукты": ["продукты", "магазин"],
    "Другое": ["перевод", "концерт", "билеты"],
}

result = categorize_transactions(transactions_, categories_)
# print(result)
