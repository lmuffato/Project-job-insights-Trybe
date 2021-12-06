from src.jobs import read


def get_unique_job_types(path):

    list_jobs = read(path)

    unique_jobs = set()

    for jobs in list_jobs:
        for job_type in jobs["job_type"].split(","):
            unique_jobs.add(job_type)

    return unique_jobs


def filter_by_job_type(jobs, job_type):
    job_type_list = []
    for job in jobs:
        if job_type == job["job_type"]:
            job_type_list.append(job)
    return job_type_list


def get_unique_industries(path):

    list_industries = read(path)

    unique_industries = set()

    for industries in list_industries:

        if industries["industry"] != "":
            unique_industries.add(industries["industry"])

    return unique_industries


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if industry == job["industry"]:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    list_industries = read(path)

    max_salary = set()

    for industries in list_industries:
        try:
            max_salary.add(int(industries["max_salary"]))
        except ValueError:
            pass

    return max(max_salary)


def get_min_salary(path):
    list_industries = read(path)

    min_salary = set()

    for industries in list_industries:
        try:
            min_salary.add(int(industries["min_salary"]))
        except ValueError:
            pass

    return min(min_salary)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    elif (
        type(job["max_salary"]) != int
        or type(job["min_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()
    elif job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


# https://www.kite.com/python/answers/how-to-raise-a-valueerror-in-python
# consulta em como lançar um erro em Python
# utilizei como consulta pergunta
# feita pelo colega Felipe Shcolnik postado no Slack
# Como pesquisar elementos em uma tupla:
# https://blog.betrybe.com/tecnologia/tuplas-em-python/


def filter_by_salary_range(jobs, salary):
    jobs_salary_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_salary_list.append(job)
        except ValueError:
            pass
    return jobs_salary_list
