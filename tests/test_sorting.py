from src.sorting import sort_by

mock_input = [
    {
        "min_salary": 80001,
        "max_salary": 120000,
        "date_posted": "2021-04-01",
    },
    {
        "min_salary": 30001,
        "max_salary": 80000,
        "date_posted": "2021-03-01",
    },
    {
        "min_salary": 10001,
        "max_salary": 30000,
        "date_posted": "2021-02-01",
    },
]


result_sorted_by_max_salary = [
    mock_input[0], mock_input[1], mock_input[2]]

result_sorted_by_min_salary = [
    mock_input[2], mock_input[1], mock_input[0]]


def test_sort_by_criteria():
    sort_by(mock_input, "min_salary")
    assert mock_input == result_sorted_by_min_salary

    sort_by(mock_input, "max_salary")
    assert mock_input == result_sorted_by_max_salary
