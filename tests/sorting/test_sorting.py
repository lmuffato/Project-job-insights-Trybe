import pytest
from src.sorting import sort_by

jobs = [
        {
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2021-12-04"
        },
        {
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2022-01-25"
        },
        {
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-11-20"
        },
    ]


def test_sort_by_criteria():
    # O teste rejeita implementações que não ordenam corretamente.
    sort_by(jobs=jobs, criteria="max_salary")
    assert jobs == [
        {
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-11-20"
        },
        {
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2022-01-25"
        },
        {
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2021-12-04"
        },
    ]
    sort_by(jobs=jobs, criteria="min_salary")
    assert jobs == [
        {
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2021-12-04"
        },
        {
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2022-01-25"
        },
        {
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-11-20"
        },
    ]
    sort_by(jobs=jobs, criteria="date_posted")
    assert jobs == [
        {
            "min_salary": "3000",
            "max_salary": "7000",
            "date_posted": "2022-01-25"
        },
        {
            "min_salary": "2000",
            "max_salary": "6000",
            "date_posted": "2021-12-04"
        },
        {
            "min_salary": "4000",
            "max_salary": "8000",
            "date_posted": "2021-11-20"
        },
    ]
    # O teste rejeita implementações que aceitam critérios não especificados.
    with pytest.raises(ValueError):
        sort_by(jobs=jobs, criteria="xablau")
