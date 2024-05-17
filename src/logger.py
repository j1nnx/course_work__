import os
import logging
from logging import Logger

if os.path.isfile(os.path.join("src/src.logger.log")):
    os.remove(os.path.join("src/src.logger.log"))


def setup_logger() -> Logger:
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(f"logger.log", mode="w")
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(module)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    return logger
