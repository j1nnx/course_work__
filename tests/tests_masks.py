import pytest
from src.masks import mask_account_number, mask_credit_card_number


def test_mask_card_or_account():
    assert mask_credit_card_number('7000792289606361') == '7000 79** **** 6361'
    assert mask_credit_card_number('1234567890123456') == '1234 56** **** 3456'


def test_form_mask_credit_card_number():
    assert mask_account_number('73654108430135874305') == '**4305'
    assert mask_account_number('1234567890123456') == '**3456'


if __name__ == "__main__":
    pytest.main()

print('Всё выводит ты красавчик')
