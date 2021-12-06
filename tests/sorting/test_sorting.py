from src.sorting import sort_by

jobs_mock = [
    {
        "job_title": "test job 1",
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2010-02-02",
    },
    {
        "job_title": "test job 2",
        "min_salary": 0,
        "max_salary": 7000,
        "date_posted": "2021-07-01",
    },
    {
        "job_title": "test job 3",
        "min_salary": 5000,
        "max_salary": 7500,
        "date_posted": "2000-09-07",
    },
    {
        "job_title": "test job 4",
        "min_salary": 2000,
        "max_salary": 3500,
        "date_posted": "2001-01-10",
    },
    {
        "job_title": "test job 5",
        "min_salary": 8000,
        "max_salary": 9500,
        "date_posted": "1995-10-10",
    },
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock[0]["min_salary"] == 0

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock[0]["max_salary"] == 9500

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock[0]["date_posted"] == "2021-07-01"
