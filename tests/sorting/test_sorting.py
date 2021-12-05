from src.sorting import sort_by
import pytest

list_jobs = [
    {
        "min_salary": 3500.00,
        "max_salary": 5500.00,
        "date_posted": "02/11/2019",
    },
    {
        "min_salary": 1500.00,
        "max_salary": 3500.00,
        "date_posted": "02/11/2020",
    },
    {
        "min_salary": 4000.00,
        "max_salary": 9000.00,
        "date_posted": "02/11/2021",
    },
]


def test_sort_by_criteria():
    sort_by(list_jobs, "min_salary")
    assert list_jobs == [
        {
            "min_salary": 3500.00,
            "max_salary": 5500.00,
            "date_posted": "02/11/2019",
        },
        {
            "min_salary": 1500.00,
            "max_salary": 3500.00,
            "date_posted": "02/11/2020",
        },
        {
            "min_salary": 4000.00,
            "max_salary": 9000.00,
            "date_posted": "02/11/2021",
        },
    ]

    sort_by(list_jobs, "max_salary")
    assert list_jobs == [
        {
            "min_salary": 4000.00,
            "max_salary": 9000.00,
            "date_posted": "02/11/2021",
        },
        {
            "min_salary": 3500.00,
            "max_salary": 5500.00,
            "date_posted": "02/11/2019",
        },
        {
            "min_salary": 1500.00,
            "max_salary": 3500.00,
            "date_posted": "02/11/2020",
        },
    ]

    sort_by(list_jobs, "date_posted")
    assert list_jobs == [
        {
            "min_salary": 1500.00,
            "max_salary": 3500.00,
            "date_posted": "02/11/2020",
        },
        {
            "min_salary": 4000.00,
            "max_salary": 9000.00,
            "date_posted": "02/11/2021",
        },
        {
            "min_salary": 3500.00,
            "max_salary": 5500.00,
            "date_posted": "02/11/2019",
        },
    ]

    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        sort_by(list_jobs, "invalid")
