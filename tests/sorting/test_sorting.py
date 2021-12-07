from src.sorting import sort_by


job_list = [
    {
        "name": "junior developer",
        "min_salary": 2500,
        "max_salary": 4500
    },
    {
        "name": "senior developer",
        "min_salary": 9000,
        "max_salary": 15000,
    },
    {
        "name": "pleno developer",
        "min_salary": 5000,
        "max_salary": 8000,
    }
]

sort_by_min_salary = [
    job_list[0],
    job_list[2],
    job_list[1]
]

sort_by_max_salary = [
    job_list[1],
    job_list[2],
    job_list[0]
]


def test_sort_by_criteria():
    sort_by(job_list, "min_salary")
    assert(job_list == sort_by_min_salary)

    sort_by(job_list, "max_salary")
    assert(job_list == sort_by_max_salary)
