from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return list(set([job["job_type"] for job in jobs]))


def filter_by_job_type(jobs, job_type):
    jobs_filtered = [
        job_filtered
        for job_filtered in jobs
        if job_filtered["job_type"] == job_type
    ]
    return jobs_filtered


def get_unique_industries(path):
    jobs = read(path)

    # jobs_filtered = list(set([
    #     unique_industry['industry'] for unique_industry
    #     in jobs if unique_industry['industry'] != ''
    #     ]))

    jobs_filtered = list(
        set([unique_industry["industry"] for unique_industry in jobs])
    )
    return list(filter(None, jobs_filtered))


def filter_by_industry(jobs, industry):
    industry_filtered = [
        job_filtered
        for job_filtered in jobs
        if job_filtered["industry"] == industry
    ]
    return industry_filtered


def get_max_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                unique_salary["max_salary"]
                for unique_salary in jobs
                if unique_salary["max_salary"] != ""
            ]
        )
    )

    max_salaries = 0
    for salary in salaries:
        if salary.isdigit():
            if int(salary) > max_salaries:
                max_salaries = int(salary)
    return max_salaries


def get_min_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                unique_salary["min_salary"]
                for unique_salary in jobs
                if unique_salary["min_salary"] != ""
            ]
        )
    )

    min_salary = int(salaries[0])
    for salary in salaries:
        if salary.isdigit():
            if int(salary) < min_salary:
                min_salary = int(salary)
    return min_salary


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError("salary isn't a valid integer")
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError(
            'job["min_salary"] or job["max_salary"] doesn\'t exists'
        )
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError(
            'job["min_salary"] or job["max_salary"] aren\'t valid integers'
        )
    if job["min_salary"] > job["max_salary"]:
        raise ValueError(
            'job["min_salary"]` is greather than `job["max_salary"]'
        )

    return job["min_salary"] <= int(salary) <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            print(ValueError)
    return list_jobs
