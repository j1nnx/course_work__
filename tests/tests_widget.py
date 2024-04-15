import pytest
from src.widget import masks_of_cards, convert_datetime_to_date


def test_masks_of_cards():
    assert masks_of_cards('Visa Platinum 7000 7922 8960 6361') == 'Visa Platinum 7000 7922 8960 6361 ** **** 6361'
    assert masks_of_cards('Maestro 7000 7922 8960 6361') == 'Maestro 7000 7922 8960 6361 ** **** 6361'
    assert masks_of_cards('Счет 73654108430135874305') == 'Счет **4305'


def test_convert_datetime_to_date():
    assert convert_datetime_to_date('2018-07-11T02:26:18.671407') == '11.07.2018'
    assert convert_datetime_to_date('2019-07-11T02:26:18.671407') == '11.07.2019'
    assert convert_datetime_to_date('2019-10-11T02:26:18.671407') == "11.10.2019"


if __name__ == '__main__':
    pytest.main()
    test_masks_of_cards()
    test_convert_datetime_to_date()



