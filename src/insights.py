from src.jobs import read


def get_unique_job_types(path):
    job_types = read(path)

    return list(set(job_type["job_type"] for job_type in job_types))

# a = get_unique_job_types("src/jobs.csv")
# print(a)


def filter_by_job_type(jobs, job_type):

    jobs_filtred = [job_filtred for job_filtred
                    in jobs if job_filtred["job_type"] == job_type]
    return jobs_filtred


def get_unique_industries(path):
    industries = read(path)
    result = list(set(
        unique_industry["industry"] for unique_industry in industries))

    return list(filter(None, result))


# a = get_unique_industries("src/jobs.csv")
# print(a)


def filter_by_industry(jobs, industry):
    industries = [
                job_industry for job_industry in jobs if
                job_industry["industry"] == industry]
    return industries

# depois de muitas falhas olhei o PR de Felipe Flores


def get_max_salary(path):
    list = read(path)
    salary = []
    for job in list:
        if (job["max_salary"].isnumeric()):
            salary.append(int(job["max_salary"]))

    return max(salary)


# a = get_max_salary("src/jobs.csv")
# print(type(a))


def get_min_salary(path):
    list = read(path)
    salary = []
    for job in list:
        if (job["min_salary"].isnumeric()):
            salary.append(int(job["min_salary"]))

    return min(salary)


def matches_salary_range(job, salary):
    if (type(salary) != int
            or "min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) != int
            or type(job["max_salary"]) != int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("Value Error")
    result = job["min_salary"] <= salary <= job["max_salary"]
    return result


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

# fontes:
# https://stackoverflow.com/questions/20309456/call-a-function-from-another-file
# https://www.w3schools.com/python/ref_func_list.asp
# https://www.w3schools.com/python/python_lists_comprehension.asp
# https://stackoverflow.com/questions/16099694/how-to-remove-empty-string-in-a-list/16099706
