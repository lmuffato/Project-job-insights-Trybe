from src.sorting import sort_by
import pytest

list_jobs = [
    {
        "min_salary": 3000,
        "max_salary": 5500,
        "date_posted": "02/11/2021",
    },
    {
        "min_salary": 1500,
        "max_salary": 3500,
        "date_posted": "01/11/2021",
    },
    {
        "min_salary": 4000,
        "max_salary": 9000,
        "date_posted": "03/11/2021",
    },
]


def test_sort_by_criteria():
    sort_by(list_jobs, "min_salary")
    assert list_jobs == [
        {
            "min_salary": 1500,
            "max_salary": 3500,
            "date_posted": "01/11/2021",
        },
        {
            "min_salary": 3000,
            "max_salary": 5500,
            "date_posted": "02/11/2021",
        },
        {
            "min_salary": 4000,
            "max_salary": 9000,
            "date_posted": "03/11/2021",
        },
    ]

    sort_by(list_jobs, "max_salary")
    assert list_jobs == [
        {
            "min_salary": 4000,
            "max_salary": 9000,
            "date_posted": "03/11/2021",
        },
        {
            "min_salary": 3000,
            "max_salary": 5500,
            "date_posted": "02/11/2021",
        },
        {
            "min_salary": 1500,
            "max_salary": 3500,
            "date_posted": "01/11/2021",
        },
    ]

    sort_by(list_jobs, "date_posted")
    assert list_jobs == [
        {
            "min_salary": 4000,
            "max_salary": 9000,
            "date_posted": "03/11/2021",
        },
        {
            "min_salary": 3000,
            "max_salary": 5500,
            "date_posted": "02/11/2021",
        },
        {
            "min_salary": 1500,
            "max_salary": 3500,
            "date_posted": "01/11/2021",
        },
    ]

    with pytest.raises(
        ValueError, match="invalid sorting criteria: invalid_criteria"
    ):
        sort_by(list_jobs, "invalid_criteria")
