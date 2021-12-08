from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    filter_by_job_type = set()
    for row in jobs_list:
        if (row["job_type"]) != "":
            filter_by_job_type.add(row["job_type"])
    return filter_by_job_type


def filter_by_job_type(jobs, job_type):
    jobs_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_job_type.append(job)
    return jobs_job_type


def get_unique_industries(path):
    jobs_list = read(path)
    jobs_industry = set()
    for row in jobs_list:
        if (row["industry"]) != "":
            jobs_industry.add(row["industry"])
    return jobs_industry


def filter_by_industry(jobs, industry):
    filter_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_by_industry.append(job)
    return filter_by_industry


def get_max_salary(path):
    jobs_list = read(path)
    jobs_max_salary = []
    for row in jobs_list:
        if (row["max_salary"]).isdigit():
            jobs_max_salary.append(int(row["max_salary"]))
    return max(jobs_max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    jobs_min_salary = []
    for row in jobs_list:
        if (row["min_salary"]).isdigit():
            jobs_min_salary.append(int(row["min_salary"]))
    return min(jobs_min_salary)


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
