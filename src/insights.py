def get_unique(elements, key):
    unique = list()

    for element in elements:
        unique_element = element[key]
        if unique_element not in unique and unique_element != "":
            unique.append(unique_element)

    return unique


def get_salaries(elements, key):
    salaries = [
        int(element[key])
        for element in elements
        if element[key] != "" and element[key].isdigit()
    ]

    return salaries


def get_unique_job_types(path):
    from src.jobs import read

    jobs = read(path)

    unique_job_types = get_unique(jobs, "job_type")

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] is job_type]


def get_unique_industries(path):
    from src.jobs import read

    jobs = read(path)

    unique_industries = get_unique(jobs, "industry")

    return unique_industries


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] is industry]


def get_max_salary(path):
    from src.jobs import read

    salaires = get_salaries(read(path), "max_salary")

    return max(salaires)


def get_min_salary(path):
    from src.jobs import read

    salaires = get_salaries(read(path), "min_salary")

    return min(salaires)


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


def check_job_salary(job, salary):
    try:
        if matches_salary_range(job, salary):
            return job
    except ValueError:
        pass


def filter_by_salary_range(jobs, salary):
    return [job for job in jobs if check_job_salary(job, salary)]
