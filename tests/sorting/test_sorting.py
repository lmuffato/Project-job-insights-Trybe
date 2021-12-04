from src.sorting import sort_by


def test_sort_by_criteria():

    mocked_jobs = [
        {"max_salary": 100, "min_salary": 50, "date_posted": "2013-05-14"},
        {"max_salary": 50, "min_salary": 30, "date_posted": "2013-05-15"},
        {"max_salary": 20, "min_salary": 10, "date_posted": "2013-05-16"},
    ]

    sort_by_min_salary = [mocked_jobs[2], mocked_jobs[1], mocked_jobs[0]]
    sort_by_max_salary = [mocked_jobs[0], mocked_jobs[1], mocked_jobs[2]]
    sort_by_date_posted = [mocked_jobs[2], mocked_jobs[1], mocked_jobs[0]]
    sort_by(mocked_jobs, "min_salary")
    assert mocked_jobs == sort_by_min_salary
    sort_by(mocked_jobs, "max_salary")
    assert mocked_jobs == sort_by_max_salary
    sort_by(mocked_jobs, "date_posted")
    assert mocked_jobs == sort_by_date_posted
