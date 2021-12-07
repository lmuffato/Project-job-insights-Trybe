import pytest
from src.sorting import sort_by

mock = [
    {"min_salary": "1", "max_salary": "1", "date_posted": "2020-08-08"},
    {"min_salary": "2", "max_salary": "2", "date_posted": "2020-08-06"},
    {"min_salary": "3", "max_salary": "3", "date_posted": "2020-08-07"},
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")

    assert mock == [
        {"min_salary": "1", "max_salary": "1", "date_posted": "2020-08-08"},
        {"min_salary": "2", "max_salary": "2", "date_posted": "2020-08-06"},
        {"min_salary": "3", "max_salary": "3", "date_posted": "2020-08-07"},
    ]

    sort_by(mock, "max_salary")
    assert mock == [
        {"min_salary": "3", "max_salary": "3", "date_posted": "2020-08-07"},
        {"min_salary": "2", "max_salary": "2", "date_posted": "2020-08-06"},
        {"min_salary": "1", "max_salary": "1", "date_posted": "2020-08-08"},
    ]

    sort_by(mock, "date_posted")
    assert mock == [
        {"min_salary": "1", "max_salary": "1", "date_posted": "2020-08-08"},
        {"min_salary": "3", "max_salary": "3", "date_posted": "2020-08-07"},
        {"min_salary": "2", "max_salary": "2", "date_posted": "2020-08-06"},
    ]

    with pytest.raises(ValueError):
        sort_by([], "asd")
