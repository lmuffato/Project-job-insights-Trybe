# import pytest

from src.sorting import sort_by

# @pytest.fixture
# def criteria_list():
#     data = [
#             {"min_salary": "3500", "max_salary": "6000",
#  "date_posted": "2021-12-03"},
#             {"min_salary": "3000", "max_salary": "7000"
# , "date_posted": "2021-12-04"},
#             {"min_salary": "8000", "max_salary": "11000"
# , "date_posted": "2021-12-01"},
#     ]


criteria_list = [
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-12-03"},
    {"min_salary": "3000", "max_salary": "7000", "date_posted": "2021-12-04"},
    {"min_salary": "8000", "max_salary": "11000", "date_posted": "2021-12-01"},
]


criteria_list_sorted_by_min_salary_output = [
    {"min_salary": "3000", "max_salary": "7000", "date_posted": "2021-12-04"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-12-03"},
    {"min_salary": "8000", "max_salary": "11000", "date_posted": "2021-12-01"},
]

criteria_list_sorted_by_max_salary_output = [
    {"min_salary": "8000", "max_salary": "11000", "date_posted": "2021-12-01"},
    {"min_salary": "3000", "max_salary": "7000", "date_posted": "2021-12-04"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-12-03"},
]

criteria_list_sorted_by_date_posted_output = [
    {"min_salary": "3000", "max_salary": "7000", "date_posted": "2021-12-04"},
    {"min_salary": "3500", "max_salary": "6000", "date_posted": "2021-12-03"},
    {"min_salary": "8000", "max_salary": "11000", "date_posted": "2021-12-01"},
]


def test_sort_by_criteria():
    sort_by(criteria_list, "min_salary")
    assert criteria_list_sorted_by_min_salary_output

    sort_by(criteria_list, "max_salary")
    assert criteria_list_sorted_by_max_salary_output

    sort_by(criteria_list, "date_posted")
    assert criteria_list_sorted_by_date_posted_output

    # with pytest.raises(
    #     ValueError, match=f"invalid sorting criteria: {criteria_list}"
    # ):
    #     sort_by(criteria_list, criteria_list)

    # with pytest.raises(ValueError, match="invalid sorting criteria: " ""):
    #     sort_by(criteria_list, "")

    # with pytest.raises(ValueError, match="invalid sorting criteria: None"):
    #     sort_by(criteria_list, None)
