from src.jobs import read


def get_unique_job_types(path):
    contentList = read(path)
    returnList = []
    for row in contentList:
        jobType = row['job_type']
        if jobType != '' and jobType not in returnList:
            returnList.append(jobType)
    return returnList


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
    contentList = read(path)
    returnList = []
    for row in contentList:
        jobType = row['industry']
        if jobType != '' and jobType not in returnList:
            returnList.append(jobType)
    return returnList
    return []


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
    previusList = []
    for row in file:
        if row['max_salary'] != '' and row['max_salary'] != 'invalid':
            previusList.append(int(row['max_salary']))
    return max(previusList)


def get_min_salary(path):
    file = read(path)
    previusList = []
    for row in file:
        if row['min_salary'] != '' and row['min_salary'] != 'invalid':
            previusList.append(int(row['min_salary']))
    return min(previusList)


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
