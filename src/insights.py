from src.jobs import read


def get_unique_job_types(path):
    readFile = read(path)
    job_types = set()
    for job in readFile:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    filter_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            filter_list.append(job)
    return filter_list


def get_unique_industries(path):
    readFile = read(path)
    industry = set()
    for row in readFile:
        if row['industry'] != '':
            industry.add(row['industry'])
    return industry


def filter_by_industry(jobs, industry):
    filter_list = []
    for job in jobs:
        if job['industry'] == industry:
            filter_list.append(job)
    return filter_list


def get_max_salary(path):
    readFile = read(path)
    max_salary = []
    for row in readFile:
        salary_row = row['max_salary']
        if salary_row != '' and salary_row != "invalid":
            max_salary.append(int(salary_row))
    return max(max_salary)


def get_min_salary(path):
    readFile = read(path)
    min_salary = []
    for row in readFile:
        salary_row = row['min_salary']
        if salary_row != '' and salary_row != "invalid":
            min_salary.append(int(salary_row))
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
