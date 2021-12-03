import pytest
from src.sorting import sort_by

mock_jobs = [
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-10-30"},
    {"min_salary": "1000", "max_salary": "1800", "date_posted": "2021-10-27"},
    {"min_salary": "8000", "max_salary": "15000", "date_posted": "2021-10-26"},
    {"min_salary": "2000", "max_salary": "8000", "date_posted": "2021-10-28"},
    {"min_salary": "1500", "max_salary": "3500", "date_posted": "2021-10-31"},
    {"min_salary": "700", "max_salary": "1200", "date_posted": "2021-10-29"},
]

expected_sort_by_min_salary_output = [
    {"min_salary": "700", "max_salary": "1200", "date_posted": "2021-10-29"},
    {"min_salary": "1000", "max_salary": "1800", "date_posted": "2021-10-27"},
    {"min_salary": "1500", "max_salary": "3500", "date_posted": "2021-10-31"},
    {"min_salary": "2000", "max_salary": "8000", "date_posted": "2021-10-28"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-10-30"},
    {"min_salary": "8000", "max_salary": "15000", "date_posted": "2021-10-26"},
]

expected_sort_by_max_salary_output = [
    {"min_salary": "8000", "max_salary": "15000", "date_posted": "2021-10-26"},
    {"min_salary": "2000", "max_salary": "8000", "date_posted": "2021-10-28"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-10-30"},
    {"min_salary": "1500", "max_salary": "3500", "date_posted": "2021-10-31"},
    {"min_salary": "1000", "max_salary": "1800", "date_posted": "2021-10-27"},
    {"min_salary": "700", "max_salary": "1200", "date_posted": "2021-10-29"},
]

expected_sort_by_date_posted_output = [
    {"min_salary": "1500", "max_salary": "3500", "date_posted": "2021-10-31"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-10-30"},
    {"min_salary": "8000", "max_salary": "15000", "date_posted": "2021-10-26"},
    {"min_salary": "1000", "max_salary": "1800", "date_posted": "2021-10-27"},
    {"min_salary": "2000", "max_salary": "8000", "date_posted": "2021-10-28"},
    {"min_salary": "700", "max_salary": "1200", "date_posted": "2021-10-29"},
]


def test_sort_by_criteria():
    sort_by(mock_jobs, 'min_salary')
    assert mock_jobs == expected_sort_by_min_salary_output

    sort_by(mock_jobs, 'max_salary')
    assert mock_jobs == expected_sort_by_max_salary_output

    sort_by(mock_jobs, 'date_posted')
    assert mock_jobs == expected_sort_by_date_posted_output


with pytest.raises(ValueError, match="invalid sorting criteria: """):
    sort_by(mock_jobs, "")

with pytest.raises(ValueError, match="invalid sorting criteria: None"):
    sort_by(mock_jobs, None)
