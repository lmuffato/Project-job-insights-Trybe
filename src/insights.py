from src.jobs import get_unique_values, get_min_or_max, filter_jobs_by


def get_unique_job_types(path):
    return get_unique_values(path, 'job_type')


def filter_by_job_type(jobs, job_type):
    return filter_jobs_by(jobs, 'job_type', job_type)


def get_unique_industries(path):
    return get_unique_values(path, 'industry')


def filter_by_industry(jobs, industry):
    return filter_jobs_by(jobs, 'industry', industry)


def get_max_salary(path):
    return get_min_or_max(path, 'max_salary', max)


def get_min_salary(path):
    return get_min_or_max(path, 'min_salary', min)


def matches_salary_range(job, salary):
    if (('min_salary' or 'max_salary') not in job
        or (type(job['min_salary']) or type(job['max_salary'])) is not int
        or job['min_salary'] > job['max_salary']
            or type(salary) is not int):
        raise ValueError
    return job['min_salary'] <= salary <= job['max_salary']


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
