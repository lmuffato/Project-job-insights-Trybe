# import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    criteria = ["min_salary", "max_salary", "date_posted"]
    job_mock_one = {
        "min_salary": "800",
        "max_salary": "3000",
        "date_posted": "2021-02-13"
    }
    job_mock_two = {
        "min_salary": "1000",
        "max_salary": "5000",
        "date_posted": "2020-12-03"
    }
    job_mock_three = {
        "min_salary": "2000",
        "max_salary": "7000",
        "date_posted": "2021-06-21"
    }
    job_mock_four = {
        "min_salary": "10000",
        "max_salary": "30000",
        "date_posted": "2021-10-08"
    }

    job_list = [job_mock_one, job_mock_two, job_mock_three, job_mock_four]
    sort_by(job_list, criteria[0])
    assert job_list == [
        job_mock_one,
        job_mock_two,
        job_mock_three,
        job_mock_four
    ]
    sort_by(job_list, criteria[1])
    assert job_list == [
        job_mock_four,
        job_mock_three,
        job_mock_two,
        job_mock_one
    ]
    sort_by(job_list, criteria[2])
    assert job_list == [
        job_mock_four,
        job_mock_three,
        job_mock_one,
        job_mock_two
    ]
    pass
