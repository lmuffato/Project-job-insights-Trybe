from src.jobs import read


def get_unique_job_types(path):
    readFile = read(path)
    result = []
    for info in readFile:
        if info["job_type"] is None or info["job_type"] in result:
            continue
        else:
            result.append(info["job_type"])
    return result


def filter_by_job_type(jobs, job_type):
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result


def get_unique_industries(path):
    readFile = read(path)
    result = []
    for info in readFile:
        if not info["industry"].rstrip() or info["industry"] in result:
            continue
        else:
            result.append(info["industry"])
    return result


def filter_by_industry(jobs, industry):
    result = []
    for job in jobs:
        if job["industry"] == industry:
            result.append(job)
    return result


def get_max_salary(path):
    readFile = read(path)
    result = 0
    max_salary = "max_salary"
    for info in readFile:
        if (not info[max_salary].rstrip()) or info[max_salary] == 'invalid':
            continue
        elif int(info[max_salary]) < int(result):
            continue
        else:
            result = int(info[max_salary])
    return result


def get_min_salary(path):
    readFile = read(path)
    result = 1000000
    min_salary = "min_salary"
    for info in readFile:
        if (not info[min_salary].rstrip()) or info[min_salary] == 'invalid':
            continue
        elif int(info[min_salary]) > int(result):
            continue
        else:
            result = int(info[min_salary])
    return result

# lançamento de erro visto no repositório do Diego-F-Affonso
# https://github.com/tryber/sd-09-project-job-insights/pull/96


def matches_salary_range(job, salary):
    all_salaries = "job['min_salary'] or job['max_salary']"
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('Error')
    if not all_salaries.rstrip():
        raise ValueError('Error')
    if not (
        type(job["min_salary"]) == int
        or type(job["max_salary"]) == int
        or type(salary) == int
    ):
        raise ValueError('Error')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('Error')
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
