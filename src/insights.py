from src.jobs import read

def get_unique_job_types(path):
    data =  read(path)
    categories = set()
    for job in data:
        if job["job_type"] !== "":
            categories.add(job["job_type"])

    return categories


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for industry in data:
        if industry["industry"] !== "":
            industries.add(industry)["industry"]
    return industries


def filter_by_industry(jobs, industry):
    list = []
    for job in jobs:
        if job["industry"] == industry:
            list.append(job)
    return list


def get_max_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["max_salary"] !== "":
            try:
                salaries.add(int(salary["max_salary"]))
            except ValueError:
                print("Error")
    return max(salaries)


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
