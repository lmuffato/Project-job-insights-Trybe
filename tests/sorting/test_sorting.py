from src.sorting import sort_by


mock_jobs = [
    {
        "min_salary": 30000,
        "max_salary": 100000,
        "date_posted": "2021-10-14",
    },
    {
        "min_salary": 10000,
        "max_salary": 50000,
        "date_posted": "2018-12-11",
    },
    {
        "min_salary": 1000,
        "max_salary": 7000,
        "date_posted": "2020-10-14",
    },
]


sorted_by_min_salary = [mock_jobs[2], mock_jobs[1], mock_jobs[0]]
sorted_by_max_salary = [mock_jobs[0], mock_jobs[1], mock_jobs[2]]


def test_sort_by_criteria():
    pass
    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == sorted_by_max_salary
