from src.sorting import sort_by

job_list = [
    {"min_salary": 2400, "max_salary": 6000, "date_posted": "2020-06-10"},
    {"min_salary": 100, "max_salary": 2000, "date_posted": "2021-03-01"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2019-05-25"},
]


def test_sort_by_criteria():
    mock_max_salary = [
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "2019-05-25"},
        {"min_salary": 2400, "max_salary": 6000, "date_posted": "2020-06-10"},
        {"min_salary": 100, "max_salary": 2000, "date_posted": "2021-03-01"},
    ]

    mock_min_salary = [
        {"min_salary": 100, "max_salary": 2000, "date_posted": "2021-03-01"},
        {"min_salary": 2400, "max_salary": 6000, "date_posted": "2020-06-10"},
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "2019-05-25"},
    ]

    mock_date_posted = [
        {"min_salary": 100, "max_salary": 2000, "date_posted": "2021-03-01"},
        {"min_salary": 2400, "max_salary": 6000, "date_posted": "2020-06-10"},
        {"min_salary": 3000, "max_salary": 7000, "date_posted": "2019-05-25"},
    ]

    sort_by(job_list, "max_salary")
    assert job_list == mock_max_salary

    sort_by(job_list, "date_posted")
    assert job_list == mock_date_posted

    sort_by(job_list, "min_salary")
    assert job_list == mock_min_salary
