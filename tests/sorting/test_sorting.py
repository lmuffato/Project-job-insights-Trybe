import pytest
from src.sorting import sort_by

invalid_criteria_error = 'Invalid Key'

jobs_list = [
   {
     'min_salary': '2500',
     'max_salary': '4000',
     'date_posted': '2021-02-16'
   },
   {
     'min_salary': '1000',
     'max_salary': '2500',
     'date_posted': '2021-03-25'
   },
   {
     'min_salary': '1100',
     'max_salary': '5000',
     'date_posted': '2021-04-17'
   },
]

jobs_list_min_salary = [
   {
     'min_salary': '1000',
     'max_salary': '2500',
     'date_posted': '2021-03-25'
   },
   {
     'min_salary': '1100',
     'max_salary': '5000',
     'date_posted': '2021-04-17'
   },
   {
     'min_salary': '2500',
     'max_salary': '4000',
     'date_posted': '2021-02-16'
   },
]

jobs_list_max_salary = [
   {
     'min_salary': '1100',
     'max_salary': '5000',
     'date_posted': '2021-04-17'
   },
   {
     'min_salary': '2500',
     'max_salary': '4000',
     'date_posted': '2021-02-16'
   },
   {
     'min_salary': '1000',
     'max_salary': '2500',
     'date_posted': '2021-03-25'
   },
]

jobs_list_date_posted = [
   {
     'min_salary': '1100',
     'max_salary': '5000',
     'date_posted': '2021-04-17'
   },
   {
     'min_salary': '1000',
     'max_salary': '2500',
     'date_posted': '2021-03-25'
   },
   {
     'min_salary': '2500',
     'max_salary': '4000',
     'date_posted': '2021-02-16'
   },
]


def test_sort_by_criteria():
    sort_by(jobs_list, 'min_salary')
    assert jobs_list == jobs_list_min_salary

    sort_by(jobs_list, 'max_salary')
    assert jobs_list == jobs_list_max_salary

    sort_by(jobs_list, 'date_posted')
    assert jobs_list == jobs_list_date_posted

    with pytest.raises(
        ValueError, match=f'invalid sorting criteria: {invalid_criteria_error}'
    ):
        sort_by(jobs_list, invalid_criteria_error)
