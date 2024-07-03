import pytest
import pandas as pd
from src.reports import filter_transactions_by_category_and_date
from typing import Any


def test_filter_transactions_empty_result():
    transactions = pd.DataFrame({
        'category': ['Food', 'Clothes', 'Entertainment'],
        'data_payment': [
            '01.01.2023', '15.01.2023', '10.03.2023'
        ]
    })
    category = 'Electronics'
    start_date = '01.01.2023'

    filtered_transactions = filter_transactions_by_category_and_date(transactions, category, start_date)

    assert len(filtered_transactions) == 0
