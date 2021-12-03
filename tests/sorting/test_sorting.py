from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "max_salary": "1000",
            "min_salary": "100",
            "date_posted": "2021-02-01",
        },
        {
            "max_salary": "2000",
            "min_salary": "200",
            "date_posted": "2021-03-01",
        },
        {
            "max_salary": "3000",
            "min_salary": "300",
            "date_posted": "2021-01-01",
        },
    ]
    results_expected = [
        {
            "criteria": "max_salary",
            "result": [
                {
                    "max_salary": "3000",
                    "min_salary": "300",
                    "date_posted": "2021-01-01",
                },
                {
                    "max_salary": "2000",
                    "min_salary": "200",
                    "date_posted": "2021-03-01",
                },
                {
                    "max_salary": "1000",
                    "min_salary": "100",
                    "date_posted": "2021-02-01",
                },
            ],
        },
        {
            "criteria": "min_salary",
            "result": [
                {
                    "max_salary": "1000",
                    "min_salary": "100",
                    "date_posted": "2021-02-01",
                },
                {
                    "max_salary": "2000",
                    "min_salary": "200",
                    "date_posted": "2021-03-01",
                },
                {
                    "max_salary": "3000",
                    "min_salary": "300",
                    "date_posted": "2021-01-01",
                },
            ],
        },
        {
            "criteria": "date_posted",
            "result": [
                {
                    "max_salary": "2000",
                    "min_salary": "200",
                    "date_posted": "2021-03-01",
                },
                {
                    "max_salary": "1000",
                    "min_salary": "100",
                    "date_posted": "2021-02-01",
                },
                {
                    "max_salary": "3000",
                    "min_salary": "300",
                    "date_posted": "2021-01-01",
                },
            ],
        },
    ]
    for test in results_expected:
        sort_by(jobs, test["criteria"])
        assert jobs == test["result"]
