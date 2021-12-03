from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_types = set()

    try:
        for job in jobs_list:
            jobs_types.add(job["job_type"])
    except NameError:
        print("Variable 'jobs_list' is not defined")

    return jobs_types


def filter_by_job_type(jobs, job_type):
    job_list = []

    try:
        for job in jobs:
            if job["job_type"] == job_type:
                job_list.append(job)
    except ValueError:
        print("Params is not defined")

    return job_list


def get_unique_industries(path):
    jobs_list = read(path)
    industries_list = set()

    try:
        for job in jobs_list:
            industries_list.add(job["industry"])
    except NameError:
        print("Variable 'jobs_list' is not defined")

    industries_list.discard("")

    return industries_list


def filter_by_industry(jobs, industry):
    industry_list = []

    try:
        for job in jobs:
            if job["industry"] == industry:
                industry_list.append(job)
    except ValueError:
        print("Params is not defined")

    return industry_list


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = set()

    for job in jobs_list:
        try:
            max_salary.add(int(job["max_salary"]))
        except ValueError:
            pass
    """
    Quando a 'pass' instrução é executada,
    nada acontece,
    mas você evita receber um erro quando o código vazio não é permitido.
    """

    return max(max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary = set()

    for job in jobs_list:
        try:
            min_salary.add(int(job["min_salary"]))
        except ValueError:
            pass
    """
    Quando a 'pass' instrução é executada,
    nada acontece,
    mas você evita receber um erro quando o código vazio não é permitido.
    """

    return min(min_salary)


def matches_salary_range(job, salary):
    """
    ValueError
    Se `job [" min_salary "]`
      ou
    `job [" max_salary "]` não existir
    Se `job [" min_salary "]`
      ou
    `job [" max_salary "]` não são inteiros válidos
    Se `job [" min_salary "]` for maior do que `job [" max_salary "]`
    Se `salário` não for um número inteiro válido
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif type(salary) != int:
        raise ValueError
    else:
        return salary >= job["min_salary"] and salary <= job["max_salary"]


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
