from src.jobs import read


def get_unique_job_types(path):
    lists = read(path)
    job_types = set(job["job_type"] for job in lists)
    # forma como foi feito o set feita com base no código do Felipe Flores
    # e com o curso
    # https://www.udemy.com/share/101rZm3@scTLs4W_HnfHdggDJ233MraWhwQHXw6VtQintOzz0spHZHhTtyjM0slSpZhl0nL8Rg==/
    #  List Comprehension em Python
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs


def get_unique_industries(path):
    lists = read(path)
    unique_industries = set(job["industry"]
                            for job in lists
                            if job["industry"] != '')
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_industry.append(job)
    return filtered_industry


def get_max_salary(path):
    list = read(path)
    max_salaries = []
    for job in list:
        if (job["max_salary"].isnumeric()):
            max_salaries.append(int(job["max_salary"]))

    return max(max_salaries)


def get_min_salary(path):
    list = read(path)
    min_salaries = []
    for job in list:
        if (job["min_salary"].isnumeric()):
            min_salaries.append(int(job["min_salary"]))

    return min(min_salaries)


def matches_salary_range(job, salary):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("min_salary or max_salary is not in job")

    if (type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError("min_salary or max_salary type is not 'int'")

    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min_salary cannot be greater than max_salary")

    if type(salary) != int:
        raise ValueError("salary type is not 'int'")

    return (job["min_salary"] <= salary <= job["max_salary"])


def filter_by_salary_range(jobs, salary):
    jobs_salary_range = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_salary_range.append(job)
        except ValueError:
            pass
    return jobs_salary_range
