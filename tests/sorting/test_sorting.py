import pytest
from datetime import date
from src.sorting import sort_by

testDict = [
     {"max_salary": 100, "min_salary": 10,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 150, "min_salary": 100,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 10000, "min_salary": 200,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 15000, "min_salary": 0,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 1500, "min_salary": 0,
      'date_posted': date(1997, 1, 1).isoformat()},
]

sortedByMax = [
     {"max_salary": 15000, "min_salary": 0,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 10000, "min_salary": 200,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 1500, "min_salary": 0,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 150, "min_salary": 100,
      'date_posted': date(1997, 1, 1).isoformat()},
     {"max_salary": 100, "min_salary": 10,
      'date_posted': date(1997, 1, 1).isoformat()},
]

noneList = [None, None, None]


def test_sort_by_criteria():
    pass
    sort_by(testDict, 'max_salary')
    assert testDict == sortedByMax

    with pytest.raises(ValueError, match="invalid sorting criteria: """):
        sort_by(testDict, 'teste')
    with pytest.raises(ValueError, match="invalid sorting criteria: None"):
        sort_by(noneList, None)
