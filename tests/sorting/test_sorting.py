import pytest
from src.sorting import sort_by

mock_jobs = [
    {"max_salary": "3500", "min_salary": "6000", "date_posted": "2021-10-20"},
    {"max_salary": "1000", "min_salary": "1800", "date_posted": "2021-11-20"},
    {"max_salary": "8000", "min_salary": "15000", "date_posted": "2021-12-01"},
    {"max_salary": "1500", "min_salary": "8000", "date_posted": "2021-11-18"},
    {"max_salary": "1500", "min_salary": "3500", "date_posted": "2021-10-31"},
    {"max_salary": "700", "min_salary": "1200", "date_posted": "2021-11-18"},
]

def test_sort_by_criteria():
    pass
