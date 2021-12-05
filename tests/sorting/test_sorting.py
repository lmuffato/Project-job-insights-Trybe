from src.sorting import sort_by


mock_of_jobs = [
    {
        "min_salary": 50000,
        "max_salary": 120000,
        "date_posted": "2021-02-18",
    },
    {
        "min_salary": 30000,
        "max_salary": 70000,
        "date_posted": "2011-11-15",
    },
    {
        "min_salary": 3000,
        "max_salary": 9000,
        "date_posted": "2020-08-05",
    },
]

sorted_min_salary = [mock_of_jobs[2], mock_of_jobs[1], mock_of_jobs[0]]
sorted_max_salary = [mock_of_jobs[0], mock_of_jobs[1], mock_of_jobs[2]]


def test_sort_by_criteria():
    sort_by(mock_of_jobs, "min_salary")
    assert mock_of_jobs == sorted_min_salary

    sort_by(mock_of_jobs, "max_salary")
    assert mock_of_jobs == sorted_max_salary
