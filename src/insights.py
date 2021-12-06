from src.jobs import read


def get_unique_job_types(path):
    read_jobs = read(path)
    job_types_set = set()

    for jobs_dict in read_jobs:
        if jobs_dict["job_type"] != "":
            job_types_set.add(jobs_dict["job_type"])

    # print(job_types_set)
    return job_types_set


# Set items are unordered, unchangeable, and do not allow duplicate values.
# https://www.w3schools.com/python/python_sets.asp


def filter_by_job_type(jobs, job_type):
    filtered_job_types_list = []

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_job_types_list.append(job)

    return filtered_job_types_list


def get_unique_industries(path):
    read_jobs = read(path)
    industries_set = set()

    for jobs_dict in read_jobs:
        if jobs_dict["industry"] != "":
            industries_set.add(jobs_dict["industry"])

    # print(industries_set)
    return industries_set


def filter_by_industry(jobs, industry):
    filtered_industries_list = []

    for job in jobs:
        if job["industry"] == industry:
            filtered_industries_list.append(job)

    return filtered_industries_list


def get_max_salary(path):
    read_jobs = read(path)
    max_salary_set = set()

    for jobs_dict in read_jobs:
        if jobs_dict["max_salary"].isnumeric():
            max_salary_set.add(int(jobs_dict["max_salary"]))
            highest_salary = max(max_salary_set)

    # print(highest_salary)
    return highest_salary
    # pass

    # The isnumeric() method returns True if all characters in a string are
    # numeric characters. If not, it returns False
    # https://www.programiz.com/python-programming/methods/string/isnumeric


def get_min_salary(path):
    read_jobs = read(path)
    min_salary_list = []

    for jobs_dict in read_jobs:
        if jobs_dict["min_salary"].isnumeric():
            min_salary_list.append(int(jobs_dict["min_salary"]))
            lowest_salary = min(min_salary_list)

    return lowest_salary


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Value Error")

    return (
        job["min_salary"] <= salary <= job["max_salary"]
    )  # retora TRUE or FALSE


# https://www.w3schools.com/python/ref_keyword_raise.asp
# The raise keyword is used to raise an exception.
# You can define what kind of error to raise, and the text to print to the user


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
