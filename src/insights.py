from src.jobs import read


def get_unique_job_types(path):
    job_types = set()
    job_list = read(path)

    for job in job_list:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    result = []

    for row in jobs:
        row_type = row["job_type"]
        if row_type == job_type:
            result.append(row)

    return result


def get_unique_industries(path):
    industries = set()
    industry_list = read(path)

    for row in industry_list:
        if row["industry"] != "":
            industries.add(row["industry"])

    return industries


def filter_by_industry(jobs, industry):
    result = []

    for row in jobs:
        row_industry = row["industry"]
        if row_industry == industry:
            result.append(row)

    return result


def get_max_salary(path):
    salary_list = read(path)
    max_salary = 0

    for row in salary_list:
        row_salary = row["max_salary"]
        if row_salary != "" and row_salary != "invalid":
            if int(row_salary) > max_salary:
                max_salary = int(row_salary)

    return max_salary


def get_min_salary(path):
    salary_list = read(path)
    min_salary = -1

    for row in salary_list:
        row_salary = row["min_salary"]
        if row_salary != "" and row_salary != "invalid":
            if min_salary == -1:
                min_salary = int(row_salary)
            if int(row_salary) < min_salary:
                min_salary = int(row_salary)

    return min_salary


def matches_salary_range(job, salary):
    try:
        if 'max_salary' in job and 'min_salary' in job:
            min_salary = job["min_salary"]
            max_salary = job["max_salary"]

            if (
                type(min_salary) != int or type(max_salary) != int
                or min_salary > max_salary
               ):
                raise ValueError("Error")

            return min_salary <= salary <= max_salary
        else:
            raise ValueError("Error")
    except ValueError:
        raise ValueError("Error")


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
