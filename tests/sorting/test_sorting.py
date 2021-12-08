from src.sorting import sort_by

jobs_mock = [
   {
     "min_salary": 1000,
     "max_salary": 7000,
     "date_posted": "2021-01-01"
   },
   {
     "min_salary": 2000,
     "max_salary": 8000,
     "date_posted": "2021-01-02"
   },
   {
     "min_salary": 3000,
     "max_salary": 9000,
     "date_posted": "2021-01-03"
   },
]

min_salary_mock = [
    {
     "min_salary": 1000,
     "max_salary": 7000,
     "date_posted": "2021-01-01"
    },
    {
     "min_salary": 2000,
     "max_salary": 8000,
     "date_posted": "2021-01-02"
    },
    {
     "min_salary": 3000,
     "max_salary": 9000,
     "date_posted": "2021-01-03"
    },
]

max_salary_mock = [
  {
    "min_salary": 3000,
    "max_salary": 9000,
    "date_posted": "2021-01-03"
  },
  {
    "min_salary": 2000,
    "max_salary": 8000,
    "date_posted": "2021-01-02"
  },
  {
    "min_salary": 1000,
    "max_salary": 7000,
    "date_posted": "2021-01-01"
  },
]

date_posted_mock = [
  {
    "min_salary": 3000,
    "max_salary": 9000,
    "date_posted": "2021-01-03"
  },
  {
    "min_salary": 2000,
    "max_salary": 8000,
    "date_posted": "2021-01-02"
  },
  {
    "min_salary": 1000,
    "max_salary": 7000,
    "date_posted": "2021-01-01"
  },
]


def test_sort_by_criteria():
    sort_by(jobs_mock, "min_salary")
    assert jobs_mock == min_salary_mock

    sort_by(jobs_mock, "max_salary")
    assert jobs_mock == max_salary_mock

    sort_by(jobs_mock, "date_posted")
    assert jobs_mock == date_posted_mock
