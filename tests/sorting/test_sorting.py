from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "max_salary": "2000",
            "min_salary": "130",
            "date_posted": "2020-03-04"
        },
        {
            "max_salary": "1000",
            "min_salary": "30",
            "date_posted": "2020-02-01"
        },
        {
            "max_salary": "10000",
            "min_salary": "200",
            "date_posted": "2020-08-12"
        },
        {
            "max_salary": "50000",
            "min_salary": "0",
            "date_posted": "2020-04-28"
        },
        {
            "max_salary": "1500",
            "min_salary": "10",
            "date_posted": "2020-05-08"
        },
        {
            "max_salary": "1400",
            "min_salary": "15",
            "date_posted": "2020-02-13"
        },
    ]

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "0"

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == "50000"

    sort_by(jobs, "date_posted")
    assert jobs[0]["date_posted"] == "2020-08-12"
