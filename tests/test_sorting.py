from src.sorting import sort_by

mock_input = [
    {
        "max_salary": 120000,
        "min_salary": 80001,
        "date_posted": "2021-04-01",
    },
    {
        "max_salary": 80000,
        "min_salary": 30001,
        "date_posted": "2021-03-01",
    },
    {
        "max_salary": 30000,
        "min_salary": 10001,
        "date_posted": "2021-02-01",
    },
    {
        "max_salary": 10000,
        "min_salary": 3000,
        "date_posted": "2021-01-01",
    },
]


result_sorted_by_max_salary = [
    # mock_input[0], mock_input[1], mock_input[2], mock_input[3]
    {
        "max_salary": 120000,
        "min_salary": 80001,
        "date_posted": "2021-04-01",
    },
    {
        "max_salary": 80000,
        "min_salary": 30001,
        "date_posted": "2021-03-01",
    },
    {
        "max_salary": 30000,
        "min_salary": 10001,
        "date_posted": "2021-02-01",
    },
    {
        "max_salary": 10000,
        "min_salary": 3000,
        "date_posted": "2021-01-01",
    },
]

result_sorted_by_min_salary = [
    # mock_input[3], mock_input[2], mock_input[1], mock_input[0]
    {
        "max_salary": 10000,
        "min_salary": 3000,
        "date_posted": "2021-01-01",
    },
    {
        "max_salary": 30000,
        "min_salary": 10001,
        "date_posted": "2021-02-01",
    },
    {
        "max_salary": 80000,
        "min_salary": 30001,
        "date_posted": "2021-03-01",
    },
    {
        "max_salary": 120000,
        "min_salary": 80001,
        "date_posted": "2021-04-01",
    },
]


def test_sort_by_criteria():
    sort_by(mock_input, "max_salary")
    assert mock_input == result_sorted_by_max_salary

    sort_by(mock_input, "min_salary")
    assert mock_input == result_sorted_by_min_salary
