import re
from typing import Any, Dict, List, Iterator

from src.csv_xlsx import read_file_from_file_csv, read_file_from_file_xlsx
from src.generators import filter_by_currency, transaction_descriptions
from src.handler import search_transactions
from src.processing import filter_dicts_by_state, sort_dicts_by_date
from src.utils import read_transaction_from_file_json, sum_amount
from src.widget import convert_datetime_to_date, masks_of_cards


def format_open_file() -> List[Dict[Any, Any]]:
    """Функция для открытия определённого файла"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    file_open = input("Выберите необходимый пункт меню: 1.JSON 2.CSV 3.Excel\n")
    if file_open == "1" or file_open.lower() == "json":
        print("Для обработки выбран json файл.")
        return read_transaction_from_file_json("../data/operatione.json")
    elif file_open == "2" or file_open.lower() == "csv":
        print("Для обработки выбран CSV файл.")
        return read_file_from_file_csv("data/transactions.csv")
    elif file_open == "3" or file_open.lower() == "excel":
        print("Для обработки выбран Excel файл.")
        return read_file_from_file_xlsx("data/transactions_excel.xlsx")
    else:
        print("Некорректный ввод, повторите ввод")
        return format_open_file()


def filter_status(data: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """Функция для выбора статуса EXECUTED, CANCELED, PENDING"""
    print("Введите статус по которому необходимо выполнить фильтрацию.")
    format_ = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    if format_.upper() not in ("EXECUTED", "CANCELED", "PENDING"):
        print("Статус не корректен, ввидите ещё раз")
        return filter_status(data)

    return filter_dicts_by_state(data, format_)


def sort_by_date(data: List[Dict[Any, Any]]) -> List[Dict[Any, Any]]:
    """Сортирует список транзакций"""
    sort = input("Отсортировать операции по дате? Да/Нет \n")
    if sort.lower() == "да":
        figure = input("по возрастанию/по убыванию \n")
        if figure.lower() == "по возрастанию":
            return sort_dicts_by_date(data)
        elif figure.lower() == "по убыванию":
            return sort_dicts_by_date(data, reverse=True)
        else:
            print("Не коректное значение, введите ещё раз")
            return sort_by_date(data)
    elif sort.lower() == "нет":
        return data  # Возвращаем исходный список, если сортировка не нужна
    else:
        print("Не корректный ответ, повторите ввод")
        return sort_by_date(data)

    # Фильтрация по валюте должна быть выполнена после сортировки
    sort_rub = input("Выводить только рублевые тразакции? Да/Нет\n")
    if sort_rub.lower() == "да":
        return filter_by_currency(data, "RUB")
    elif sort_rub.lower() == "нет":
        return data
    else:
        print("Некорректный ответ, повторите ввод")
        return sort_by_date(data)


def filter_user_keyword(data: List[Dict[Any, Any]]) -> Any:
    """Фильтрация по введённому слову"""
    keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")
    if keyword.lower() == "да":
        find_ = input("Что бы вы хотели найти?\n")
        return search_transactions(data, find_)
    elif keyword.lower() == "нет":
        return data
    else:
        print("Некоректный ввод, введите ещё раз")
        return filter_user_keyword(data)


def print_transaction(data: List[Dict[Any, Any]]) -> None:
    """Вывод отформатированного списка транзакций"""
    print("Распечатываю итоговый список транзакций")
    if data and len(data) != 0:
        descriptions_iterator = transaction_descriptions(data)
        for transaction in data:
            print(convert_datetime_to_date(transaction["date"]), next(descriptions_iterator))
            if re.search("Перевод", transaction["description"]):
                print(masks_of_cards(transaction["from"]), "->", masks_of_cards(transaction["to"]))
            else:
                print(masks_of_cards(transaction["to"]))
                print(f"Сумма: {sum_amount(transaction)} руб. \n")
    else:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")


def main() -> None:
    """Функция запускающая обработку транзакций"""
    data = format_open_file()
    data = filter_status(data)
    data = sort_by_date(data)
    data = filter_user_keyword(data)
    print_transaction(data)


if __name__ == "__main__":
    main()
