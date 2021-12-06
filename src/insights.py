import csv


def get_unique_job_types(path):
    with open(path, mode="r") as file:
        file_reader = csv.DictReader(file, delimiter=",")
        return list(set([row["job_type"] for row in file_reader]))


def filter_by_job_type(jobs, job_type):
    total = []
    for line in jobs:
        if line['job_type'] == job_type:
            total.append(line)
    return total


def get_unique_industries(path):
    with open(path, mode="r") as file:
        file_reader = csv.DictReader(file, delimiter=",")
        row = [row["industry"] for row in file_reader]
        return [industry for industry in filter(None, (list(set(row))))]


def filter_by_industry(jobs, industry):
    total = []
    for line in jobs:
        if line['industry'] == industry:
            total.append(line)
    return total


def filter_list(row):
    filter_list_empty = filter(None, (list(set(row))))
    list_salary = [min_salary for min_salary in filter_list_empty]
    filter_salary_not_string = []
    for line in list_salary:
        if line.isdigit():
            filter_salary_not_string.append(line)
    return filter_salary_not_string


def get_max_salary(path):
    with open(path, mode="r") as file:
        file_reader = csv.DictReader(file, delimiter=",")
        row = [row["max_salary"] for row in file_reader]
        list_salary = filter_list(row)
        return int(max(list_salary, key=int))
    pass


def get_min_salary(path):
    with open(path, mode='r') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        row = [row["min_salary"] for row in file_reader]
        list_salary = filter_list(row)
        return int(min(list_salary, key=int))
    pass


def matches_salary_range(job, salary):
    if 'max_salary' not in job.keys() or 'min_salary' not in job.keys():
        raise ValueError("some key does not exist")

    max_salary = type(job['max_salary']) is not int
    min_salary = type(job['max_salary']) is not int

    if min_salary or max_salary:
        raise ValueError("aren't valid integers")
    elif job['min_salary'] > job['max_salary']:
        raise ValueError("is greather than `job['max_salary']")
    elif type(salary) is not int:
        raise ValueError("`salary` isn't a valid integer")
    return job['min_salary'] <= salary <= job['max_salary']


def filter_by_salary_range(jobs, salary):
    match_jobs = []
    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
        except ValueError:
            pass
        else:
            if result:
                match_jobs.append(job)
    return match_jobs
