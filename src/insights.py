from src.jobs import read


def get_unique_job_types(path):

    list = read(path)
    unique_job_types = set(row["job_type"] for row in list)
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    jobs_filtered = []

    for x in jobs:
        if x["job_type"] == job_type:
            jobs_filtered.append(x)
    return jobs_filtered


def get_unique_industries(path):
    list = read(path)

    unique_industries = set(
        row["industry"]
        for row in list
        if row["industry"] != "" and row["industry"] != "invalid"
    )
    return unique_industries


def filter_by_industry(jobs, industry):
    industries_filtered = []

    for x in jobs:
        if x["industry"] == industry:
            industries_filtered.append(x)
    return industries_filtered


def get_max_salary(path):

    data = read(path)

    max_salary = 0
    for x in data:
        if (
            x["max_salary"] != "invalid"
            and x["max_salary"] != ""
            and int(x["max_salary"]) > max_salary
        ):
            max_salary = int(x["max_salary"])
    return max_salary


def get_min_salary(path):

    list = read(path)

    min_salary = 999999
    for x in list:
        if (
            x["min_salary"] != "invalid"
            and x["min_salary"] != ""
            and int(x["min_salary"]) < min_salary
        ):
            min_salary = int(x["min_salary"])

    return min_salary


def matches_salary_range(job, salary):
    if (
        type(salary) is not int
        or "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
    ):

        raise ValueError

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    new_list = []

    for x in jobs:
        try:
            if matches_salary_range(x, salary):
                new_list.append(x)
        except ValueError as error:
            print(error)

    return new_list
