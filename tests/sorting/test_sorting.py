import pytest
from src.sorting import sort_by

jobs = [
    {
        "min_salary": "1500",
        "max_salary": "3500",
        "date_posted": "2021-12-03"
    },
    {
        "min_salary": "1000",
        "max_salary": "3000",
        "date_posted": "2021-12-02"
    },
    {
        "min_salary": "500",
        "max_salary": "1500",
        "date_posted": "2021-12-01"
    },
]

expected = [
    {
        "min_salary": "500",
        "max_salary": "1500",
        "date_posted": "2021-12-01"
    },
    {
        "min_salary": "1000",
        "max_salary": "3000",
        "date_posted": "2021-12-02"
    },
    {
        "min_salary": "1500",
        "max_salary": "3500",
        "date_posted": "2021-12-03"
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == expected


with pytest.raises(ValueError, match="invalid sorting criteria: """):
    sort_by(jobs, "")

with pytest.raises(ValueError, match="invalid sorting criteria: None"):
    sort_by(jobs, None)
