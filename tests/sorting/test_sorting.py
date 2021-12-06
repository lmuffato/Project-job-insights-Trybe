from src.sorting import sort_by


mocked_jobs = [
    {"max_salary": 100, "min_salary": 50},
    {"max_salary": 50, "min_salary": 30},
    {"max_salary": 20, "min_salary": 10},
]

sort_by_min_salary = [mocked_jobs[2], mocked_jobs[1], mocked_jobs[0]]
sort_by_max_salary = [mocked_jobs[0], mocked_jobs[1], mocked_jobs[2]]


def test_sort_by_criteria():
    sort_by(mocked_jobs, "min_salary")
    assert mocked_jobs == sort_by_min_salary

    sort_by(mocked_jobs, "max_salary")
    assert mocked_jobs == sort_by_max_salary
