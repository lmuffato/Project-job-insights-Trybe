from src.sorting import sort_by


job_list = [
    {
        "name": "junior developer",
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": 2021-12-29,
    },
    {
        "name": "senior developer",
        "min_salary": 5000,
        "max_salary": 9000,
        "date_posted": 2020-5-5,
    },
    {
        "name": "developer",
        "min_salary": 2900,
        "max_salary": 6500,
        "date_posted": 2021-3-12,
    }
]

sorted_by_max_salary = [
    job_list[1],
    job_list[2],
    job_list[0]
]


sorted_by_min_salary = [
    job_list[0],
    job_list[2],
    job_list[1]
]


def test_sort_by_criteria():
    sort_by(job_list, "min_salary")
    assert(job_list == sorted_by_min_salary)

    sort_by(job_list, "max_salary")
    assert(job_list == sorted_by_max_salary)
