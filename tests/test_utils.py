import os
import unittest
from typing import Any, Dict
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.utils import sum_amount

load_dotenv()
API_KEY = os.getenv("api_keys")


class TestTransactionSum(unittest.TestCase):
    def test_sum_amount_with_mocked_rate(self) -> None:
        # Создаем фиктивный ответ API
        mock_rate: float = 75.0
        transaction: Dict[str, Any] = {
            "operationAmount": {"amount": "500", "currency": {"code": "USD"}}
        }
        expected_total: float = 500 * mock_rate

        with patch("src.utils.get_transactions_rub_to_usd", return_value=mock_rate) as mock_method:
            total: float = sum_amount(transaction)
            mock_method.assert_called_once_with("USD")
            self.assertEqual(total, expected_total)

    def test_sum_amount_with_real_data(self) -> None:
        # Используем реальные данные для тестирования
        transaction: Dict[str, Any] = {
            "operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}
        }
        amount_in_rub: float = float(transaction["operationAmount"]["amount"])
        total: float = sum_amount(transaction)
        self.assertEqual(total, amount_in_rub)

    @patch("src.utils.requests.get")
    def test_get_transactions_rub_to_usd_with_mock(self, mock_get: MagicMock) -> None:
        """Фиктивный ответ API"""
        mock_response: MagicMock = MagicMock()
        mock_response.json.return_value = {"rates": {"RUB": 75.0}}
        mock_get.return_value = mock_response


if __name__ == "__main__":
    unittest.main()
