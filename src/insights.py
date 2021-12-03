from src.jobs import read


def get_unique_job_types(path):
    answer = []
    data = read(path)
    for job in data:
        jt = job["job_type"]
        if jt and jt not in answer:
            answer.append(jt)
    return answer


def filter_by_job_type(jobs, job_type):
    answer = []
    for job in jobs:
        if job["job_type"] == job_type:
            answer.append(job)
    return answer


def get_unique_industries(path):
    answer = []
    data = read(path)
    for job in data:
        industry = job["industry"]
        if industry and industry not in answer:
            answer.append(industry)
    return answer


def filter_by_industry(jobs, industry):
    answer = []
    for job in jobs:
        if job["industry"] == industry:
            answer.append(job)
    return answer


def get_max_salary(path):
    answer = []
    data = read(path)
    for job in data:
        salary = job["max_salary"]
        if salary and salary.isdigit() and salary not in answer:
            answer.append(int(salary))
    return max(answer)


def get_min_salary(path):
    answer = []
    data = read(path)
    for job in data:
        salary = job["min_salary"]
        if salary and salary.isdigit() and salary not in answer:
            answer.append(int(salary))
    return min(answer)


def matches_salary_range(job, salary):
    min, max = job.get("min_salary"), job.get("max_salary")
    if (
        not isinstance(min, int)
        or not isinstance(max, int)
        or not isinstance(salary, int)
        or min > max
    ):
        raise ValueError
    return min <= salary <= max


def filter_by_salary_range(jobs, salary):
    answer = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                answer.append(job)
        except ValueError:
            next
    return answer
