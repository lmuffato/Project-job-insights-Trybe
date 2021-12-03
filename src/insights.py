from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    job_list = read(path)
    for job in job_list:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    job_in_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_in_job_type.append(job)

    return job_in_job_type


def get_unique_industries(path):
    industry_types = set()
    job_list = read(path)
    for job in job_list:
        industry_types.add(job["industry"])

    return industry_types


def filter_by_industry(jobs, industry):
    jobs_in_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_in_industry.append(job)

    return jobs_in_industry


def get_max_salary(path):
    job_list = read(path)
    max_salary = 0
    for job in job_list:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return max_salary


def get_min_salary(path):
    job_list = read(path)
    min_salary = 100000000000
    for job in job_list:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])

    return min_salary


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
