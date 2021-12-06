from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    category = set()
    for index in data:
        if index["job_type"] != "":
            category.add(index["job_type"])
    return category


def filter_by_job_type(jobs, job_type):

    return []


def get_unique_industries(path):
    data = read(path)
    industry = set()
    for index in data:
        if index["industry"] != "":
            industry.add(index["industry"])
    return industry


def filter_by_industry(jobs, industry):

    return []


def get_max_salary(path):

    pass


def get_min_salary(path):

    pass


def matches_salary_range(job, salary):

    pass


def filter_by_salary_range(jobs, salary):

    return []
