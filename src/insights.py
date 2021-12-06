from jobs import read


def get_unique_job_types(path):
    data = read(path)
    uniques_types_of_jobs = set()
    for job in data:
        if job['job_type'] != '':
            uniques_types_of_jobs.add(job['job_type'])
    return uniques_types_of_jobs


# print(get_unique_job_types('jobs.csv'))   # Teste manual
# python3 -m pytest tests/test_insights.py   # Teste do avaliador


def filter_by_job_type(jobs, job_type):
    filtered_job = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_job.append(job)
    return filtered_job


# job_types = [
#         {"id": 1, "job_type": "PART_TIME"},
#         {"id": 4, "job_type": "OTHER"},
#         {"id": 5, "job_type": "FULL_TIME"},
#         {"id": 6, "job_type": "FULL_TIME"},
# ]
# print(filter_by_job_type(job_types, 'FULL_TIME'))   # Teste manual
# python3 -m pytest tests/test_insights.py   # Teste do avaliador


def get_unique_industries(path):
    data = read(path)
    unique_industries = set()
    for industry in data:
        if industry['industry'] != '':
            unique_industries.add(industry['industry'])
    return unique_industries


# print(get_unique_industries('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def filter_by_industry(jobs, industry):
    filtered_industries = []
    for indus in jobs:
        if indus['industry'] == industry:
            filtered_industries.append(indus)
    return filtered_industries


# industries_types = [
#         {"id": 1, "industry": "agriculture"},
#         {"id": 2, "industry": "agriculture"},
#         {"id": 3, "industry": "solar energy"},
# ]
# print(filter_by_industry(industries_types, 'agriculture'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def get_max_salary(path):
    data = read(path)
    max_salaries = set()
    for salary in data:
        if salary['max_salary'] != '':
            max_salaries.add(int(salary['max_salary']))
    return max(max_salaries)


# print(get_max_salary('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


def get_min_salary(path):
    data = read(path)
    min_salaries = set()
    for salary in data:
        if salary['max_salary'] != '':
            min_salaries.add(int(salary['min_salary']))
    return min(min_salaries)


# print(get_min_salary('jobs.csv'))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador

def verify_valid_inputs_salary_range(job, salary):
    if type(salary) != int:
        raise ValueError('salary is not an integer')

    for value in job:
        if ('min_salary' not in value or 'max_salary' not in value):
            raise ValueError("min salary or max salary does not exist")

        if (type(value['min_salary']) != int or type(
          value['max_salary']) != int):
            raise ValueError('min salary or max salary is not an integer')


def matches_salary_range(job, salary):
    verify_valid_inputs_salary_range(job, salary)
    for value in job:
        if value['min_salary'] <= salary <= value['max_salary']:
            return True
    return False


jobs_salaries = [
    {'max_salary': 500, 'min_salary': 0},
    {'max_salary': 1500, 'min_salary': 501},
    {'max_salary': 10000, 'min_salary': 1600},
]
print(matches_salary_range(jobs_salaries, 15000))  # Teste manual
# python3 -m pytest tests/test_insights.py  # Teste do avaliador


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
