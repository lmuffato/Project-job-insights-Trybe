# Feito em pair programming com Lucas Lara
# e ajuda do Felipe Flores que apareceu na sala
from src.sorting import sort_by

mock_jobs = [
    {
        "min_salary": 45000,
        "max_salary": 115000,
        "date_posted": "2021-02-26",
    },
    {
        "min_salary": 25000,
        "max_salary": 65000,
        "date_posted": "2018-04-06",
    },
    {
        "min_salary": 2500,
        "max_salary": 8500,
        "date_posted": "2020-08-05",
    },
]

sorted_by_min_salary = [mock_jobs[2], mock_jobs[1], mock_jobs[0]]
sorted_by_max_salary = [mock_jobs[0], mock_jobs[1], mock_jobs[2]]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == sorted_by_max_salary
    