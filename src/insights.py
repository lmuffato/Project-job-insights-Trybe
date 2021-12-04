import pandas as pd


def get_unique_job_types(path):
    df = pd.read_csv(path)
    to_return = df['job_type'].unique()
    return to_return


def filter_by_job_type(jobs, job_type):
    df = pd.DataFrame(jobs)
    s = list(df.loc[df['job_type'] == job_type].T.to_dict().items())
    to_return = []
    for dir in s:
        to_return.append(dir[1])
    print(to_return)
    return to_return


def get_unique_industries(path):
    df = pd.read_csv(path)
    pre_def_data = df['industry'].dropna()
    to_return = pre_def_data.unique()

    return to_return


def filter_by_industry(jobs, industry):
    df = pd.DataFrame(jobs)
    s = list(df.loc[df['industry'] == industry].T.to_dict().items())
    to_return = []
    for dir in s:
        to_return.append(dir[1])
    print(to_return)
    return to_return


def get_max_salary(path):
    df = pd.read_csv(path)
    regex = "(^\d+$|^\d+\.\d+$)"
    max_s = df['max_salary'].dropna().apply(str)
    s = int(max_s[max_s.str.match(regex)].apply(float).max())

    return s


def get_min_salary(path):
    df = pd.read_csv(path)
    regex = "(^\d+$|^\d+\.\d+$)"
    min_s = df['min_salary'].dropna().apply(str)
    s = int(min_s[min_s.str.match(regex)].apply(float).min())

    return s


def matches_salary_range(job, salary):
    if (type(salary) is not int
            or "min_salary" not in job
            or "max_salary" not in job
            or type(job["min_salary"]) is not int
            or type(job["max_salary"]) is not int
            or job["min_salary"] > job["max_salary"]):
        raise ValueError("wrong data format")
    return (job["max_salary"] >= salary >= job["min_salary"])


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
    df = pd.DataFrame(jobs)
    print(df)
    return []
