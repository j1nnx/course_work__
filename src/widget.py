from src.masks import mask_account_number, mask_credit_card_number


def masks_of_cards(data: str) -> str:
    """
    Функция переиспользует ранее написанные функции
    и возвращает исходную строку с замаскированным номером карты/счета.fla
    """
    right_data = data.split(" ")
    if right_data[0] == "Счет":
        return f"Счет {mask_account_number(right_data[-1])}"
    else:
        return f'{" ".join(right_data[:-1])} {mask_credit_card_number(right_data[-1])}'


def convert_datetime_to_date(datetime_string: str) -> str:
    """Функция, которая принимает строку и возвращает строку с датой"""
    date_parts = datetime_string.split("T")[0].split("-")
    return f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
