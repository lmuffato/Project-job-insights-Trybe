from src import jobs


def get_unique_values(key, vector):
    unique_list = set()
    for list_item in vector:
        if list_item[key] != '' and list_item[key] != 'invalid':
            unique_list.add(list_item[key])
    return unique_list

# Source (artigo sobre como filtrar valores nulos ou false em Python):
# https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-pt


def filter_by_param(key, category_name, vector):
    list_result = []
    for list_item in vector:
        if list_item[key] == category_name:
            list_result.append(list_item)
    return list_result


def get_unique_job_types(path):
    list_of_dicts = jobs.read(path)
    jobs_types_list = get_unique_values('job_type', list_of_dicts)
    return jobs_types_list


def filter_by_job_type(jobs, job_type):
    result = filter_by_param('job_type', job_type, jobs)
    return result


def get_unique_industries(path):
    list_of_dicts = jobs.read(path)
    unique_industries = get_unique_values('industry', list_of_dicts)
    return unique_industries


def filter_by_industry(jobs, industry):
    result = filter_by_param('industry', industry, jobs)
    return result


def get_max_salary(path):
    salary = 0
    list_of_dicts = jobs.read(path)
    list_of_salaries = get_unique_values('max_salary', list_of_dicts)
    for job_salary in list_of_salaries:
        if int(job_salary) > salary:
            salary = int(job_salary)
    return salary


def get_min_salary(path):
    min_salary = 0
    list_of_dicts = jobs.read(path)
    list_of_salaries = get_unique_values('min_salary', list_of_dicts)
    min_salary = get_max_salary(path)
    for job_salary in list_of_salaries:
        if int(job_salary) < min_salary:
            min_salary = int(job_salary)
    return min_salary


def matches_salary_range(job, salary):
    if (type(salary) is not int
        or "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError('Value Error! Wrong data type.')
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    list_of_jobs = []
    for job in jobs:
        try:
            salary_range = matches_salary_range(job, salary)
            if salary_range:
                list_of_jobs.append(job)
        except ValueError as err:
            print(f"Unexpected {err=}, {type(err)=}")
            pass
    return list_of_jobs
# Source:
# https://cafeinacodificada.com.br/python-try-catch/
# https://docs.python.org/pt-br/3/reference/compound_stmts.html?highlight=try#with
# Exceptions and errors in Python:
# https://docs.python.org/3/tutorial/errors.html?highlight=try%20except
