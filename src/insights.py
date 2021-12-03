from src.jobs import read


# python sets: https://www.w3schools.com/python/python_sets.asp
# set methods: https://www.w3schools.com/python/python_sets_methods.asp
def get_unique_job_types(path):
    job_list = read(path)
    job_type_set = set()
    for job in job_list:
        job_type_set.add(job["job_type"])
    return job_type_set


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if (job["job_type"] == job_type):
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    job_list = read(path)
    industries_set = set()
    for job in job_list:
        if (job["industry"] != ''):
            industries_set.add(job["industry"])
    return industries_set


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if (job["industry"] == industry):
            job_list.append(job)
    return job_list


# Python Math Functions: https://www.w3schools.com/python/python_math.asp
# Python String IsNumeric():
# https://www.w3schools.com/python/ref_string_isnumeric.asp
def get_max_salary(path):
    job_list = read(path)
    salary_array = []
    for job in job_list:
        if(job["max_salary"].isnumeric()):
            salary_array.append(int(job["max_salary"]))
    return max(salary_array)


def get_min_salary(path):
    job_list = read(path)
    salary_array = []
    for job in job_list:
        if(job["min_salary"].isnumeric()):
            salary_array.append(int(job["min_salary"]))
    return min(salary_array)


def check_errors(job, salary):
    if (type(salary) != int or
        "min_salary" not in job or
        "max_salary" not in job or
        type(job["min_salary"]) is not int or
        type(job["max_salary"]) is not int or
            job["min_salary"] > job["max_salary"]):
        raise ValueError("Value Error")


def matches_salary_range(job, salary):
    check_errors(job, salary)
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    job_list = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                job_list.append(job)
        except ValueError:
            pass
    return job_list
