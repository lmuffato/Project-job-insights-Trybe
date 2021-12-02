import pytest
from src.sorting import sort_by

valid_criterias = ["min_salary", "max_salary", "date_posted"]

job_1 = {
    "job_name": "junior developer", "max_salary": 3500,
    "min_salary": 2000, "date_posted": "2021-08-01",
    }

job_2 = {
    "job_name": "pleno developer", "max_salary": 5000,
    "min_salary": 3000, "date_posted": "2021-08-10",
    }

job_3 = {
    "job_name": "senior developer", "max_salary": 8000,
    "min_salary": 5000, "date_posted": "2021-08-04",
    }

jobs = [job_1, job_2, job_3]

sorted_max_salary = [job_3, job_2, job_1]
sorted_min_salary = [job_1, job_2, job_3]
sorted_date_posted = [job_2, job_3, job_1]

# Inception
sort_result = [
    sorted_min_salary,
    sorted_max_salary,
    sorted_date_posted,
]

invalid_criterias = [
    criteria
    for criteria in jobs[0].keys()
    if criteria not in valid_criterias
]


def test_sort_by_criteria():
    print('Ok!')
    # none = None
    for index_criteria in range(len(valid_criterias)):
        sort_by(jobs, valid_criterias[index_criteria])
        sort = sort_result[index_criteria]
        assert jobs == sort
    for invalid_criteria in invalid_criterias:
        with pytest.raises(ValueError):
            sort_by(jobs, invalid_criteria)
