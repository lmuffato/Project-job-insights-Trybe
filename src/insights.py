from src.jobs import read


def get_unique_job_types(path):
    jobTypes = read(path)
    uniqueJobs = []
    for row in jobTypes:
        if row['job_type'] is None or row['job_type'] not in uniqueJobs:
            uniqueJobs.append(row['job_type'])
    return uniqueJobs


def filter_by_job_type(jobs, job_type):
    jobTypes = []
    for row in jobs:
        if row['job_type'] == job_type:
            jobTypes.append(row)
    return jobTypes


def get_unique_industries(path):
    data = read(path)
    industries = []
    for row in data:
        if row['industry'] not in industries and row['industry']:
            industries.append(row['industry'])
    return industries


'''
def filter_by_industry(jobs, industry):
    industries = []
    for row in jobs:
        if row['industry'] == industry:
            industries.append(row)
    return industries
'''


def get_max_salary(path):
    data = read(path)
    max_salary = []
    for row in data:
        salary_in_row = row['max_salary']
        if salary_in_row != '' and salary_in_row != 'invalid':
            max_salary.append(int(salary_in_row))
    return max(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = []
    for row in data:
        salary_in_row = row['min_salary']
        if salary_in_row != '' and salary_in_row != 'invalid':
            min_salary.append(int(salary_in_row))
    return min(min_salary)


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
