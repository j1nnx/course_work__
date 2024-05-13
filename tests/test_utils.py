import unittest
from unittest.mock import patch, MagicMock
from src.utils import sum_amount, get_transactions_rub_to_usd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("api_keys")


class TestTransactionSum(unittest.TestCase):
    def test_sum_amount_with_mocked_rate(self):
        # Создаем фиктивный ответ API
        mock_rate = 75.0
        transaction = {
            "operationAmount": {
                "amount": "500",
                "currency": {
                    "code": "USD"
                }
            }
        }
        expected_total = 500 * mock_rate

        with patch('src.utils.get_transactions_rub_to_usd', return_value=mock_rate) as mock_method:
            total = sum_amount(transaction)
            mock_method.assert_called_once_with("USD")
            self.assertEqual(total, expected_total)

    def test_sum_amount_with_real_data(self):
        # Используем реальные данные для тестирования
        transaction = {
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "code": "RUB"
                }
            }
        }
        expected_total = float(transaction["operationAmount"]["amount"])
        # Проверяем, что функция работает корректно без мокирования
        total = sum_amount(transaction)
        self.assertEqual(total, expected_total)

    @patch("src.utils.requests.get")
    def test_get_transactions_rub_to_usd_with_mock(self, mock_get):
        """Фиктивный ответ API"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response


if __name__ == '__main__':
    unittest.main()

