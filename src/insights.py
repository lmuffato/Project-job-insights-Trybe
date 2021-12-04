from src.jobs import read


def get_unique_job_types(path):
    jobs_dict = read(path)
    # for jobs in jobs_dict:
    #     all_jobs.add(jobs["job_type"])
    all_jobs = {jobs["job_type"] for jobs in jobs_dict}

    return all_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_dict = read(path)
    all_jobs = set()
    for jobs in jobs_dict:
        if jobs["industry"]:
            all_jobs.add(jobs["industry"])
    return all_jobs


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
    jobs_dict = read(path)
    max_salary = 0
    for jobs in jobs_dict:
        if jobs["max_salary"] and jobs["max_salary"] != 'invalid':
            salary = int(jobs["max_salary"])
            if salary > max_salary:
                max_salary = salary

    return max_salary


def get_min_salary(path):
    jobs_dict = read(path)
    min_salary = get_max_salary(path)
    for jobs in jobs_dict:
        if jobs["min_salary"] and jobs["min_salary"] != 'invalid':
            salary = int(jobs["min_salary"])
            if salary < min_salary:
                min_salary = salary

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
