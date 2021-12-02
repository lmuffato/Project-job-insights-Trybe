import csv
from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_read = read(path)
    job_types = []
    for job in jobs_read:
        if job["job_type"] not in job_types and job not in (None, ""):
            job_types.append(job["job_type"])
    return job_types


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
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    results = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        header, *data = reader
        line_count = 0
        for row in data:
            line_count += 1
            if (row["industry"] not in results and
               row["industry"] not in (None, "")):
                results.append(row["industry"])
    return results


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
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
        isdigit**
    """
    reader = read(path)
    max_salary_list = [int(row["max_salary"]) for row in reader
                       if (row["max_salary"].isdigit())]
    return max(max_salary_list)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    reader = read(path)
    min_salary_list = [int(row["min_salary"]) for row in reader
                       if (row["min_salary"].isdigit())]
    return min(min_salary_list)


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
    if type(salary) is not int:
        raise ValueError("The salary isn't an integer")

    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError("The min_salary and max_salary are needed")

    if (
        type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
    ):
        raise ValueError("The min_salary and max_salary aren't integers")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("The max_salary lower than min_salary")

    return job["min_salary"] <= salary <= job["max_salary"]


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
    in_range = [
        job for job in jobs
        if (
            isinstance(salary, int) and isinstance(job["min_salary"], int)
            and isinstance(job["max_salary"], int)
            and job["min_salary"] <= salary <= job["max_salary"]
        )
         ]
    return in_range
