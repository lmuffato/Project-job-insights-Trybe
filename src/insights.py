from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    filter_by_job_type = set()
    for row in jobs_list:
        if (row["job_type"]) != "":
            filter_by_job_type.add(row["job_type"])
    return filter_by_job_type


def filter_by_job_type(jobs, job_type):
    jobs_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_job_type.append(job)
    return jobs_job_type


def get_unique_industries(path):
    jobs_list = read(path)
    jobs_industry = set()
    for row in jobs_list:
        if (row["industry"]) != "":
            jobs_industry.add(row["industry"])
    return jobs_industry


def filter_by_industry(jobs, industry):
    filter_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filter_by_industry.append(job)
    return filter_by_industry


def get_max_salary(path):
    jobs_list = read(path)
    jobs_max_salary = []
    for row in jobs_list:
        if (row["max_salary"]).isdigit():
            jobs_max_salary.append(int(row["max_salary"]))
    return max(jobs_max_salary)


def get_min_salary(path):
    jobs_list = read(path)
    jobs_min_salary = []
    for row in jobs_list:
        if (row["min_salary"]).isdigit():
            jobs_min_salary.append(int(row["min_salary"]))
    return min(jobs_min_salary)


def matches_salary_range(job, salary):
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        salary_int = int(salary)

        if max_salary < min_salary:
            raise ValueError("max salary must be greather than min salary!")

        return min_salary <= salary_int <= max_salary

    except TypeError:
        raise ValueError("Types must be integer!")

    except KeyError:
        raise ValueError("max salary and min salary must be filled!")


def filter_by_salary_range(jobs, salary):
    filter_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filter_by_salary_range.append(job)
        except ValueError:
            print(ValueError)

    return filter_by_salary_range
