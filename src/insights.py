from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    category = set()
    for index in data:
        if index["job_type"] != "":
            category.add(index["job_type"])
    return category


def get_unique_industries(path):
    data = read(path)
    industry = set()
    for index in data:
        if index["industry"] != "":
            industry.add(index["industry"])
    return industry


def get_max_salary(path):
    data = read(path)
    salary = set()
    for index in data:
        if index["max_salary"] != "":
            try:
                salary.add(int(index["max_salary"]))
            except ValueError:
                print("deu ruim")
    return max(salary)


def get_min_salary(path):
    data = read(path)
    salary = set()
    for index in data:
        if index["min_salary"] != "":
            try:
                salary.add(int(index["min_salary"]))
            except ValueError:
                print("deu ruim")
    return min(salary)


def filter_by_job_type(jobs, job_type):
    filter_job = []
    for index in jobs:
        if index["job_type"] == job_type:
            filter_job.append(index)
    return filter_job


def filter_by_industry(jobs, industry):
    filter_industry = []
    for index in jobs:
        if index["industry"] == industry:
            filter_industry.append(index)
    return filter_industry


def matches_salary_range(job, salary):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("err")
    if (type(job["max_salary"]) != int or type(job["min_salary"]) != int):
        raise ValueError("err")
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("err")
    if (type(salary) != int):
        raise ValueError("err")

    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):

    return []
