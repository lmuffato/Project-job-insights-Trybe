from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    job_list = read(path)

    for job in job_list:
        job_types.add(job["job_type"])
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
    return []


def get_unique_industries(path):
    industries = set()
    industry_list = read(path)

    for row in industry_list:
        if row["industry"] != "":
            industries.add(row["industry"])

    return industries


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
    salary_list = read(path)
    max_salary = 0

    for row in salary_list:
        row_salary = row["max_salary"]
        if row_salary != "" and row_salary != "invalid":
            if int(row_salary) > max_salary:
                max_salary = int(row_salary)

    return max_salary


def get_min_salary(path):
    salary_list = read(path)
    min_salary = -1

    for row in salary_list:
        row_salary = row["min_salary"]
        if row_salary != "" and row_salary != "invalid":
            if min_salary == -1:
                min_salary = int(row_salary)
            if int(row_salary) < min_salary:
                min_salary = int(row_salary)

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
