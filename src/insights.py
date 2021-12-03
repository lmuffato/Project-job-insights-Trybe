from src.jobs import read


def get_unique_job_types(path):
    my_files = read(path)

    my_var = set()

    for file in my_files:
        my_var.add(file["job_type"])

    return my_var


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    file = read(path)

    industry = set()

    for item in file:
        if item["industry"] != "":
            industry.add(item["industry"])

    return industry


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    file = read(path)

    max_salaries = [
        int(item["max_salary"])
        for item in file
        if item["max_salary"] != ""
        and item["max_salary"].isnumeric()
        ]

    return max(max_salaries)


def get_min_salary(path):
    file = read(path)

    min_salaries = [
        int(item["min_salary"])
        for item in file
        if item["min_salary"] != ""
        and item["min_salary"].isnumeric()
        ]

    return min(min_salaries)


def matches_salary_range(job, salary):
    min_salary, max_salary = job.get("min_salary"), job.get("max_salary")

    if (
        type(min_salary) != int
        or type(max_salary) != int
        or type(salary) != int
        or min_salary > max_salary
    ):
        raise ValueError

    return min_salary <= salary <= max_salary


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
