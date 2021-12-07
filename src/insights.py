from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    jobs_quantity = set()
    for row in list:
        if row["job_type"] != "":
            jobs_quantity.add(row["job_type"])

    return jobs_quantity


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    list = read(path)
    industries_quantity = set()
    for row in list:
        if row["industry"] != "":
            industries_quantity.add(row["industry"])

    return industries_quantity


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):
    list = read(path)
    max_sal = set()
    for row in list:
        if row["max_salary"] != "":
            try:
                max_sal.add(int(row["max_salary"]))
            except ValueError:
                print("Error message")
    return max(max_sal)


def get_min_salary(path):
    list = read(path)
    min_sal = set()
    for row in list:
        if row["min_salary"] != "":
            try:
                min_sal.add(int(row["min_salary"]))
            except ValueError:
                print("Error message")
    return min(min_sal)


def matches_salary_range(job, salary):
    if ("min_salary" not in job
        or "max_salary" not in job
        or type(salary) is not int
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("Invalid data")
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
