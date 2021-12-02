from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2003-03-27"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2002-02-26"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2001-01-25"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-12-02"},
    ]


def test_sort_by_criteria(jobs):
    mock_min_salary = [
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2001-01-25"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2002-02-26"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2003-03-27"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-12-02"},
    ]
    mock_max_salary = [
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-12-02"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2003-03-27"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2002-02-26"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2001-01-25"},
    ]
    mock_date_posted = [
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-12-02"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2003-03-27"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2002-02-26"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2001-01-25"},
    ]
    sort_by(jobs, "min_salary")
    assert jobs == mock_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == mock_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == mock_date_posted
