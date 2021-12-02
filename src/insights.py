from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    jobs_types_list = dict()
    for job in jobs_list:
        if job["job_type"] not in jobs_types_list:
            jobs_types_list[job["job_type"]] = 0
        jobs_types_list[job["job_type"]] += 1
    return jobs_types_list


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
    job_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    jobs_industries_list = dict()
    for job in jobs_list:
        if len(job["industry"]) != 0:
            if job["industry"] not in jobs_industries_list:
                jobs_industries_list[job["industry"]] = 0
            jobs_industries_list[job["industry"]] += 1
    return jobs_industries_list


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
    job_industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_industry_list.append(job)
    return job_industry_list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs_list = read(path)
    jobs_min_salary = 0
    for job in jobs_list:
        if len(job["max_salary"]) != 0 and not job["max_salary"].isalpha():
            current_salary = int(job["max_salary"])
            if jobs_min_salary == 0:
                jobs_min_salary = current_salary
            elif jobs_min_salary < current_salary:
                jobs_min_salary = current_salary
    return jobs_min_salary


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
    jobs_list = read(path)
    jobs_min_salary = 0
    for job in jobs_list:
        if len(job["min_salary"]) != 0 and not job["min_salary"].isalpha():
            current_salary = int(job["min_salary"])
            if jobs_min_salary == 0:
                jobs_min_salary = current_salary
            elif jobs_min_salary > current_salary:
                jobs_min_salary = current_salary
    return jobs_min_salary


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
    if not ("min_salary" in job and "max_salary" in job):
        raise ValueError('"min_salary" and "max_salary" must be provided')
    elif not isinstance(job["min_salary"], int) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError('"min_salary" and "max_salary" must be intengers')
    elif int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError('"max_salary" must be bigger then "min_salary"')
    elif not isinstance(salary, int):
        raise ValueError('"salary" must a number')
    salary_range = int(job["min_salary"]) <= salary <= int(job["max_salary"])
    return salary_range


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
    jobs_list_with_salary_in_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list_with_salary_in_range.append(job)
        except Exception:
            print("Something is not right")
    return jobs_list_with_salary_in_range
