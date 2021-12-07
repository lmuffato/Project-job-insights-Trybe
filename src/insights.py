from .jobs import read


def get_unique_job_types(path):

    list_data = read(path)

    job_types = set()
    for row in list_data:
        for job in row["job_type"].split(","):
            job_types.add(job)

    return job_types


def filter_by_job_type(jobs, job_type):

    filtered_jobs = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):

    list_data = read(path)

    industries = set()

    for job in list_data:
        if job["industry"] != "":
            industries.add(job["industry"])

    return industries


def filter_by_industry(jobs, industry):

    filtered_industries = []

    for industry_ in jobs:
        if industry_["industry"] == industry:
            filtered_industries.append(industry_)

    return filtered_industries


def get_max_salary(path):

    list_data = read(path)

    bigger_salary = 0

    for job in list_data:
        if (
            job["max_salary"] != ""
            and job["max_salary"] != "invalid"
            and int(job["max_salary"]) > bigger_salary
        ):
            bigger_salary = int(job["max_salary"])

    return bigger_salary


def get_min_salary(path):

    # Refatorado com ajudado colega André Barroso

    list_data = read(path)

    lower_salary = list(
        set(
            int(job["min_salary"])
            for job in list_data
            if job["min_salary"] != "" and job["min_salary"] != "invalid"
        )
    )

    return min(lower_salary)


def matches_salary_range(job, salary):

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
        or type(salary) is not int
    ):
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
