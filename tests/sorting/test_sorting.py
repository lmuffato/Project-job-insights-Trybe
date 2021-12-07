from src.sorting import sort_by
import pytest

jobs = [
    {"min_salary": 0, "max_salary": 10, "date_posted": "01/01/2021"},
    {"min_salary": 5, "max_salary": 15, "date_posted": "01/03/2021"},
]

sort_by_max_salary_mock = [
    {"min_salary": 5, "max_salary": 15, "date_posted": "01/03/2021"},
    {"min_salary": 0, "max_salary": 10, "date_posted": "01/01/2021"},
]


def test_sort_by_criteria():
    with pytest.raises(ValueError, match="invalid sorting criteria: nohing"):
        sort_by(jobs, "nohing")

    sort_by(jobs, "max_salary")
    assert jobs == sort_by_max_salary_mock
