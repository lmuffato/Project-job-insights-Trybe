from src.sorting import sort_by


list_of_jobs = [
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 2000,
            'date_posted': '2019-06-05'
        },
        {
            'title': 'Back end developer',
            'min_salary': 1000,
            'max_salary': 3000,
            'date_posted': '2020-08-15'
        },
        {
            'title': 'Full stack end developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2015-12-11'
        }
    ]


def test_sort_by_criteria():
    max_salary_order = [{
        'title': 'Full stack end developer',
        'min_salary': 4000,
        'max_salary': 8000,
        'date_posted': '2015-12-11'
        },
        {
            'title': 'Back end developer',
            'min_salary': 1000,
            'max_salary': 3000,
            'date_posted': '2020-08-15'
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 2000,
            'date_posted': '2019-06-05'
        }]

    assert sort_by(list_of_jobs, 'max_salary') is max_salary_order

    min_salary_order = [{
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 2000,
            'date_posted': '2019-06-05'
        },
        {
            'title': 'Back end developer',
            'min_salary': 1000,
            'max_salary': 3000,
            'date_posted': '2020-08-15'
        },
        {
            'title': 'Full stack end developer',
            'min_salary': 4000,
            'max_salary': 8000,
            'date_posted': '2015-12-11'
        }]

    assert sort_by(list_of_jobs, 'min_salary') is min_salary_order

    date_posted_order = [{
        'title': 'Full stack end developer',
        'min_salary': 4000,
        'max_salary': 8000,
        'date_posted': '2015-12-11'
        },
        {
            'title': 'Back end developer',
            'min_salary': 1000,
            'max_salary': 3000,
            'date_posted': '2020-08-15'
        },
        {
            'title': 'Front end developer',
            'min_salary': 1000,
            'max_salary': 2000,
            'date_posted': '2019-06-05'
        }]

    assert sort_by(list_of_jobs, 'date_posted') is date_posted_order

    invalid_order = [
        {'min_salary': 4000, 'max_salary': 8000, 'date_posted': '2015-12-11'},
        {'min_salary': 3000, 'max_salary': 5000, 'date_posted': '2015-10-11'},
        {'min_salary': '', 'max_salary': 8000, 'date_posted': '2015-12-11'},
    ]

    assert sort_by(list_of_jobs, 'min_salary') is invalid_order
