from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_list = set()
    for job in jobs:
        jobs_list.add(job["job_type"])
    return jobs_list


def get_unique_industries(path):
    jobs = read(path)
    industries = set(job["industry"] for job in jobs if job["industry"] != '')
    return industries


def get_max_salary(path):
    jobs = read(path)
    salaries = [int(job["max_salary"]) for job in jobs
                if job["max_salary"] != "" and job["max_salary"].isnumeric()]
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = [int(job["min_salary"]) for job in jobs
                if job["min_salary"] != "" and job["min_salary"].isnumeric()]
    return min(salaries)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


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
