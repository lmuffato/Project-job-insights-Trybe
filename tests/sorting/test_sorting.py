from src.sorting import sort_by

list_of_jobs = [
    {"min_salary": 20, "max_salary": 200, "date_posted": "2021-11-02"},
    {"min_salary": 30, "max_salary": 300, "date_posted": "2021-11-03"},
    {"min_salary": 10, "max_salary": 100, "date_posted": "2021-11-01"},
]

ordered_by_min_salary = [list_of_jobs[2], list_of_jobs[0], list_of_jobs[1]]
ordered_by_max_salary = [list_of_jobs[1], list_of_jobs[0], list_of_jobs[2]]
ordered_by_date_posted = [
    list_of_jobs[1],
    list_of_jobs[0],
    list_of_jobs[2],
]


def test_sort_by_criteria():

    sort_by(list_of_jobs, "min_salary")
    assert list_of_jobs == ordered_by_min_salary

    sort_by(list_of_jobs, "max_salary")
    assert list_of_jobs == ordered_by_max_salary

    sort_by(list_of_jobs, "date_posted")
    assert list_of_jobs == ordered_by_date_posted


# The assert keyword lets you test if a condition in your code returns True
# if not, the program will raise an AssertionError.
# ex: se eu trocar a ordem da variável da linha 9, terei um assertion error
# https://www.w3schools.com/python/ref_keyword_assert.asp
