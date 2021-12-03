from src.jobs import read
# from jobs import read
path = 'jobs.csv'


def get_unique_job_types(path):
    jobs_list = read(path)

    jobs_types = set()

    for job in jobs_list:
        jobs_types.add(job['job_type'])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    list_jobs_type = [
      job for job in jobs
      if job_type == job['job_type']
    ]

    return list_jobs_type


def get_unique_industries(path):
    jobs_list = read(path)

    unique_industries = set()

    for job in jobs_list:
        if job['industry'] != '':
            unique_industries.add(job['industry'])

    return unique_industries


def filter_by_industry(jobs, industry):
    list_jobs_industry = [
      job for job in jobs
      if industry == job['industry']
    ]

    return list_jobs_industry


def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        try:
            salaries.add(int(job['max_salary']))
        except ValueError:
            pass

    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        try:
            salaries.add(int(job['min_salary']))
        except ValueError:
            pass

    return min(salaries)


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
