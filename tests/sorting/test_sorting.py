from src.sorting import sort_by

job_list = [
    {
        "min_salary": 10,
        "max_salary": 20,
        "date_posted": 2020-4-28,
    },
    {
        "min_salary": 100,
        "max_salary": 200,
        "date_posted": 2020-6-7,
    },
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": 2020-6-6,
    },
]


def test_sort_by_criteria():
    assert sort_by(job_list, "min_salary") == [
        {
            "min_salary": 10,
            "max_salary": 20,
            "date_posted": 2020-4-28,
        },
        {
            "min_salary": 100,
            "max_salary": 200,
            "date_posted": 2020-6-7,
        },
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": 2020-6-6,
        },
    ]
    assert sort_by(job_list, "max_salary") == [
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": 2020-6-6,
        },
        {
            "min_salary": 100,
            "max_salary": 200,
            "date_posted": 2020-6-7,
        },
        {
            "min_salary": 10,
            "max_salary": 20,
            "date_posted": 2020-4-28,
        },
    ]
    assert sort_by(job_list, "date_posted") == [
        {
            "min_salary": 100,
            "max_salary": 200,
            "date_posted": 2020-6-7,
        },
        {
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": 2020-6-6,
        },
        {
            "min_salary": 10,
            "max_salary": 20,
            "date_posted": 2020-4-28,
        },
    ]
    pass
