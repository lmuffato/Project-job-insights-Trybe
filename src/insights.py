from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return list(set([job['job_type'] for job in jobs]))


def filter_by_job_type(jobs, job_type):
    filtered = filter(lambda job: job['job_type'] == job_type, jobs)
    return list(filtered)


def get_unique_industries(path):
    jobs = read(path)

    industries = list(
        set([unique_industry["industry"]
             for unique_industry in jobs
             if unique_industry["industry"] != ""])
    )

    return industries


def filter_by_industry(jobs, industry):
    filtered = filter(lambda job: job['industry'] == industry, jobs)
    return list(filtered)


def get_max_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                int(unique_salary["max_salary"])
                for unique_salary in jobs
                if unique_salary["max_salary"] != ""
                and unique_salary["max_salary"].isdigit()
            ]
        )
    )

    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                int(unique_salary["min_salary"])
                for unique_salary in jobs
                if unique_salary["min_salary"] != ""
                and unique_salary["min_salary"].isdigit()
            ]
        )
    )

    return min(salaries)


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
