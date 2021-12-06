import pytest
from src.sorting import sort_by

jobs1 = [
    {
     "min_salary": 3000,
     "max_salary": 99000,
     "date_posted": "2021/11/11"},
    {
     "min_salary": 2000,
     "max_salary": 4000,
     "date_posted": "2021/11/10"},
    {
     "min_salary": 8000,
     "max_salary": 15000,
     "date_posted": "2021/11/09"},
    {
     "min_salary": 1000,
     "max_salary": 5000,
     "date_posted": "2021/11/08"}
]

jobs2 = [
    {
     "min_salary": 1000,
     "max_salary": 5000,
     "date_posted": "2021/11/08"},
    {
     "min_salary": 2000,
     "max_salary": 4000,
     "date_posted": "2021/11/10"},
    {
     "min_salary": 3000,
     "max_salary": 99000,
     "date_posted": "2021/11/11"},
    {
     "min_salary": 8000,
     "max_salary": 15000,
     "date_posted": "2021/11/09"},

    ]


def test_sort_by_criteria():
    sort_by(jobs1, "min_salary")
    assert jobs1 == jobs2
    with pytest.raises(ValueError):
        assert sort_by([], "oioioio") is None
    with pytest.raises(ValueError):
        assert sort_by(jobs1, "") is None
