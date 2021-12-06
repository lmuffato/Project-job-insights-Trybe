# Feito com base na explicação do Felipe Flores - T10 - A
from src.sorting import sort_by

mock = [
    {
        "min_salary": 58000,
        "max_salary": 128000,
        "date_posted": "2021-03-06",
    },
    {
        "min_salary": 38000,
        "max_salary": 78000,
        "date_posted": "2018-04-13",
    },
    {
        "min_salary": 3800,
        "max_salary": 9800,
        "date_posted": "2020-08-31",
    },
]

sorted_min_salary = [mock[2], mock[1], mock[0]]
sorted_max_salary = [mock[0], mock[1], mock[2]]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == sorted_min_salary

    sort_by(mock, "max_salary")
    assert mock == sorted_max_salary
