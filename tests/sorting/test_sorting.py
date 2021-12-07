from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_mock = [
        {
            "min_salary": 2,
            "max_salary": 4,
            "date_posted": "2021-01-01",
        },
        {
            "min_salary": 1,
            "max_salary": 5,
            "date_posted": "2021-01-03",
        },
        {
            "min_salary": 3,
            "max_salary": 6,
            "date_posted": "2021-01-02",
        },
    ]

    sort_by_min = [jobs_mock[1], jobs_mock[0], jobs_mock[2]]
    sort_by_max = [jobs_mock[2], jobs_mock[1], jobs_mock[0]]
    sort_by_date = [jobs_mock[1], jobs_mock[2], jobs_mock[0]]

    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == sort_by_min

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == sort_by_max

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == sort_by_date
