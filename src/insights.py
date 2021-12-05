from src.jobs import read


def get_unique_job_types(path):
    lists = read(path)
    job_types = set(job["job_type"] for job in lists)
    # forma como foi feito o set feita com base no código do Felipe Flores
    # e com o curso
    # https://www.udemy.com/share/101rZm3@scTLs4W_HnfHdggDJ233MraWhwQHXw6VtQintOzz0spHZHhTtyjM0slSpZhl0nL8Rg==/
    #  List Comprehension em Python
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    lists = read(path)
    unique_industries = set(job["industry"]
                            for job in lists
                            if job["industry"] != '')
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    list = read(path)
    max_salaries = []
    for job in list:
        if (job["max_salary"].isnumeric()):
            max_salaries.append(int(job["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    list = read(path)
    min_salaries = []
    for job in list:
        if (job["min_salary"].isnumeric()):
            min_salaries.append(int(job["min_salary"]))

    return min(min_salaries)


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
