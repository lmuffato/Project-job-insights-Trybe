from src.jobs import read


def get_unique_job_types(path):
    readFile = read(path)
    result = []
    for info in readFile:
        if info["job_type"] is None or info["job_type"] in result:
            continue
        else:
            result.append(info["job_type"])
    return result


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result



def get_unique_industries(path):
    readFile = read(path)
    result = []
    for info in readFile:
        if not info["industry"].rstrip() or info["industry"] in result:
            continue
        else:
            result.append(info["industry"])
    return result


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
    readFile = read(path)
    result = 0
    max_salary = "max_salary"
    for info in readFile:
        if (not info[max_salary].rstrip()) or info[max_salary] == 'invalid':
            continue
        elif int(info[max_salary]) < int(result):
            continue
        else:
            result = int(info[max_salary])
    return result


def get_min_salary(path):
    readFile = read(path)
    result = 1000000
    min_salary = "min_salary"
    for info in readFile:
        if (not info[min_salary].rstrip()) or info[min_salary] == 'invalid':
            continue
        elif int(info[min_salary]) > int(result):
            continue
        else:
            result = int(info[min_salary])
    return result


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
