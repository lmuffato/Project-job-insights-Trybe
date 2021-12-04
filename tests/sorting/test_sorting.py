from src.sorting import sort_by

# mocks

MIN_SALARY = "min_salary"
MAX_SALARY = "max_salary"
DATE_POSTED = "date_posted"

criteria_list = [
    {"max_salary": "3000", "min_salary": "1000", "date_posted": "2021-05-19"},
    {"max_salary": "3500", "min_salary": "1500", "date_posted": "2021-06-23"},
    {"max_salary": "12000", "min_salary": "7000", "date_posted": "2021-05-05"},
    {"max_salary": "4000", "min_salary": "2000", "date_posted": "2021-12-06"},
]

sorted_by_min_salary = [
    {"max_salary": "3000", "min_salary": "1000", "date_posted": "2021-05-19"},
    {"max_salary": "3500", "min_salary": "1500", "date_posted": "2021-06-23"},
    {"max_salary": "4000", "min_salary": "2000", "date_posted": "2021-12-06"},
    {"max_salary": "12000", "min_salary": "7000", "date_posted": "2021-05-05"},
]

sorted_by_max_salary = [
    {"max_salary": "12000", "min_salary": "7000", "date_posted": "2021-05-05"},
    {"max_salary": "4000", "min_salary": "2000", "date_posted": "2021-12-06"},
    {"max_salary": "3500", "min_salary": "1500", "date_posted": "2021-06-23"},
    {"max_salary": "3000", "min_salary": "1000", "date_posted": "2021-05-19"},
]

sorted_by_date = [
    {"max_salary": "4000", "min_salary": "2000", "date_posted": "2021-12-06"},
    {"max_salary": "3500", "min_salary": "1500", "date_posted": "2021-06-23"},
    {"max_salary": "3000", "min_salary": "1000", "date_posted": "2021-05-19"},
    {"max_salary": "12000", "min_salary": "7000", "date_posted": "2021-05-05"},
]


def test_sort_by_criteria():
    sort_by(criteria_list, MIN_SALARY)
    assert criteria_list == sorted_by_min_salary

    sort_by(criteria_list, MAX_SALARY)
    assert criteria_list == sorted_by_max_salary

    sort_by(criteria_list, DATE_POSTED)
    assert criteria_list == sorted_by_date
