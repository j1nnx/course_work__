import json
import logging
from logging import Logger
from pathlib import Path
from typing import Any

import pandas as pd


def setup_logger() -> Logger:
    """Function to set up the logger."""
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
    """Function to read a .xls or .json file."""
    if Path(filename).suffix.lower() == ".xls":
        df = pd.read_excel(filename)
        logger.info("Successfully read .xls file")
        return df.to_dict(orient="records")
    elif Path(filename).suffix.lower() == ".json":
        with open(filename, "r", encoding="utf-8") as file:
            logger.info("Successfully read .json file")
            return json.load(file)
    else:
        logger.error("Unsupported file format")
        print("Unsupported file format")


def write_data(file: str, result: Any) -> None:
    """Function to write results to the specified file."""
    try:
        if file.endswith(".txt"):
            with open(file, "a", encoding="utf-8") as f:
                f.write(result)
        else:
            with open(file, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4, ensure_ascii=False)
        logger.info(f"Successfully wrote to file {file}")
    except Exception as e:
        logger.error(f"Error writing to file {file}: {e}")
