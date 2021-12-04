from src.jobs import read

# from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_jobs_types = set(job["job_type"] for job in jobs_list)
    print(unique_jobs_types)
    return unique_jobs_types


def filter_by_job_type(jobs, job_type):
    list_of_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_of_jobs.append(job)
    return list_of_jobs


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = set(
        job["industry"] for job in jobs_list if job["industry"]
    )
    return unique_industries


def filter_by_industry(jobs, industry):
    industries_list = []
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    jobs_list = read(path)
    salary_list = []
    for job in jobs_list:
        if job["max_salary"].isdigit():
            salary_list.append(int(job["max_salary"]))
    return max(salary_list)


def get_min_salary(path):
    jobs_list = read(path)
    salary_min_list = []
    for job in jobs_list:
        if job["min_salary"].isdigit():
            salary_min_list.append(int(job["min_salary"]))
    return min(salary_min_list)


def matches_salary_range(job, salary):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("doesn't exists")
    max = job["max_salary"]
    min = job["min_salary"]
    if (type(min) != int) or (type(max) != int):
        raise ValueError("not int")
    if job["max_salary"] < job["min_salary"]:
        raise ValueError("salaries values aren't corrects")
    if (type(salary) != int):
        raise ValueError("salary has a incorrect value")
    else:
        return min <= salary <= max


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
