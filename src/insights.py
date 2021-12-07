from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = set()
    for job in jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    jobs = read(path)
    industries = set()
    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    industry_filtered_jobs = [
        job for job in jobs if job["industry"] == industry
    ]
    return industry_filtered_jobs


def get_max_salary(path):
    jobs = read(path)
    max_salaries = [
        int(job["max_salary"])
        for job in jobs
        if job["max_salary"].isnumeric() and job["max_salary"] != ""
    ]
    return max(max_salaries)


def get_min_salary(path):
    jobs = read(path)
    min_salaries = [
        int(job["min_salary"])
        for job in jobs
        if job["min_salary"].isnumeric() and job["min_salary"] != ""
    ]
    return min(min_salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            ValueError
    return filtered_jobs
