from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()

    try:
        for job in jobs_list:
            jobs_types.add(job["job_type"])
    except NameError:
        print("Variable 'jobs_list' is not defined")

    return jobs_types


def filter_by_job_type(jobs, job_type):
    job_list = []

    try:
        for job in jobs:
            if job['job_type'] == job_type:
                job_list.append(job)
    except ValueError:
        print("Variable 'jobs_list' is not defined")

    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    industries_list = set()

    try:
        for job in jobs_list:
            industries_list.add(job["industry"])
    except NameError:
        print("Variable 'jobs_list' is not defined")

    industries_list.discard("")

    return industries_list


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
    max_salary = set()

    for job in jobs_list:
        try:
            max_salary.add(int(job["max_salary"]))
        except ValueError:
            pass
    """
    Quando a 'pass' instrução é executada,
    nada acontece,
    mas você evita receber um erro quando o código vazio não é permitido.
    """

    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = set()

    for job in jobs_list:
        try:
            min_salary.add(int(job["min_salary"]))
        except ValueError:
            pass
    """
    Quando a 'pass' instrução é executada,
    nada acontece,
    mas você evita receber um erro quando o código vazio não é permitido.
    """

    return min(min_salary)


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
