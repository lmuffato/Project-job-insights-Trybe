import pytest
from datetime import date
from src.sorting import sort_by

testDict = [
     {"max_salary": 100, "min_salary": 10, 'date_posted': date(1997, 4, 2)},
     {"max_salary": 150, "min_salary": 100, 'date_posted': date(1998, 4, 2)},
     {"max_salary": 10000, "min_salary": 200, 'date_posted': date(1999, 4, 2)},
     {"max_salary": 15000, "min_salary": 0, 'date_posted': date(2000, 4, 2)},
     {"max_salary": 1500, "min_salary": 0, 'date_posted': date(2001, 4, 2)},
]


def test_sort_by_criteria():
    with pytest.raises(ValueError):
        sort_by(testDict[0], 'teste')
    byMax = sort_by(testDict, 'max_salary')
    byMin = sort_by(testDict, 'min_salary')
    by_date = sort_by(testDict, 'date_posted')
    assert byMax[0]['max_salary'] == 15000
    assert byMin[4]['min_salary'] == 200
    assert by_date[0]['min_salary'] == 10
