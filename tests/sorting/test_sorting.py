import pytest
from src.sorting import sort_by

invalid_criteria = "Invalid_key"

criterialist = [
    {
        "min_salary": "1500",
        "max_salary": "3500",
        "date_posted": "2021-11-22"
    },
    {
        "min_salary": "1000",
        "max_salary": "3000",
        "date_posted": "2021-10-22"
    },
    {
        "min_salary": "500",
        "max_salary": "1500",
        "date_posted": "2021-12-22"
    },
]


def test_sort_by_criteria():
    sort_by(criterialist, "min_salary")
    assert criterialist == [
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-12-22"
        },
        {
            "min_salary": "1000",
            "max_salary": "3000",
            "date_posted": "2021-10-22"
        },
        {
            "min_salary": "1500",
            "max_salary": "3500",
            "date_posted": "2021-11-22"
        },
    ]
    sort_by(criterialist, "max_salary")
    assert criterialist == [
        {
            "min_salary": "1500",
            "max_salary": "3500",
            "date_posted": "2021-11-22"
        },
        {
            "min_salary": "1000",
            "max_salary": "3000",
            "date_posted": "2021-10-22"
        },
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-12-22"
        },
    ]
    sort_by(criterialist, "date_posted")
    assert criterialist == [
        {
            "min_salary": "500",
            "max_salary": "1500",
            "date_posted": "2021-12-22"
        },
        {
            "min_salary": "1500",
            "max_salary": "3500",
            "date_posted": "2021-11-22"
        },
        {
            "min_salary": "1000",
            "max_salary": "3000",
            "date_posted": "2021-10-22"
        },
    ]
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
    ):
        sort_by(criterialist, invalid_criteria)
