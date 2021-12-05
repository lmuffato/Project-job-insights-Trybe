from src.jobs import read


def get_unique_job_types(path):
    file = read(path)
    job_types = set()
    for jobe in file:
        job_types.add(jobe['job_type'])
    return job_types


def filter_by_job_type(jobs, job_type):
    filter_job = [job for job in jobs if job['job_type'] == job_type]
    return filter_job


def get_unique_industries(path):
    file = read(path)
    industries = set(job["industry"] for job in file if job["industry"])
    return industries


def filter_by_industry(jobs, industry):
    filer_industry = [
        industria for industria in jobs if industria['industry'] == industry
    ]
    return filer_industry


def get_max_salary(path):
    file = read(path)
    max_salary = [
        int(job["max_salary"]) for job in file if job["max_salary"].isdigit()
    ]
    return max(max_salary)


def get_min_salary(path):
    file = read(path)
    min_salary = [
        int(job["min_salary"]) for job in file if job["min_salary"].isdigit()
    ]
    return min(min_salary)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError()

    min_salary = job["min_salary"]
    max_salary = job["max_salary"]

    if (
        type(max_salary) != int
        or type(min_salary) != int
        or min_salary > max_salary
        or type(salary) != int
    ):
        raise ValueError()

    else:
        return salary in range(min_salary, max_salary)


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
