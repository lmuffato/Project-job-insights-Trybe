from src.sorting import sort_by


list_of_jobs = [
    {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2019-06-05'},
    {'min_salary': 2000, 'max_salary': 4000, 'date_posted': '2020-06-05'},
    {'min_salary': 4000, 'max_salary': 16000, 'date_posted': '2015-06-05'},
]


def test_sort_by_criteria():
    max_salary_order = [
        {'min_salary': 4000, 'max_salary': 16000, 'date_posted': '2015-06-05'},
        {'min_salary': 2000, 'max_salary': 4000, 'date_posted': '2020-06-05'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2019-06-05'},
    ]

    sort_by(list_of_jobs, 'max_salary')
    assert list_of_jobs == max_salary_order

    min_salary_order = [
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2019-06-05'},
        {'min_salary': 2000, 'max_salary': 4000, 'date_posted': '2020-06-05'},
        {'min_salary': 4000, 'max_salary': 16000, 'date_posted': '2015-06-05'},
    ]

    sort_by(list_of_jobs, 'min_salary')
    assert list_of_jobs == min_salary_order

    date_posted_order = [
        {'min_salary': 2000, 'max_salary': 4000, 'date_posted': '2020-06-05'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2019-06-05'},
        {'min_salary': 4000, 'max_salary': 16000, 'date_posted': '2015-06-05'},
    ]

    sort_by(list_of_jobs, 'date_posted')
    assert list_of_jobs == date_posted_order
