from src.jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    unique_jobs_types = set(job["job_type"] for job in list_jobs)
    print(unique_jobs_types)
    return unique_jobs_types


def filter_by_job_type(jobs, job_type):
    list_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_jobs.append(job)
    return list_jobs


def get_unique_industries(path):

    list_jobs = read(path)
    unique_industries = set(
        job["industry"] for job in list_jobs if job["industry"]
    )
    print(unique_industries)
    return unique_industries


def filter_by_industry(jobs, industry):
    list_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            list_jobs.append(job)
    return list_jobs


def get_max_salary(path):
    list_jobs = read(path)
    list_salaries = []
    for job in list_jobs:
        if job["max_salary"].isdigit():
            list_salaries.append(int(job["max_salary"]))
    return max(list_salaries)


def get_min_salary(path):
    list_jobs = read(path)
    list_salaries = []
    for job in list_jobs:
        if job["min_salary"].isdigit():
            list_salaries.append(int(job["min_salary"]))
    return min(list_salaries)


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
            pass
    return result
