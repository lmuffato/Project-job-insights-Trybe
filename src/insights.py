from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return list(set([job["job_type"] for job in jobs]))


def filter_by_job_type(jobs, job_type):
    jobs_filtered = [
        job_filtered
        for job_filtered in jobs
        if job_filtered["job_type"] == job_type
    ]
    return jobs_filtered


def get_unique_industries(path):
    jobs = read(path)

    # jobs_filtered = list(set([
    #     unique_industry['industry'] for unique_industry
    #     in jobs if unique_industry['industry'] != ''
    #     ]))

    jobs_filtered = list(
        set([unique_industry["industry"] for unique_industry in jobs])
    )
    return list(filter(None, jobs_filtered))


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
    salaries = read(path)
    return max(set(
        [unique_salary["max_salary"] for unique_salary in salaries]
    ))


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : strget_unique_job_types
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


# print(read('src/jobs.csv'))
# print(get_unique_job_types("src/jobs.csv"))
# print(get_unique_industries("src/jobs.csv"))
# print(get_max_salary("src/jobs.csv"))
