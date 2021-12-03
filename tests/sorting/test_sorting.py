from src.sorting import sort_by


jobs = [
    {"max_salary": 1000, "min_salary": 100, "date_posted": "2020-05-02"},
    {"max_salary": 212901, "min_salary": 125410, "date_posted": "2020-04-28"},
    {"max_salary": 103279, "min_salary": 94715, "date_posted": "2020-05-05"},
    {"max_salary": 35000, "min_salary": 20000, "date_posted": "2020-05-07"},
    {"max_salary": 143860, "min_salary": 54991, "date_posted": "2020-05-08"},
    {"max_salary": 55893, "min_salary": 46298, "date_posted": "2020-05-01"},
    {"max_salary": 148734, "min_salary": 122296, "date_posted": "2020-04-27"},
]


def test_sort_by_criteria():

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"max_salary": 1000,
         "min_salary": 100,
         "date_posted": "2020-05-02"},
        {"max_salary": 35000,
         "min_salary": 20000,
         "date_posted": "2020-05-07"},
        {"max_salary": 55893,
         "min_salary": 46298,
         "date_posted": "2020-05-01"},
        {"max_salary": 143860,
         "min_salary": 54991,
         "date_posted": "2020-05-08"},
        {"max_salary": 103279,
         "min_salary": 94715,
         "date_posted": "2020-05-05"},
        {"max_salary": 148734,
         "min_salary": 122296,
         "date_posted": "2020-04-27"},
        {"max_salary": 212901,
         "min_salary": 125410,
         "date_posted": "2020-04-28"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"max_salary": 212901,
         "min_salary": 125410,
         "date_posted": "2020-04-28"},
        {"max_salary": 148734,
         "min_salary": 122296,
         "date_posted": "2020-04-27"},
        {"max_salary": 143860,
         "min_salary": 54991,
         "date_posted": "2020-05-08"},
        {"max_salary": 103279,
         "min_salary": 94715,
         "date_posted": "2020-05-05"},
        {"max_salary": 55893,
         "min_salary": 46298,
         "date_posted": "2020-05-01"},
        {"max_salary": 35000,
         "min_salary": 20000,
         "date_posted": "2020-05-07"},
        {"max_salary": 1000,
         "min_salary": 100,
         "date_posted": "2020-05-02"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"max_salary": 143860,
         "min_salary": 54991,
         "date_posted": "2020-05-08"},
        {"max_salary": 35000,
         "min_salary": 20000,
         "date_posted": "2020-05-07"},
        {"max_salary": 103279,
         "min_salary": 94715,
         "date_posted": "2020-05-05"},
        {"max_salary": 1000,
         "min_salary": 100,
         "date_posted": "2020-05-02"},
        {"max_salary": 55893,
         "min_salary": 46298,
         "date_posted": "2020-05-01"},
        {"max_salary": 212901,
         "min_salary": 125410,
         "date_posted": "2020-04-28"},
        {"max_salary": 148734,
         "min_salary": 122296,
         "date_posted": "2020-04-27"},
    ]
