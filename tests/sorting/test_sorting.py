from src.sorting import sort_by


def test_sort_by_criteria():
    mock_jobs = [
        {
            'max_salary': 5500,
            'min_salary': 3500,
            'date_posted': '2021-06-05'
        },
        {
            'max_salary': 7500,
            'min_salary': 5500,
            'date_posted': '2021-06-06'
        },
        {
            'max_salary': 10000,
            'min_salary': 7500,
            'date_posted': '2021-06-04'
        },
    ]

    sorted_by_min_salary = [
        mock_jobs[0],
        mock_jobs[1],
        mock_jobs[2],
    ]

    sorted_by_max_salary = [
        mock_jobs[2],
        mock_jobs[1],
        mock_jobs[0],
    ]

    sorted_by_date_posted = [
        mock_jobs[1],
        mock_jobs[0],
        mock_jobs[2],
    ]

    sort_by(mock_jobs, 'min_salary')
    assert mock_jobs == sorted_by_min_salary
    sort_by(mock_jobs, 'max_salary')
    assert mock_jobs == sorted_by_max_salary
    sort_by(mock_jobs, 'date_posted')
    assert mock_jobs == sorted_by_date_posted
