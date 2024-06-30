import json
import logging
from logging import Logger
from pathlib import Path
from typing import Any

import pandas as pd


def setup_logger() -> Logger:
    """Функция настройки логгера"""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("logger.log", mode="w")
    file_handler.setLevel(logging.DEBUG)

    formatter_ = logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter_)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()


def read_file_xls(filename: Any) -> Any:
    """Функция чтения файла .xls"""
    if Path(filename).suffix.lower() == ".xls":
        df = pd.read_excel(filename)
        logger.info("Successfully read file")
        return df.to_dict(orient="records")
    elif Path(filename).suffix.lower() == ".json":
        with open(filename, "r", encoding="utf-8") as file:
            logger.info("Successfully read file")
            return json.load(file)
    else:
        logger.error(f"С функцией read_file_xls что-то не так")
        print("Неверный формат файла")


def write_data(file: str, result: Any) -> None:
    """Функция которая записывает резуьтаты в указанный файл."""
    try:
        if file.endswith(".txt"):
            with open(file, "a") as file:
                file.write(result)
        else:
            with open(file, "w") as file:
                json.dump(result, file, indent=4, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Ошибка при записи файла {file}: {e}")
