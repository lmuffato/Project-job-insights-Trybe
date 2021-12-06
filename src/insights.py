from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    return list(set([job['job_type'] for job in jobs]))


def filter_by_job_type(jobs, job_type):
    filtered = filter(lambda job: job['job_type'] == job_type, jobs)
    return list(filtered)


def get_unique_industries(path):
    jobs = read(path)

    industries = list(
        set([unique_industry["industry"]
             for unique_industry in jobs
             if unique_industry["industry"] != ""])
    )

    return industries


def filter_by_industry(jobs, industry):
    filtered = filter(lambda job: job['industry'] == industry, jobs)
    return list(filtered)


def get_max_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                int(unique_salary["max_salary"])
                for unique_salary in jobs
                if unique_salary["max_salary"] != ""
                and unique_salary["max_salary"].isdigit()
            ]
        )
    )

    return max(salaries)


def get_min_salary(path):
    jobs = read(path)
    salaries = list(
        set(
            [
                int(unique_salary["min_salary"])
                for unique_salary in jobs
                if unique_salary["min_salary"] != ""
                and unique_salary["min_salary"].isdigit()
            ]
        )
    )

    return min(salaries)


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError("`salary` isn't a valid integer")
    elif "min_salary" not in job or "max_salary" not in job:
        raise ValueError(
            '`job["min_salary"]` or job["max_salary"]` doesn\'t exists')
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError(
            'job["min_salary"] or job["max_salary"] aren\'t valid integers'
        )
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError(
            '`job["min_salary"]` is greather than `job["max_salary"]`')
    else:
        return job["min_salary"] <= salary <= job["max_salary"]


def validate_job(job, salary):
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        return False


def filter_by_salary_range(jobs, salary):
    filtered = filter(lambda job: validate_job(job, salary), jobs)
    return list(filtered)
