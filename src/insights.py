from .jobs import read


def get_unique_job_types(path):
    job_list = read(path)
    unique_jobs = set(job["job_type"] for job in job_list)

    return unique_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]

    return filtered_jobs


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
    job_list = read(path)
    unique_industries = set(
        job["industry"] for job in job_list if job["industry"] != ""
    )
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industries = [job for job in jobs if job["industry"] == industry]

    return filtered_industries


def get_max_salary(path):
    job_list = read(path)
    max_salaries = set(
        int(job["max_salary"])
        for job in job_list
        if job["max_salary"].isnumeric()
    )
    return max(max_salaries)


def get_min_salary(path):
    job_list = read(path)
    max_salaries = set(
        int(job["min_salary"])
        for job in job_list
        if job["min_salary"].isnumeric()
    )
    return min(max_salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(salary) is not int
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["max_salary"] < job["min_salary"]
    ):
        raise ValueError("Valores inválidos")
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


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
