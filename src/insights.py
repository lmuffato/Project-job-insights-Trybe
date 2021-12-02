from src.jobs import read


def get_unique_job_types(path):
    jobs_read = read(path)
    my_set = set()
    for row in jobs_read:
        if row["job_type"] != "":
            my_set.add(row["job_type"])
    return my_set


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
    pass


def get_unique_industries(path):
    jobs_read = read(path)
    my_set = set()
    for row in jobs_read:
        if row["industry"] != "":
            my_set.add(row["industry"])
    return my_set


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
    pass


def get_max_salary(path):
    jobs_read = read(path)
    my_set = []
    for row in jobs_read:
        if row["max_salary"].isnumeric():
            my_set.append(int(row["max_salary"]))
            max_sal = max(my_set)
    return max_sal


def get_min_salary(path):
    jobs_read = read(path)
    my_set = []
    for row in jobs_read:
        if row["min_salary"].isnumeric():
            my_set.append(int(row["min_salary"]))
            min_sal = min(my_set)
    return min_sal


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
    pass
