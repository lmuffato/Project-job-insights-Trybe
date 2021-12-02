from src.jobs import read


def get_unique_job_types(path):
    jobs_content = read(path)
    unique_job_types = set()
    for job in jobs_content:
        for job_types in job["job_type"].split(','):

            unique_job_types.add(job_types)

    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        for type_of_job in job['job_type'].split(','):
            if type_of_job == job_type:
                filtered_jobs.append(job)
    return filtered_jobs


# https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings


def get_unique_industries(path):
    jobs_content = read(path)
    unique_industries = set()
    for job in jobs_content:
        for job_industries in job["industry"].split('"'):
            unique_industries.add(job_industries)
    industries = list(filter(None, unique_industries))
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        for job_industry in job['industry'].split('"'):
            if job_industry == industry:
                filtered_jobs.append(job)
    return filtered_jobs

# https://www.pythonpool.com/python-check-if-string-is-integer/


def get_max_salary(path):
    jobs_content = read(path)
    biggest_salary = 0
    for job in jobs_content:
        for salary in job["max_salary"].split('"'):
            if salary.isnumeric() and float(salary) > biggest_salary:
                biggest_salary = float(salary)

    return int(biggest_salary)


def get_min_salary(path):
    jobs_content = read(path)
    lower_salary = get_max_salary(path)
    for job in jobs_content:
        for salary in job["min_salary"].split('"'):
            if salary.isnumeric() and float(salary) < lower_salary:
                lower_salary = float(salary)

    return int(lower_salary)
    pass


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
