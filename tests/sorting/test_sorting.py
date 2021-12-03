from src.sorting import sort_by

jobs = [
    {"min_salary": 1, "max_salary": 25, "date_posted": "2021-12-03"},
    {"min_salary": 500, "max_salary": 15000, "date_posted": "2021-05-05"},
    {"min_salary": 2000, "max_salary": 13000, "date_posted": "2010-12-25"},
    {"min_salary": 9000, "max_salary": 20000, "date_posted": "2019-07-25"},
]

mock_min_salary = [
    {"min_salary": 1, "max_salary": 25, "date_posted": "2021-12-03"},
    {"min_salary": 500, "max_salary": 15000, "date_posted": "2021-05-05"},
    {"min_salary": 2000, "max_salary": 13000, "date_posted": "2010-12-25"},
    {"min_salary": 9000, "max_salary": 20000, "date_posted": "2019-07-25"},
]

mock_max_salary = [
      {"min_salary": 9000, "max_salary": 20000, "date_posted": "2019-07-25"},
      {"min_salary": 500, "max_salary": 15000, "date_posted": "2021-05-05"},
      {"min_salary": 2000, "max_salary": 13000, "date_posted": "2010-12-25"},
      {"min_salary": 1, "max_salary": 25, "date_posted": "2021-12-03"},
  ]

mock_date_posted = [
    {"min_salary": 1, "max_salary": 25, "date_posted": "2021-12-03"},
    {"min_salary": 500, "max_salary": 15000, "date_posted": "2021-05-05"},
    {"min_salary": 9000, "max_salary": 20000, "date_posted": "2019-07-25"},
    {"min_salary": 2000, "max_salary": 13000, "date_posted": "2010-12-25"},
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == mock_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == mock_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == mock_date_posted
