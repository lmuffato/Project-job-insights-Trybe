from src.jobs import read
import sys


def is_not_empty(*values):
    is_valid_values = True
    for value in values:
        if(value == ''):
            is_valid_values = False
            break
    return is_valid_values


def is_int(*values):
    is_valid_values = True
    for value in values:
        if(type(value) != int):
            is_valid_values = False
            break
    return is_valid_values


def is_not_alpha(value):
    return not value.isalpha()


def get_unique_job_types(path):
    jobs_data = read(path)
    unique_job_types = set()

    for job in jobs_data:
        if is_not_empty(job["job_type"]):
            unique_job_types.add(job["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    list_of_jobs = []
    for job in jobs:
        if(job['job_type'] == job_type):
            list_of_jobs.append(job)

    return list_of_jobs


def get_unique_industries(path):
    jobs_data = read(path)
    unique_industries = set()
    for job in jobs_data:
        if is_not_empty(job["industry"]):
            unique_industries.add(job["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    list_of_industries = []
    for job in jobs:
        if(job['industry'] == industry):
            list_of_industries.append(job)

    return list_of_industries


def get_max_salary(path):
    jobs_data = read(path)
    max_salary = 0

    for job in jobs_data:
        if(is_not_empty(job['max_salary']) and
           is_not_alpha(job['max_salary'])):
            salary = int(job['max_salary'])
            if(salary > max_salary):
                max_salary = salary

    return max_salary


def get_min_salary(path):
    jobs_data = read(path)
    # Source:
    # https://stackoverflow.com/questions/7604966/
    # maximum-and-minimum-values-for-ints
    min_salary = sys.maxsize

    for job in jobs_data:
        if(is_not_empty(job['min_salary']) and
           is_not_alpha(job['min_salary'])):
            salary = int(job['min_salary'])
            if(salary < min_salary):
                min_salary = salary

    return min_salary


def matches_salary_range(job, salary):
    if('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('not exist')

    max_salary = job['max_salary']
    min_salary = job['min_salary']

    if(not is_int(max_salary, min_salary, salary)):
        raise ValueError('Some value is not int')
    elif(min_salary > max_salary):
        raise ValueError('min_salary greater than max_salary')
    else:
        return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    list_of_jobs = []

    for job in jobs:
        if('min_salary' not in job or 'max_salary' not in job):
            continue

        min_salary = job['min_salary']
        max_salary = job['max_salary']

        if(is_not_empty(min_salary, max_salary, salary) and
           is_int(min_salary, max_salary, salary)):
            if(min_salary <= salary <= max_salary):
                list_of_jobs.append(job)

    return list_of_jobs
