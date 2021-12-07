from src.sorting import sort_by

array_object = [
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2021-06-30",
    },
    {
        "min_salary": 10000,
        "max_salary": 30000,
        "date_posted": "2021-06-30",
    },
    {
        "min_salary": 23000,
        "max_salary": 33000,
        "date_posted": "2021-06-30",
    },
    {
        "min_salary": 12000,
        "max_salary": 32000,
        "date_posted": "2021-06-30",
    },
]

order_min_salary = [
    array_object[3],
    array_object[2],
    array_object[1],
    array_object[0],
]
order_max_salary = [
    array_object[0],
    array_object[1],
    array_object[2],
    array_object[3],
]


def test_sort_by_criteria():

    sort_by(array_object, "min_salary")
    assert array_object == order_min_salary

    sort_by(array_object, "max_salary")
    assert array_object == order_max_salary
