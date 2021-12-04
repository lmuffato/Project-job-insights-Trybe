from src.jobs import read


def get_unique_job_types(path):
    jobs_dict = read(path)
    all_jobs = set(jobs["job_type"] for jobs in jobs_dict)

    return all_jobs


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_dict = read(path)
    all_jobs = set()
    for jobs in jobs_dict:
        if jobs["industry"]:
            all_jobs.add(jobs["industry"])
    return all_jobs


def filter_by_industry(jobs, industry):
    jobs_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_list.append(job)

    return jobs_list


def get_max_salary(path):
    jobs_dict = read(path)
    max_salary = 0
    for jobs in jobs_dict:
        if jobs["max_salary"] and jobs["max_salary"] != 'invalid':
            salary = int(jobs["max_salary"])
            if salary > max_salary:
                max_salary = salary

    return max_salary


def get_min_salary(path):
    jobs_dict = read(path)
    min_salary = get_max_salary(path)
    for jobs in jobs_dict:
        if jobs["min_salary"] and jobs["min_salary"] != 'invalid':
            salary = int(jobs["min_salary"])
            if salary < min_salary:
                min_salary = salary

    return min_salary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job or
        "max_salary" not in job or
        type(job["max_salary"]) is not int or
        type(job["min_salary"]) is not int or
        not isinstance(job["max_salary"], int) or  # outra forma
        not isinstance(job["min_salary"], int) or
        job["min_salary"] > job["max_salary"] or
        not isinstance(salary, int)
    ):
        raise ValueError

    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    ranged_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                ranged_jobs.append(job)
        except ValueError:
            ranged_jobs = ranged_jobs

    return ranged_jobs
