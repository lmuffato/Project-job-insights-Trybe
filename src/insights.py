from src import jobs


def get_unique_job_types(path):
    file = jobs.read(path)
    job_types = set()

    for row in file:
        if row["job_type"] != "":
            job_types.add(row["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for row in jobs:
        if row["job_type"] == job_type:
            filtered_jobs.append(row)
    return filtered_jobs


def get_unique_industries(path):
    file = jobs.read(path)
    industries_types = set()

    for row in file:
        if row["industry"] != "":
            industries_types.add(row["industry"])
    return industries_types


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for row in jobs:
        if row["industry"] == industry:
            filtered_industry.append(row)
    return filtered_industry


def get_max_salary(path):
    file = jobs.read(path)
    max_salary = 0

    for row in file:
        if row["max_salary"] != "" and row["max_salary"] != "invalid":
            if int(row["max_salary"]) > max_salary:
                max_salary = int(row["max_salary"])
    return max_salary


def get_min_salary(path):
    file = jobs.read(path)
    min_salary = get_max_salary(path)

    for row in file:
        if row["min_salary"] != "" and row["min_salary"] != "invalid":
            if int(row["min_salary"]) < min_salary:
                min_salary = int(row["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Value Error")

    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("Value Error")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("Value Error")

    if type(salary) != int:
        raise ValueError("Value Error")

    return salary >= job["min_salary"] and salary <= job["max_salary"]


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
