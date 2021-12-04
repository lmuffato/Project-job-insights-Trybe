from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    job_types = set()
    for job in file:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    matching_jobs = [job for job in jobs if job["job_type"] == job_type]
    return matching_jobs


def get_unique_industries(path):
    file = read(path)
    unique_industries = set(job["industry"] for job in file if job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    matching_industries = [job for job in jobs if job["industry"] == industry]
    return matching_industries


def get_max_salary(path):
    file = read(path)
    max_salary = [
        int(job["max_salary"]) for job in file if job["max_salary"].isdigit()
    ]
    return max(max_salary)


def get_min_salary(path):
    file = read(path)
    min_salary = [
        int(job["min_salary"]) for job in file if job["min_salary"].isdigit()
    ]
    return min(min_salary)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (
        type(max_salary) != int
        or type(min_salary) != int
        or min_salary > max_salary
        or type(salary) != int
    ):
        raise ValueError()

    else:
        return salary in range(min_salary, max_salary)


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
