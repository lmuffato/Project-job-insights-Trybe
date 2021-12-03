from src.sorting import sort_by


test_jobs_list = [
    {
        "name": "Veterinária",
        "min_salary": 2800,
        "max_salary": 5900,
        "date_posted": 2021-10-22,
    },
    {
        "name": "Advogado",
        "min_salary": 4000,
        "max_salary": 7900,
        "date_posted": 2020-12-4,
    },
    {
        "name": "Psicologa",
        "min_salary": 2200,
        "max_salary": 6000,
        "date_posted": 2021-9-16,
    }
]

result_expect_when_sorted_by_min_salary = [
    test_jobs_list[2],
    test_jobs_list[0],
    test_jobs_list[1]
]

result_expect_when_sorted_by_max_salary = [
    test_jobs_list[1],
    test_jobs_list[2],
    test_jobs_list[0]
]


def test_sort_by_criteria():
    sort_by(test_jobs_list, "min_salary")
    assert(test_jobs_list == result_expect_when_sorted_by_min_salary)

    sort_by(test_jobs_list, "max_salary")
    assert(test_jobs_list == result_expect_when_sorted_by_max_salary)
