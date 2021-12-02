from src.jobs import read


def get_unique_job_types(path):
    my_files = read(path)

    my_var = set()

    for file in my_files:
        my_var.add(file["job_type"])

    return my_var


def filter_by_job_type(jobs, job_type):
    my_jobs = [job for job in jobs if job["job_type"] == job_type]
    return my_jobs


def get_unique_industries(path):
    file = read(path)

    industry = set()

    for item in file:
        if item["industry"] != "":
            industry.add(item["industry"])

    return industry


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
    file = read(path)

    max_salaries = [
        int(item["max_salary"])
        for item in file
        if item["max_salary"] != ""
        and item["max_salary"].isnumeric()
        ]

    return max(max_salaries)


def get_min_salary(path):
    file = read(path)

    min_salaries = [
        int(item["min_salary"])
        for item in file
        if item["min_salary"] != ""
        and item["min_salary"].isnumeric()
        ]

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
