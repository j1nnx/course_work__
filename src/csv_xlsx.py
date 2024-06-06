import csv
from typing import Any, Dict, List

import pandas as pd


def read_csv(file_path: str) -> Any:
    poos = []
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            poos.append(row)
    return poos


def read_file_from_file_xlsx(filename: str) -> List[Dict]:
    """Читает file xlsx и возвращает список"""
    data = pd.read_excel(filename)
    return data.to_dict("records")
