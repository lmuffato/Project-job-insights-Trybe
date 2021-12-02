from src.jobs import read
import sys


def get_unique_job_types(path):
    jobs_data = read(path)
    unique_job_types = set()

    for job in jobs_data:
        if job["job_type"] != "":
            unique_job_types.add(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    list_of_jobs = []
    for job in jobs:
        if(job['job_type'] == job_type):
            list_of_jobs.append(job)

    return list_of_jobs


def get_unique_industries(path):
    jobs_data = read(path)
    unique_industries = set()
    for job in jobs_data:
        if job["industry"] != "":
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    list_of_industries = []
    for job in jobs:
        if(job['industry'] == industry):
            list_of_industries.append(job)

    return list_of_industries


def get_max_salary(path):
    jobs_data = read(path)
    max_salary = 0

    for job in jobs_data:
        if(job['max_salary'] != '' and not job['max_salary'].isalpha()):
            salary = int(job['max_salary'])
            if(salary > max_salary):
                max_salary = salary

    return max_salary


def get_min_salary(path):
    jobs_data = read(path)
    # Source: https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints
    min_salary = sys.maxsize

    for job in jobs_data:
        if(job['min_salary'] != '' and not job['min_salary'].isalpha()):
            salary = int(job['min_salary'])
            if(salary < min_salary):
                min_salary = salary

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
