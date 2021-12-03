from src.jobs import read


# python sets: https://www.w3schools.com/python/python_sets.asp
# set methods: https://www.w3schools.com/python/python_sets_methods.asp
def get_unique_job_types(path):
    job_list = read(path)
    job_type_set = set()
    for job in job_list:
        job_type_set.add(job["job_type"])
    return job_type_set


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if (job["job_type"] == job_type):
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    job_list = read(path)
    industries_set = set()
    for job in job_list:
        if (job["industry"] != ''):
            industries_set.add(job["industry"])
    return industries_set


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if (job["industry"] == industry):
            job_list.append(job)
    return job_list


# Python Math Functions: https://www.w3schools.com/python/python_math.asp
# Python String IsNumeric():
# https://www.w3schools.com/python/ref_string_isnumeric.asp
def get_max_salary(path):
    job_list = read(path)
    salary_array = []
    for job in job_list:
        if(job["max_salary"].isnumeric()):
            salary_array.append(int(job["max_salary"]))
    return max(salary_array)


def get_min_salary(path):
    job_list = read(path)
    salary_array = []
    for job in job_list:
        if(job["min_salary"].isnumeric()):
            salary_array.append(int(job["min_salary"]))
    return min(salary_array)


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
