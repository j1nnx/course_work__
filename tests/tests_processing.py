import pytest
from src.processing import filter_dicts_by_state, sort_dicts_by_date

dict_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filters_dicts_by_state():
    filtered_list = filter_dicts_by_state(dict_list, state="CANCELED")
    assert all(dict_["state"] == "CANCELED" for dict_ in filtered_list)


def test_sort_dicts_by_date():
    sorted_ = sort_dicts_by_date(dict_list)
    dates = [dicts["date"] for dicts in sorted_]
    assert dates == ['2019-07-03T18:35:29.512364',
                     '2018-10-14T08:21:33.419441',
                     '2018-09-12T21:27:25.241689',
                     '2018-06-30T02:08:58.425572']


if __name__ == "__main__":
    pytest.main()
    test_filters_dicts_by_state()
    test_sort_dicts_by_date()
    print('Всё выводит ты красавчик')

