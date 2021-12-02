from src.sorting import sort_by
import pytest


jobs = [
    {
        "max_salary": "100",
        "min_salary": "10",
        "date_posted": "2020-05-10",
    },
    {
        "min_salary": "100",
        "max_salary": "500",
        "date_posted": "2021-10-05",
    },
    {
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2021-05-10",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "2000"

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "10"

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2021-10-05"

    invalid_key = "teste"

    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_key}"
    ):
        sort_by(jobs, invalid_key)
