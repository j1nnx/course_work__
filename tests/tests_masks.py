import pytest

from src.masks import mask_account_number, mask_credit_card_number


@pytest.fixture
def card_numbers() -> list:
    return [("7000792289606361", "7000 79** **** 6361"), ("1234567890123456", "1234 56** **** 3456")]


@pytest.fixture
def account_numbers() -> list:
    return [("73654108430135874305", "**4305"), ("1234567890123456", "**3456")]


@pytest.mark.parametrize(
    "original_number, masked_number",
    [("7000792289606361", "7000 79** **** 6361"), ("1234567890123456", "1234 56** **** 3456")],
)
def test_mask_card_or_account(original_number: str, masked_number: str) -> None:
    assert mask_credit_card_number(original_number) == masked_number


@pytest.mark.parametrize(
    "original_number, masked_number", [("73654108430135874305", "**4305"), ("1234567890123456", "**3456")]
)
def test_form_mask_credit_card_number(original_number: str, masked_number: str) -> None:
    assert mask_account_number(original_number) == masked_number


if __name__ == "__main__":
    pytest.main()
    test_mask_card_or_account("7000792289606361", "7000 79** **** 6361")
    test_form_mask_credit_card_number("73654108430135874305", "**4305")

print("Всё выводит ты красавчик")
