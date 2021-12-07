from src.jobs import read   # Para o avaliador e os teste
# from jobs import read   # Para testar manualmente


def get_unique_job_types(path):
    data = read(path)
    uniques_types_of_jobs = set()
    for job in data:
        if job['job_type'] != '':
            uniques_types_of_jobs.add(job['job_type'])
    return uniques_types_of_jobs


def filter_by_job_type(jobs, job_type):
    filtered_job = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_job.append(job)
    return filtered_job


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for industry in data:
        if industry['industry'] != '':
            unique_industries.add(industry['industry'])
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for indus in jobs:
        if indus['industry'] == industry:
            filtered_industries.append(indus)
    return filtered_industries


def get_max_salary(path):
    data = read(path)
    max_salaries = set()
    for salary in data:
        if salary['max_salary'] != '':
            try:
                max_salaries.add(int(salary['max_salary']))
            except ValueError:
                print('Aconteceu um erro')
    return max(max_salaries)


def get_min_salary(path):
    data = read(path)
    min_salaries = set()
    for salary in data:
        if salary['min_salary'] != '':
            try:
                min_salaries.add(int(salary['min_salary']))
            except ValueError:
                print('Aconteceu um erro')
    return min(min_salaries)


def matches_salary_range(job, salary):
    if (type(salary) != int):
        raise ValueError('salary is not an integer')

    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('min salary or max salary does not exist')

    if (type(job['min_salary']) != int or type(job['max_salary']) != int):
        raise ValueError('min salary or max salary is not an integer')

    if (job["min_salary"] > job["max_salary"]):
        raise ValueError('The min salary cannot be higher than the max salary')

    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    filtred_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtred_jobs.append(job)
        except ValueError:
            print('Aconteceu um erro')
    return filtred_jobs
