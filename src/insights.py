from src.jobs import read


def get_unique_job_types(path):

    list_jobs = read(path)

    unique_jobs = set()

    for jobs in list_jobs:
        for job_type in jobs["job_type"].split(","):
            unique_jobs.add(job_type)

    return unique_jobs


def filter_by_job_type(jobs, job_type):
    job_type_list = []
    for job in jobs:
        if job_type == job["job_type"]:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):

    list_industries = read(path)

    unique_industries = set()

    for industries in list_industries:

        if industries["industry"] != "":
            unique_industries.add(industries["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if industry == job["industry"]:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    list_industries = read(path)

    max_salary = set()

    for industries in list_industries:
        try:
            max_salary.add(int(float(industries["max_salary"])))
        except ValueError:
            pass

    return max(max_salary)


def get_min_salary(path):
    list_industries = read(path)

    min_salary = set()

    for industries in list_industries:
        try:
            min_salary.add(int(float(industries["min_salary"])))
        except ValueError:
            pass

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


    """
    return []
