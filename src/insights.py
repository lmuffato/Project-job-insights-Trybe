from src.jobs import read


def get_unique_job_types(path):
    list = read(path)
    dic_types = set(job["job_type"] for job in list)
    return dic_types


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if (job["job_type"] == job_type):
            list.append(job)
    return list


def get_unique_industries(path):
    list = read(path)
    dic_types = set(job["industry"] for job in list if job["industry"] != '')
    return dic_types


def filter_by_industry(jobs, industry):
    list = []
    for job in jobs:
        if (job["industry"] == industry):
            list.append(job)
    return list


def get_max_salary(path):
    list = read(path)
    salary_list = []
    for job in list:
        if (job["max_salary"].isnumeric()):
            salary_list.append(int(job["max_salary"]))

    return max(salary_list)


def get_min_salary(path):
    list = read(path)
    salary_list = []
    for job in list:
        if (job["min_salary"].isnumeric()):
            salary_list.append(int(job["min_salary"]))

    return min(salary_list)


def matches_salary_range(job, salary):
    if (type(salary) != int
            or "min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) is not int
            or type(job["max_salary"]) is not int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("Value Error")
    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    arrJobs = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                arrJobs.append(job)
        except ValueError:
            pass
    return arrJobs
