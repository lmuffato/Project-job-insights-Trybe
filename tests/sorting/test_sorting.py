from src.sorting import sort_by
import pytest

jobs_mock = [
  {
    'max_salary': 1200,
    'min_salary': 300,
    'date_posted': '2021-09-24',
  },
  {
    'max_salary': 1300,
    'min_salary': 500,
    'date_posted': '2021-10-07',
  },
  {
    'max_salary': 700,
    'min_salary': 250,
    'date_posted': '2021-01-23',
  },
  {
    'max_salary': 1100,
    'min_salary': 400,
    'date_posted': '2021-09-25',
  }
]


def test_sort_by_criteria():
    sort_by(jobs_mock, 'min_salary')
    assert jobs_mock == [
      {
        'max_salary': 700,
        'min_salary': 250,
        'date_posted': '2021-01-23',
      },
      {
        'max_salary': 1200,
        'min_salary': 300,
        'date_posted': '2021-09-24',
      },
      {
        'max_salary': 1100,
        'min_salary': 400,
        'date_posted': '2021-09-25',
      },
      {
        'max_salary': 1300,
        'min_salary': 500,
        'date_posted': '2021-10-07',
      }
    ]

    sort_by(jobs_mock, 'max_salary')
    assert jobs_mock == [
      {
        'max_salary': 1300,
        'min_salary': 500,
        'date_posted': '2021-10-07',
      },
      {
        'max_salary': 1200,
        'min_salary': 300,
        'date_posted': '2021-09-24',
      },
      {
        'max_salary': 1100,
        'min_salary': 400,
        'date_posted': '2021-09-25',
      },
      {
        'max_salary': 700,
        'min_salary': 250,
        'date_posted': '2021-01-23',
      }
    ]

    sort_by(jobs_mock, 'date_posted')
    assert jobs_mock == [
      {
        'max_salary': 1300,
        'min_salary': 500,
        'date_posted': '2021-10-07',
      },
      {
        'max_salary': 1100,
        'min_salary': 400,
        'date_posted': '2021-09-25',
      },
      {
        'max_salary': 1200,
        'min_salary': 300,
        'date_posted': '2021-09-24',
      },
      {
        'max_salary': 700,
        'min_salary': 250,
        'date_posted': '2021-01-23',
      }
    ]

    criteria = ''
    with pytest.raises(
      ValueError,
      match=f"invalid sorting criteria: {criteria}"
    ):
        sort_by(jobs_mock, criteria)

    criteria = None
    with pytest.raises(
      ValueError,
      match=f"invalid sorting criteria: {criteria}"
    ):
        sort_by(jobs_mock, criteria)
