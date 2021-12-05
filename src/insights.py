from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    unique_jobs = set()
    for x in data:
        if x["job_type"] != "":
            unique_jobs.add(x["job_type"])

    return unique_jobs


def filter_by_job_type(jobs, job_type):
    filter_job = []
    for x in jobs:
        if x["job_type"] == job_type:
            filter_job.append(x)

    return filter_job


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for x in data:
        if x["industry"] != "":
            unique_industries.add(x["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    filter_industry = []
    for x in jobs:
        if x["industry"] == industry:
            filter_industry.append(x)

    return filter_industry


def get_max_salary(path):
    data = read(path)
    salary = set()
    for x in data:
        if x["max_salary"] != "":
            try:
                salary.add(int(x["max_salary"]))
            except ValueError:
                print("Error message")

    return max(salary)


def get_min_salary(path):
    data = read(path)
    salary = set()
    for x in data:
        if x["min_salary"] != "":
            try:
                salary.add(int(x["min_salary"]))
            except ValueError:
                print("Error message")

    return min(salary)


def matches_salary_range(job, salary):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("min salary or max salary not found")
    if (type(job["max_salary"]) != int or type(job["min_salary"]) != int):
        raise ValueError("min salary or max salary it is not a number")
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("Min > Max")
    if (type(salary) != int):
        raise ValueError("Salary it is not a number")

    return (job["min_salary"] <= salary <= job["max_salary"])


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
