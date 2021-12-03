from src.sorting import sort_by


jobs = [
        {
            "id": 1,
            "min_salary": 1000,
            "max_salary": 10000,
            "date_posted": 20180801000000
        },
        {
            "id": 2,
            "min_salary": 900,
            "max_salary": 9000,
            "date_posted": 20180701000000
        },
        {
            "id": 3,
            "min_salary": 800,
            "max_salary": 8000,
            "date_posted": 20180601000000
        },
    ]
jobs2 = [
        {
            "id": 3,
            "min_salary": 800,
            "max_salary": 8000,
            "date_posted": 20180601000000
        },
        {
            "id": 2,
            "min_salary": 900,
            "max_salary": 9000,
            "date_posted": 20180701000000
        },
        {
            "id": 1,
            "min_salary": 1000,
            "max_salary": 10000,
            "date_posted": 20180801000000
        },
    ]


def test_sort_by_criteria():
    sorted2 = sort_by(jobs, "min_salary")
    sorted3 = sort_by(jobs, "max_salary")
    sorted4 = sort_by(jobs, "date_posted")

    assert jobs2 in sorted2
    assert jobs in sorted3
    assert jobs2 in sorted4
