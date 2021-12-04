from src.jobs import read


def get_unique_job_types(path):
    jobs_read = read(path)
    my_set = set()
    for row in jobs_read:
        if row["job_type"] != "":
            my_set.add(row["job_type"])
    return my_set


def filter_by_job_type(jobs, job_type):
    filtered = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered.append(job)

    return filtered


def get_unique_industries(path):
    jobs_read = read(path)
    my_set = set()
    for row in jobs_read:
        if row["industry"] != "":
            my_set.add(row["industry"])
    return my_set


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job['industry'] == industry:
            filtered.append(job)

    return filtered


def get_max_salary(path):
    jobs_read = read(path)
    my_salary = []
    for row in jobs_read:
        if row["max_salary"].isnumeric():
            my_salary.append(int(row["max_salary"]))
            max_sal = max(my_salary)
    return max_sal


def get_min_salary(path):
    jobs_read = read(path)
    my_salary = []
    for row in jobs_read:
        if row["min_salary"].isnumeric():
            my_salary.append(int(row["min_salary"]))
            min_sal = min(my_salary)
    return min_sal


def matches_salary_range(job, salary):
    if ("min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
            or type(salary) is not int):
        raise ValueError("Value Error: Invalid")
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs
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
    pass
