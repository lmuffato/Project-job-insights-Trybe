from src import jobs


def get_unique_job_types(path):
    data = jobs.read(path)
    jobs_types = set()
    for row in data:
        jobs_types.add(row["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    data = jobs.read(path)
    industries = set()
    for row in data:
        if row["industry"] != "":
            industries.add(row["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs


def get_max_salary(path):
    data = jobs.read(path)
    salaries = []
    for row in data:
        if row["max_salary"].isnumeric():
            salaries.append(int(row["max_salary"]))
    return max(salaries)


def get_min_salary(path):
    data = jobs.read(path)
    salaries = []
    for row in data:
        if row["min_salary"].isnumeric():
            salaries.append(int(row["min_salary"]))
    return min(salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    if type(salary) != int:
        raise ValueError
    else:
        return salary >= job["min_salary"] and salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            print('ValueError')
    return result
