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
        "min_salary": 4000,
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
        "date_posted": "2020-10-10",
    },
]

ordered_by_date = [
    jobs_mock[1], jobs_mock[4], jobs_mock[0], jobs_mock[3], jobs_mock[2]
]

ordered_by_min_salary = [
    jobs_mock[0], jobs_mock[3], jobs_mock[1], jobs_mock[2], jobs_mock[4]
]

ordered_by_max_salary = [
    jobs_mock[4], jobs_mock[2], jobs_mock[1], jobs_mock[3], jobs_mock[0]
]

criteria = ["date_posted", "max_salary", "min_salary"]


def test_sort_by_criteria():
    sort_by(jobs_mock, criteria[0])
    assert jobs_mock == ordered_by_date

    sort_by(jobs_mock, criteria[1])
    assert jobs_mock == ordered_by_max_salary

    sort_by(jobs_mock, criteria[2])
    assert jobs_mock == ordered_by_min_salary
