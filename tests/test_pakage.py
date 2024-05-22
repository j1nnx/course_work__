import unittest
import csv
import pandas as pd


class TestDataProcessing (unittest.TestCase):

    # Тест для проверки чтения данных из CSV файла
    def test_csv_data_reading(self) -> None:
        """Test file csv"""
        with open('../data/transactions.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                self.assertIsInstance(row, list)

    # Тест для проверки чтения данных из Excel файла
    def test_excel_data_reading(self) -> None:
        """Test file excel"""
        data = pd.read_excel("..\\data\\transactions_excel.xlsx")
        self.assertIsInstance(data, pd.DataFrame)
        self.assertFalse(data.empty, "Excel data should not be empty")


if __name__ == '__main__':
    unittest.main()
