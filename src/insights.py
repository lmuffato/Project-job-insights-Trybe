from src.jobs import read


def get_unique_job_types(path):
    return set(job['job_type'] for job in read(path) if job['job_type'])


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    return set(job['industry'] for job in read(path) if job['industry'])


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    return max(
        [int(job['max_salary']) for job in read(path)
            if job['max_salary'].isnumeric()])


def get_min_salary(path):
    return min(
        [int(job['min_salary']) for job in read(path)
            if job['min_salary'].isnumeric()])


def matches_salary_range(job, salary):
    if ('min_salary' not in job
            or 'max_salary' not in job
            or not type(job['min_salary']) == int
            or not type(job['max_salary']) == int
            or job['min_salary'] > job['max_salary']
            or not type(salary) == int):
        raise ValueError

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filtered_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salaries.append(job)
        except ValueError:
            pass
    return filtered_salaries
