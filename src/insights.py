from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    jobs_list = set()
    for job in jobs:
        jobs_list.add(job["job_type"])
    return jobs_list


def get_unique_industries(path):
    jobs = read(path)
    industries = set(job["industry"] for job in jobs if job["industry"] != '')
    return industries


def get_max_salary(path):
    jobs = read(path)
    salaries = [int(job["max_salary"]) for job in jobs
                if job["max_salary"] != "" and job["max_salary"].isnumeric()]
    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = [int(job["min_salary"]) for job in jobs
                if job["min_salary"] != "" and job["min_salary"].isnumeric()]
    return min(salaries)


def filter_by_job_type(jobs, job_type):
    filter_jobs = [job for job in jobs if job["job_type"] == job_type]
    return filter_jobs


def filter_by_industry(jobs, industry):
    jobs_industry = [job for job in jobs if job["industry"] == industry]
    return jobs_industry


def matches_salary_range(job, salary):
    if (type(salary) != int
            or "min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("Value Error")
    salaries = job["min_salary"] <= salary <= job["max_salary"]
    return salaries


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
