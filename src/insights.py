from src.jobs import read


def get_unique_job_types(path):
    contentList = read(path)
    returnList = []
    for row in contentList:
        jobType = row['job_type']
        if jobType != '' and jobType not in returnList:
            returnList.append(jobType)
    return returnList


def filter_by_job_type(jobs, job_type):
    filterd = []
    for job in jobs:
        if job['job_type'] == job_type:
            filterd.append(job)
    return filterd


def get_unique_industries(path):
    contentList = read(path)
    returnList = []
    for row in contentList:
        jobType = row['industry']
        if jobType != '' and jobType not in returnList:
            returnList.append(jobType)
    return returnList


def filter_by_industry(jobs, industry):
    filterd = []
    for job in jobs:
        if job['industry'] == industry:
            filterd.append(job)
    return filterd


def get_max_salary(path):
    file = read(path)
    previusList = []
    for row in file:
        if row['max_salary'] != '' and row['max_salary'] != 'invalid':
            previusList.append(int(row['max_salary']))
    return max(previusList)


def get_min_salary(path):
    file = read(path)
    previusList = []
    for row in file:
        if row['min_salary'] != '' and row['min_salary'] != 'invalid':
            previusList.append(int(row['min_salary']))
    return min(previusList)


def matches_salary_range(job, salary):
    if 'min_salary' not in job.keys() or 'max_salary' not in job.keys():
        raise ValueError
    min = job['min_salary']
    max = job['max_salary']
    firstCondition = type(min) != int or type(max) != int
    if firstCondition or type(salary) != int:
        raise ValueError
    secondCondition = min > max
    if secondCondition:
        raise ValueError
    if salary >= min and salary <= max:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    filtered = []
    for job in jobs:
        try:
            condition = matches_salary_range(job, salary)
            if condition:
                filtered.append(job)
        except ValueError:
            print('esse não pode')
    return filtered
