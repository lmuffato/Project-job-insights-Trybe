from src.jobs import read


def get_unique_job_types(path):
    readFile = read(path)
    job_types = set()
    for job in readFile:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    filter_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            filter_list.append(job)
    return filter_list


def get_unique_industries(path):
    readFile = read(path)
    industry = set()
    for row in readFile:
        if row['industry'] != '':
            industry.add(row['industry'])
    return industry


def filter_by_industry(jobs, industry):
    filter_list = []
    for job in jobs:
        if job['industry'] == industry:
            filter_list.append(job)
    return filter_list


def get_max_salary(path):
    readFile = read(path)
    max_salary = []
    for row in readFile:
        salary_row = row['max_salary']
        if salary_row != '' and salary_row != "invalid":
            max_salary.append(int(salary_row))
    return max(max_salary)


def get_min_salary(path):
    readFile = read(path)
    min_salary = []
    for row in readFile:
        salary_row = row['min_salary']
        if salary_row != '' and salary_row != "invalid":
            min_salary.append(int(salary_row))
    return min(min_salary)


def matches_salary_range(job, salary):
    if type(salary) is not int:
        raise ValueError("salary must be an integer")
    if not ('min_salary' in job and 'max_salary' in job):
        raise ValueError("job must have min_salary and max_salary")
    if (
        type(job['min_salary']) is not int or
        type(job['max_salary']) is not int
    ):
        raise ValueError("min_salary and max_salary must be integers")
    if job['min_salary'] > job['max_salary']:
        raise ValueError("min_salary must be less than max_salary")
    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filter_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_list.append(job)
        except ValueError:
            print("Invalid salary range")
    return filter_list
