import pytest
from src.sorting import sort_by

jobs_mock = [
    {
        "job_title": "job 1",
        "min_salary": 1000,
        "max_salary": 7000,
        "date_posted": "2021-10-04",
    },
    {
        "job_title": "job 2",
        "min_salary": 2000,
        "max_salary": 6000,
        "date_posted": "2021-10-03",
    },
    {
        "job_title": "job 3",
        "min_salary": 3000,
        "max_salary": 5000,
        "date_posted": "2021-10-02",
    },
    {
        "job_title": "job 4",
        "min_salary": 4000,
        "max_salary": 4500,
        "date_posted": "2021-10-01",
    },
]

sorted_by_min = [
    jobs_mock[0],
    jobs_mock[1],
    jobs_mock[2],
    jobs_mock[3],
]

sorted_by_max = [
    jobs_mock[3],
    jobs_mock[2],
    jobs_mock[1],
    jobs_mock[0],
]

sorted_by_date = [
    jobs_mock[3],
    jobs_mock[2],
    jobs_mock[1],
    jobs_mock[0],
]

sort_criteria = ["min_salary", "max_salary", "date_posted"]
wrong_criteria = "jobs"


def test_sort_by_criteria():
    sort_by(jobs_mock, sort_criteria[0])
    assert jobs_mock == sorted_by_min

    sort_by(jobs_mock, sort_criteria[1])
    assert jobs_mock == sorted_by_max

    sort_by(jobs_mock, sort_criteria[2])
    assert jobs_mock == sorted_by_date

    with pytest.raises(ValueError, match="invalid sorting criteria: jobs"):
        sort_by(jobs_mock, wrong_criteria)
