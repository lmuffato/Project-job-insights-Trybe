from src.jobs import read
# from jobs import read
path = 'jobs.csv'


def get_unique_job_types(path):
    jobs_list = read(path)

    jobs_types = set()

    for job in jobs_list:
        jobs_types.add(job['job_type'])

    return jobs_types


def filter_by_job_type(jobs, job_type):
    list_jobs_type = [
      job for job in jobs
      if job_type == job['job_type']
    ]

    return list_jobs_type


def get_unique_industries(path):
    jobs_list = read(path)

    unique_industries = set()

    for job in jobs_list:
        if job['industry'] != '':
            unique_industries.add(job['industry'])

    return unique_industries


def filter_by_industry(jobs, industry):
    list_jobs_industry = [
      job for job in jobs
      if industry == job['industry']
    ]

    return list_jobs_industry


def get_max_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        try:
            salaries.add(int(job['max_salary']))
        except ValueError:
            pass

    return max(salaries)


def get_min_salary(path):
    jobs_list = read(path)
    salaries = set()

    for job in jobs_list:
        try:
            salaries.add(int(job['min_salary']))
        except ValueError:
            pass

    return min(salaries)


def validate_matches_salary_range(min_salary, max_salary, salary):
    if min_salary == '' or max_salary == '':
        return False
    elif not isinstance(min_salary, int) or not isinstance(max_salary, int):
        return False
    elif int(min_salary) > int(max_salary):
        return False
    elif not isinstance(salary, int):
        return False
    return True


def matches_salary_range(job, salary):
    min_salary = job['min_salary'] if 'min_salary' in job else ''
    max_salary = job['max_salary'] if 'max_salary' in job else ''
    result = validate_matches_salary_range(min_salary, max_salary, salary)

    if result is False:
        raise ValueError()

    if int(min_salary) <= salary <= int(max_salary):
        return True
    return False


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
