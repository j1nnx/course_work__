import json
import os
from datetime import datetime
from typing import Any, List, Dict

import requests
import yfinance as yf
from dotenv import load_dotenv

from src.utils import read_file_xls, setup_logger

load_dotenv()
api_key = os.getenv("api_keys")
logger = setup_logger()


def get_greeting(hour: Any) -> str:
    """Возвращает приветствие в зависимости от времени"""
    if hour is None:
        hour = datetime.now()
    else:
        hour = datetime.strptime(hour, "%d.%m.%Y %H:%M")
    hour = hour.hour
    if 5 < hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 24:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def card_number(read: Any) -> Any:
    """Возвращает номер карты пользователя"""
    if read is not None:
        for transaction in read:
            return transaction["Номер карты"]
        logger.info("Функция card_number работает успешно")
    else:
        logger.error("С функцией card_number что-то не так")
        return None


def total_sum_amount(reader: Any, card_number_: Any) -> Any:
    """Возвращает общую сумму всех транзакций пользователя"""
    total = 0
    if card_number_:
        for transaction in reader:
            total += transaction["Сумма операции"]
    logger.info("Successfully! Result - %s" % total)
    return round(total)


def cashback(total_sum: int) -> Any:
    """Возвращает кешбек"""
    cash = total_sum // 100
    logger.info("Successfully! Result - %s" % cash)
    return cash


def top_transaction(data: Any) -> Any:
    """Возвращает топ 5 транзакций пользователя"""
    if data is not None:

        def sort_sum(item: Any) -> Any:
            return item["Сумма операции"]

        data.sort(key=sort_sum, reverse=True)

        result = []
        count = 0
        for transaction in data:
            if count < 5:
                result.append(
                    {
                        "date": transaction["Дата операции"],
                        "amount": round(transaction["Сумма операции"]),
                        "category": transaction["Категория"],
                        "description": transaction["Описание"],
                    }
                )
                count += 1
            else:
                break
        logger.info("Successfully! Result - %s" % result)
        return result
    else:
        logger.error("Something went wrong in 'top_transactions' function...")
        return None


def get_currency(currency: Any) -> Any:
    """Возвращает курс валют"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"api_key": api_key}, timeout=15)
    response_data = json.loads(response.text)

    if "rates" in response_data and "RUB" in response_data["rates"]:
        rate = response_data["rates"]["RUB"]
        logger.info("Функция get_currency работает успешно!")
        return rate
    else:
        logger.error(f"Ошибка в ответе API: {response_data}")
        return None


def get_stock_currency(stock: str) -> Any:
    """Возвращает курс акций"""
    ticker = yf.Ticker(stock)
    data_todays = ticker.history(period="1d")
    if not data_todays.empty:
        high_price = data_todays["High"].iloc[0]
        logger.info("Функция get_stock_currency работает успешно!")
        return high_price
    else:
        return 0.0


def create_operations(greeting: Any, card_numbers: Any, total_sum: Any, cash: Any, top: Any) -> Any:
    """Возвращает словарь с данными пользователя"""
    data = {"greeting": greeting, "cards": [], "top_transactions": [], "currency_rates": [], "stock_prices": []}
    if read_file_xls("../data/operation.xls"):
        for _ in read_file_xls("../data/operation.xls"):
            if card_numbers not in [card["last_digits"] for card in data["cards"]] and card_numbers is not None:
                data["cards"].append(
                    {"last_digits": card_numbers, "total_spent": round (total_sum, 2), "cashback": cash}
                )
        data["top_transactions"] = top

        usd_rate = get_currency("USD")
        eur_rate = get_currency("EUR")

        if usd_rate is not None and eur_rate is not None:
            data["currency_rates"].append(
                (
                    {"currency": "USD", "rate": round(usd_rate, 2)},
                    {"currency": "EUR", "rate": round(eur_rate, 2)},
                )
            )
        else:
            logger.error("Failed to retrieve currency rates")

        data["stock_prices"].append(
            [
                {"stock": "AAPL", "price": round(get_stock_currency ("AAPL"), 2)},
                {"stock": "AMZN", "price": round(get_stock_currency ("AMZN"), 2)},
                {"stock": "GOOGL", "price": round(get_stock_currency ("GOOGL"), 2)},
                {"stock": "MSFT", "price": round(get_stock_currency ("MSFT"), 2)},
                {"stock": "TSLA", "price": round(get_stock_currency ("TSLA"), 2)},
            ]
        )
        logger.info("Функция create_operations работает успешно!")
    return data
