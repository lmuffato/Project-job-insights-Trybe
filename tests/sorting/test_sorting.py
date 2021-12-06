from src.sorting import sort_by

jobs = [
    {
        "max_salary": 100000,
        "min_salary": 200,
        "date_posted": "2020-05-20"
    },
    {
        "max_salary": 11500,
        "min_salary": 0,
        "date_posted": "2019-09-15"
    },
    {
        "max_salary": 20000,
        "min_salary": 8000,
        "date_posted": "2021-01-15"
    },
]

sorted_min_salary = [jobs[1], jobs[0], jobs[2]]
sorted_max_salary = [jobs[0], jobs[2], jobs[1]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == sorted_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sorted_max_salary
