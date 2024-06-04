import json
import re
from typing import Any


def search_transactions(transactions: Any, search_string: Any) -> Any:
    return [transaction for transaction in transactions if re.search(search_string, transaction["description"])]


def categorize_transactions(transactions: Any, categories: Any) -> Any:
    category_counts = {category: 0 for category in categories}
    for transaction in transactions:
        category = transaction.get("category")
        if category in category_counts:
            category_counts[category] += 1
    return category_counts


def read_file_json(filename: str) -> Any:
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
