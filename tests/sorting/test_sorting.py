from src.sorting import sort_by


jobs_mock = [
    {
        "min_salary": 50,
        "max_salary": 500,
    },
    {
        "min_salary": 20,
        "max_salary": 600,
    },
    {
        "min_salary": 80,
        "max_salary": 900,
    },
]

sort_by_min = [jobs_mock[1], jobs_mock[0], jobs_mock[2]]
sort_by_max = [jobs_mock[2], jobs_mock[1], jobs_mock[0]]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == sort_by_min

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == sort_by_max
