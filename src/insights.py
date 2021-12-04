from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs_types = set(job["job_type"] for job in jobs_list)
    print(unique_jobs_types)
    return unique_jobs_types


def filter_by_job_type(jobs, job_type):
    list_of_jobs = []
    for job in jobs:
        if(job['job_type'] == job_type):
            list_of_jobs.append(job)
    return list_of_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = set(
        job["industry"]for job in jobs_list if job["industry"]
    )
    return unique_industries


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
    jobs_list = read(path)
    salary_list = []
    for job in jobs_list:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"]))
    return max(salary_list)


def get_min_salary(path):
    jobs_list = read(path)
    salary_min_list = []
    for job in jobs_list:
        if job["min_salary"].isdigit():
            salary_min_list.append(int(job["min_salary"]))
    return min(salary_min_list)


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
