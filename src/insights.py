from .jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    job_types = set()

    for job in jobs_list:
        job_types.add(job['job_type'])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    industries = set()

    for job in jobs_list:
        if job['industry'] != '':
            industries.add(job['industry'])
    return list(industries)


def filter_by_industry(jobs, industry):
    filtered_jobs = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0

    for job in jobs_list:
        if job['max_salary'] != '' and job['max_salary'] != 'invalid':
            if int(job['max_salary']) > max_salary:
                max_salary = int(job['max_salary'])

    return int(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = get_max_salary(path)

    for job in jobs_list:
        if job['min_salary'] != '' and job['min_salary'] != 'invalid':
            if int(job['min_salary']) < min_salary:
                min_salary = int(job['min_salary'])

    return int(min_salary)


def matches_salary_range(job, salary):
    if 'max_salary' not in job or 'min_salary' not in job:
        raise ValueError('Value Error')

    if type(job['max_salary']) != int or type(job['min_salary']) != int:
        raise ValueError('Value Error')

    if job['min_salary'] > job['max_salary']:
        raise ValueError('Value Error')

    if type(salary) != int:
        raise ValueError('Value Error')

    return job['max_salary'] >= salary and salary >= job['min_salary']


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            isJobValid = matches_salary_range(job, salary)
        except ValueError:
            continue
        else:
            if isJobValid:
                filtered_jobs.append(job)
    return filtered_jobs
