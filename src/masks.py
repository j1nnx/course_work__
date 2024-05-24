from src.logger import setup_logger

logger = setup_logger()


def mask_credit_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if len(card_number) == 16:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info("Function mask_credit_card_number completed successfully")
        return masked_number
    else:
        logger.error("With the function mask_credit_card_number something is wrong")
    return card_number


def mask_account_number(account_number: str) -> str:
    """Функция принимает на вход номер счёта и возвращает ее маску"""
    if len(account_number) == 21:
        masked_number = f"**{account_number[-4:]}"
        logger.info("Function mask_account_number completed successfully")
        return masked_number
    else:
        logger.error("With the function mask_account_number something is wrong")
    return account_number


mask_credit_card_number("1234567890123456")
mask_account_number("12345678901234567890123456789012")
