from src.sorting import sort_by

jobs_list = [
    {"min_salary": 0, "max_salary": 10, "date_posted": "01/12/2021"},
    {"min_salary": 10, "max_salary": 30, "date_posted": "02/12/2021"},
    {"min_salary": 20, "max_salary": 50, "date_posted": "03/12/2021"},
]

sort_by_min_salary = [
    {"min_salary": 0, "max_salary": 10, "date_posted": "03/12/2021"},
    {"min_salary": 10, "max_salary": 30, "date_posted": "03/12/2021"},
    {"min_salary": 20, "max_salary": 50, "date_posted": "03/12/2021"},
]

sort_by_max_salary = [
    {"min_salary": 20, "max_salary": 50, "date_posted": "03/12/2021"},
    {"min_salary": 10, "max_salary": 30, "date_posted": "02/12/2021"},
    {"min_salary": 0, "max_salary": 10, "date_posted": "01/12/2021"},
]

sort_by_date_posted = [
    {"min_salary": 0, "max_salary": 10, "date_posted": "01/12/2021"},
    {"min_salary": 10, "max_salary": 30, "date_posted": "02/12/2021"},
    {"min_salary": 20, "max_salary": 50, "date_posted": "03/12/2021"},
]


def test_sort_by_criteria():
    sort_by(jobs_list, "min_salary")
    assert sort_by_min_salary

    sort_by(jobs_list, "max_salary")
    assert sort_by_max_salary

    sort_by(jobs_list, "date_posted")
    assert sort_by_date_posted
