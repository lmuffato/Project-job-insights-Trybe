from src.jobs import read


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
    list_jobs = set()
    reader_datas = read(path)
    for row in reader_datas:
        list_jobs.add(row["job_type"])
    return list_jobs


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
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


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
    list_industry = set()
    reader_datas = read(path)
    for row in reader_datas:
        if row["industry"]:
            list_industry.add(row["industry"])
    return list_industry


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
    industry_list = []
    for row in jobs:
        if row["industry"] == industry:
            industry_list.append(row)
    return industry_list


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
    reader_datas = read(path)
    max_value = set()
    for row in reader_datas:
        if row["max_salary"] != '' and row["max_salary"].isnumeric():
            max_value.add(int(row["max_salary"]))
    return max(max_value)


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
    reader_datas = read(path)
    min_value = set()
    for row in reader_datas:
        if row["min_salary"] != '' and row["min_salary"].isnumeric():
            min_value.add(int(row["min_salary"]))
    return min(min_value)


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
    if (type(salary) is not int
       or "max_salary" not in job
       or "min_salary" not in job
       or type(job["min_salary"]) is not int
       or type(job["max_salary"]) is not int
       or job["min_salary"] > job["max_salary"]):
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


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
