from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    job_list = read(path)
    for job in job_list:
        job_types.add(job["job_type"])

    return job_types


def filter_by_job_type(jobs, job_type):
    job_in_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_in_job_type.append(job)

    return job_in_job_type


def get_unique_industries(path):
    industry_types = set()
    job_list = read(path)
    for job in job_list:
        if job["industry"] != '' and job["industry"] != 'invalid':
            industry_types.add(job["industry"])

    return industry_types


def filter_by_industry(jobs, industry):
    jobs_in_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_in_industry.append(job)

    return jobs_in_industry


def get_max_salary(path):
    job_list = read(path)
    max_salary = 0
    for job in job_list:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            if int(job["max_salary"]) > max_salary:
                max_salary = int(job["max_salary"])

    return max_salary


def get_min_salary(path):
    job_list = read(path)
    min_salary = 100000000000
    for job in job_list:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            if int(job["min_salary"]) < min_salary:
                min_salary = int(job["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    try:
        if (type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]
                or type(salary) != int):
            raise ValueError
    except KeyError:
        raise ValueError

    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return bool(1)
    return bool(0)


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
