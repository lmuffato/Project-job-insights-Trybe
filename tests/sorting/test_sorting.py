from src.sorting import sort_by


jobs = [
    {
        "min_salary": 4000,
        "max_salary": 5000,
    },
    {
        "min_salary": 3000,
        "max_salary": 4000,
    },
    {
        "min_salary": 2000,
        "max_salary": 3000,
    },
    {
        "min_salary": 1000,
        "max_salary": 2000,
    },
]

sort_by_min_salary = [jobs[3], jobs[2], jobs[1], jobs[0]]
sort_by_max_salary = [jobs[0], jobs[1], jobs[2], jobs[3]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == sort_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sort_by_max_salary
