from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "id": 1,
            "min_salary": 1000,
            "max_salary": 2000,
            "date_posted": "1992-04-12",
        },
        {
            "id": 2,
            "min_salary": 3500,
            "max_salary": 4500,
            "date_posted": "1997-01-14",
        },
        {
            "id": 3,
            "min_salary": 1500,
            "max_salary": 2500,
            "date_posted": "2000-09-10",
        },
    ]

    min_wage = [jobs[0], jobs[2], jobs[1]]
    max_wage = [jobs[1], jobs[2], jobs[0]]
    date_posted_ordered = [jobs[2], jobs[1], jobs[0]]

    sort_by(jobs, "min_salary")
    assert jobs == min_wage

    sort_by(jobs, "max_salary")
    assert jobs == max_wage

    sort_by(jobs, "date_posted")
    assert jobs == date_posted_ordered
