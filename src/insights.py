from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    categorias = set()
    for elemento in data:
        if elemento["job_type"] != "":
            categorias.add(elemento["job_type"])
    return categorias


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    data = read(path)
    industrias = set()
    for elemento in data:
        if elemento["industry"] != "":
            industrias.add(elemento["industry"])
    return industrias


def filter_by_industry(jobs, industry):
    jobs_in_industry = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_in_industry.append(job)
    return jobs_in_industry


def get_max_salary(path):
    data = read(path)
    salarios = set()
    for elemento in data:
        if elemento["max_salary"] != "":
            try:
                salarios.add(int(elemento["max_salary"]))
            except ValueError:
                print("Pane no sistema")

    return max(salarios)


def get_min_salary(path):
    data = read(path)
    salarios = set()
    for elemento in data:
        if elemento["min_salary"] != "":
            try:
                salarios.add(int(elemento["min_salary"]))
            except ValueError:
                print("Pane no sistema")

    return min(salarios)


def matches_salary_range(job, salary):
    if (
        type(salary) != int
        or "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Value Error")

    return job["min_salary"] <= salary <= job["max_salary"]
# https://github.com/tryber/sd-010-a-project-job-insights/pull/16/files

def filter_by_salary_range(jobs, salary):
    arrJobs = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                arrJobs.append(job)
        except ValueError:
            pass
    return arrJobs


# Usei ajuda do Lucas Lara, Carlos Sá!! Obrigada