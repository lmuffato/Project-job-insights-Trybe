from src.sorting import sort_by

jobs = [
        {
            "id": 1,
            "max_salary": 10000,
            "min_salary": 4500,
            "date_posted": "2021-01-10"
        },
        {
            "id": 2,
            "max_salary": 5000,
            "min_salary": 3500,
            "date_posted": "2021-07-05"
        },
        {
            "id": 3,
            "max_salary": 15000,
            "min_salary": 1500,
            "date_posted": "2021-01-01"
        },
    ]

min_jobs_salary = [
        {
            "id": 3,
            "max_salary": 15000,
            "min_salary": 1500,
            "date_posted": "2021-01-01"
        },
        {
            "id": 2,
            "max_salary": 5000,
            "min_salary": 3500,
            "date_posted": "2021-07-05"
        },
        {
            "id": 1,
            "max_salary": 10000,
            "min_salary": 4500,
            "date_posted": "2021-01-10"
        },
    ]

max_jobs_salary = [
        {
            "id": 3,
            "max_salary": 15000,
            "min_salary": 1500,
            "date_posted": "2021-01-01"
        },
        {
            "id": 1,
            "max_salary": 10000,
            "min_salary": 4500,
            "date_posted": "2021-01-10"
        },
        {
            "id": 2,
            "max_salary": 5000,
            "min_salary": 3500,
            "date_posted": "2021-07-05"
        },
    ]

date_jobs_salary = [
        {
            "id": 2,
            "max_salary": 5000,
            "min_salary": 3500,
            "date_posted": "2021-07-05"
        },
        {
            "id": 1,
            "max_salary": 10000,
            "min_salary": 4500,
            "date_posted": "2021-01-10"
        },
        {
            "id": 3,
            "max_salary": 15000,
            "min_salary": 1500,
            "date_posted": "2021-01-01"
        },
    ]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == min_jobs_salary

    sort_by(jobs, 'max_salary')
    assert jobs == max_jobs_salary

    sort_by(jobs, 'date_posted')
    assert jobs == date_jobs_salary
