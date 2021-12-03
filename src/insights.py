from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = []
    for job in all_jobs:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    all_jobs = read(path)
    industries = []
    for job in all_jobs:
        if job["industry"] not in industries and job["industry"]:
            industries.append(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    all_jobs = read(path)
    max_salaries = []
    for job in all_jobs:
        try:
            max_salaries.append(int(job["max_salary"]))
        except ValueError:
            pass
    return max(max_salaries)


def get_min_salary(path):
    all_jobs = read(path)
    min_salaries = []
    for job in all_jobs:
        try:
            min_salaries.append(int(job["min_salary"]))
        except ValueError:
            pass
    return min(min_salaries)


def matches_salary_range(job, salary):
    if ("max_salary" not in job
            or "min_salary" not in job
            or type(job["max_salary"]) is not int
            or type(job["min_salary"]) is not int
            or job["max_salary"] < job["min_salary"]
            or type(salary) is not int):
        raise ValueError
    if job["max_salary"] >= salary >= job["min_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_list.append(job)
        except ValueError:
            pass
    return jobs_list
