from src.sorting import sort_by

mock_jobs = [
    {
        "job_title": "Teste 1",
        "date_posted": "2021-10-14",
        "max_salary": 100000,
        "min_salary": 30000,
    },
    {
        "job_title": "Teste 2",
        "date_posted": "2018-12-11",
        "max_salary": 50000,
        "min_salary": 10000,
    },
    {
        "job_title": "Teste 3",
        "date_posted": "2020-10-14",
        "max_salary": 7000,
        "min_salary": 1000,
    },
]

sorted_by_min_salary = [mock_jobs[2], mock_jobs[1], mock_jobs[0]]
sorted_by_max_salary = [mock_jobs[0], mock_jobs[1], mock_jobs[2]]


def test_sort_by_criteria():
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == sorted_by_max_salary
