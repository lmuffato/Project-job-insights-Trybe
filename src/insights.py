from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    categories = set()
    for job in data:
        if job["job_type"] != "":
            categories.add(job["job_type"])
    return categories


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for industry in data:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return industries


def filter_by_industry(jobs, industry):
    list = []
    for job in jobs:
        if job["industry"] == industry:
            list.append(job)
    return list


def get_max_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["max_salary"] != "":
            try:
                salaries.add(int(salary["max_salary"]))
            except ValueError:
                print("Error")
    return max(salaries)


def get_min_salary(path):
    data = read(path)
    salaries = set()
    for salary in data:
        if salary["min_salary"] != "":
            try:
                salaries.add(int(salary["min_salary"]))
            except ValueError:
                print("Error")
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        type(salary) != int
        or "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Value Error")
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    arrJobs = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                arrJobs.append(job)
        except ValueError:
            pass
    return arrJobs
