import pytest
from src.sorting import sort_by

jobs_mock = [
    {
        "max_salary": 4100,
        "min_salary": 2100,
        "date_posted": "2021-10-23",
    },
    {
        "max_salary": 8100,
        "min_salary": 4100,
        "date_posted": "2021-09-18",
    },
    {
        "max_salary": 5100,
        "min_salary": 2600,
        "date_posted": "2021-09-22",
    },
    {
        "max_salary": 2100,
        "min_salary": 1100,
        "date_posted": "2021-06-19",
    },
]
# mock de max_salary como critário
jobs_mock_sort_by_max_salary = [
    {
        "max_salary": 8100,
        "min_salary": 4100,
        "date_posted": "2021-09-18",
    },
    {
        "max_salary": 5100,
        "min_salary": 2600,
        "date_posted": "2021-09-22",
    },
    {
        "max_salary": 4100,
        "min_salary": 2100,
        "date_posted": "2021-10-23",
    },
    {
        "max_salary": 2100,
        "min_salary": 1100,
        "date_posted": "2021-06-19",
    },
]
# mock de min_salary como critário

jobs_mock_sort_by_min_salary = [
    {
        "max_salary": 2100,
        "min_salary": 1100,
        "date_posted": "2021-06-19",
    },
    {
        "max_salary": 4100,
        "min_salary": 2100,
        "date_posted": "2021-10-23",
    },
    {
        "max_salary": 5100,
        "min_salary": 2600,
        "date_posted": "2021-09-22",
    },
    {
        "max_salary": 8100,
        "min_salary": 4100,
        "date_posted": "2021-09-18",
    },
]
# mock de date_posted como critário

jobs_mock_sort_by_date_posted = [
    {
        "max_salary": 4100,
        "min_salary": 2100,
        "date_posted": "2021-10-23",
    },
    {
        "max_salary": 5100,
        "min_salary": 2600,
        "date_posted": "2021-09-22",
    },
    {
        "max_salary": 8100,
        "min_salary": 4100,
        "date_posted": "2021-09-18",
    },
    {
        "max_salary": 2100,
        "min_salary": 1100,
        "date_posted": "2021-06-19",
    },
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == jobs_mock_sort_by_max_salary

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == jobs_mock_sort_by_min_salary

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == jobs_mock_sort_by_date_posted

    criteria = "some_invalid_criteria"
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {criteria}"
    ):
        sort_by(jobs_mock, criteria)
