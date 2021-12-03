from src.jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    return list(set(job["job_type"] for job in list_jobs))


# lista de elementos únicos utilizando o set()
# https://www.delftstack.com/pt/howto/python/how-to-get-unique-values-from-a-list-in-python/


def filter_by_job_type(jobs, job_type):
    return list(job for job in jobs if job["job_type"] == job_type)


def get_unique_industries(path):
    list_jobs = read(path)
    return list(
        set(
            job["industry"] for job in list_jobs if job["industry"] != ''
           )
        )


def filter_by_industry(jobs, industry):
    return list(job for job in jobs if job["industry"] == industry)


def get_max_salary(path):
    list_jobs = read(path)
    list_max_salary = list(
        int(job["max_salary"])
        for job in list_jobs if job["max_salary"].isnumeric())

    return max(list_max_salary)
    pass

# Pegar maior valor de uma lista
# https://pt.stackoverflow.com/questions/257905/retornando-somente-o-maior-valor-de-uma-lista-python


def get_min_salary(path):
    list_jobs = read(path)
    list_min_salary = list(
        int(job["min_salary"])
        for job in list_jobs if job["min_salary"].isnumeric())

    return min(list_min_salary)
    pass


def matches_salary_range(job, salary):
    if ("min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]
            or type(salary) != int):
        raise ValueError("Value Error")

    return (job["min_salary"] <= salary <= job["max_salary"])
    pass


def filter_by_salary_range(jobs, salary):
    list_jobs_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs_by_salary.append(job)
        except ValueError:
            pass

    return list_jobs_by_salary
