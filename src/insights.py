from jobs import read


def get_unique_job_types(path):
    data = read(path)
    uniques_types_of_jobs = set()
    for job in data:
        if job['job_type'] != '':
            uniques_types_of_jobs.add(job['job_type'])
    return uniques_types_of_jobs


# print(get_unique_job_types('jobs.csv'))   # Teste manual
# python3 -m pytest tests/test_insights.py   # Teste do avaliador


def filter_by_job_type(jobs, job_type):
    filtered_job = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_job.append(job)
    return filtered_job


# job_types = [
#         {"id": 1, "job_type": "PART_TIME"},
#         {"id": 4, "job_type": "OTHER"},
#         {"id": 5, "job_type": "FULL_TIME"},
#         {"id": 6, "job_type": "FULL_TIME"},
# ]
# print(filter_by_job_type(job_types, 'FULL_TIME'))   # Teste manual
# python3 -m pytest tests/test_insights.py   # Teste do avaliador


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for industry in data:
        if industry['industry'] != '':
            unique_industries.add(industry['industry'])
    return unique_industries


# print(get_unique_industries('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    data = read(path)
    max_salaries = set()
    for salary in data:
        if salary['max_salary'] != '':
            max_salaries.add(int(salary['max_salary']))
    return max(max_salaries)


# print(get_max_salary('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def get_min_salary(path):
    data = read(path)
    min_salaries = set()
    for salary in data:
        if salary['max_salary'] != '':
            min_salaries.add(int(salary['min_salary']))
    return min(min_salaries)


# print(get_min_salary('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
