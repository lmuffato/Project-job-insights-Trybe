from src.jobs import read


def get_unique_job_types(path):
    job_types = read(path)

    return list(set(job_type["job_type"] for job_type in job_types))

# a = get_unique_job_types("src/jobs.csv")
# print(a)


def filter_by_job_type(jobs, job_type):

    jobs_filtred = [job_filtred for job_filtred
                    in jobs if job_filtred["job_type"] == job_type]
    return jobs_filtred


def get_unique_industries(path):
    industries = read(path)
    result = list(set(
        unique_industry["industry"] for unique_industry in industries))

    return list(filter(None, result))


# a = get_unique_industries("src/jobs.csv")
# print(a)


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

# depois de muitas falhas olhei o PR de Felipe Flores


def get_max_salary(path):
    list = read(path)
    salary = []
    for job in list:
        if (job["max_salary"].isnumeric()):
            salary.append(int(job["max_salary"]))

    return max(salary)


# a = get_max_salary("src/jobs.csv")
# print(type(a))


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

# fontes:
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file
# https://www.w3schools.com/python/ref_func_list.asp
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://stackoverflow.com/questions/16099694/how-to-remove-empty-string-in-a-list/16099706