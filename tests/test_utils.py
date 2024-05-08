import unittest
from src.utils import read_transaction_from_file_json, get_transactions_rub_to_usd, sum_amount_from_transactions


def test_read_transaction_from_file_json():
    transactions = read_transaction_from_file_json('path_to_your_test_file.json')
    assert isinstance(transactions, list), "Должен вернуть список"


def test_get_transactions_rub_to_usd():
    rate = get_transactions_rub_to_usd('USD')
    assert isinstance(rate, float), "Должен вернуть число с плавающей точкой"
    assert rate > 0, "Курс должен быть больше нуля"


def test_sum_amount_from_transactions():
    transactions = [
        {'operationAmount': {'amount': '100', 'currency': {'code': 'USD'}}},
        {'operationAmount': {'amount': '200', 'currency': {'code': 'EUR'}}},
        {'operationAmount': {'amount': '300', 'currency': {'code': 'RUB'}}}
    ]
    total = sum_amount_from_transactions(transactions)
    assert isinstance(total, float), "Должен вернуть число с плавающей точкой"
    assert total == 600.0, "Сумма должна быть равна 600.0"  # Предполагая, что курс 1:1 для упрощения


test_read_transaction_from_file_json()
test_get_transactions_rub_to_usd()
test_sum_amount_from_transactions()


if __name__ == '__main__':
    unittest.main()
