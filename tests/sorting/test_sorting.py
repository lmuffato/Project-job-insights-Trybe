from src.sorting import sort_by
import pytest

mock = [
  {
    'max_salary': 3000,
    'min_salary': 2000,
    'date_posted': '2021-04-05',
  },
  {
    'max_salary': 2850,
    'min_salary': 2100,
    'date_posted': '2021-07-05',
  },
  {
    'max_salary': 3100,
    'min_salary': 2850,
    'date_posted': '2021-09-30',
  },
  {
    'max_salary': 6100,
    'min_salary': 3000,
    'date_posted': '2021-12-07',
  }
]


def test_sort_by_criteria():
    sort_by(mock, 'min_salary')
    assert mock == [
      {
        'max_salary': 3000,
        'min_salary': 2000,
        'date_posted': '2021-04-05',
      },
      {
        'max_salary': 2850,
        'min_salary': 2100,
        'date_posted': '2021-07-05',
      },
      {
        'max_salary': 3100,
        'min_salary': 2850,
        'date_posted': '2021-09-30',
      },
      {
        'max_salary': 6100,
        'min_salary': 3000,
        'date_posted': '2021-12-07',
      }
    ]

    sort_by(mock, 'max_salary')
    assert mock == [
      {
        'max_salary': 6100,
        'min_salary': 3000,
        'date_posted': '2021-12-07',
      },
      {
        'max_salary': 3100,
        'min_salary': 2850,
        'date_posted': '2021-09-30',
      },
      {
        'max_salary': 3000,
        'min_salary': 2000,
        'date_posted': '2021-04-05',
      },
      {
        'max_salary': 2850,
        'min_salary': 2100,
        'date_posted': '2021-07-05',
      }
    ]

    sort_by(mock, 'date_posted')
    assert mock == [
      {
        'max_salary': 6100,
        'min_salary': 3000,
        'date_posted': '2021-12-07',
      },
      {
        'max_salary': 3100,
        'min_salary': 2850,
        'date_posted': '2021-09-30',
      },
      {
        'max_salary': 2850,
        'min_salary': 2100,
        'date_posted': '2021-07-05',
      },
      {
        'max_salary': 3000,
        'min_salary': 2000,
        'date_posted': '2021-04-05',
      }
    ]

    criteria = ''
    with pytest.raises(
      ValueError,
      match=f"invalid sorting criteria: {criteria}"
    ):
        sort_by(mock, criteria)

    criteria = None
    with pytest.raises(
      ValueError,
      match=f"invalid sorting criteria: {criteria}"
    ):
        sort_by(mock, criteria)
