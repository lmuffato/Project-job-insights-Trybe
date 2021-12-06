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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
