from src.jobs import read


def prop(prop_name: str):
    def getByProp(element: str) -> str:
        return element[prop_name]
    return getByProp


def nonEmpty(element: str) -> bool:
    return len(element) > 0


def nonInvalid(element: str) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False


def get_unique_job_types(path: str) -> "list[str]":
    """Checks all different job types and returns a list of them
    Must call `read`
    Parameters
    ----------
    path : str
        Must be passed to `read`
    Returns
    -------
    list
        List of unique job types
    """
    return list(set(filter(nonEmpty, map(prop("job_type"), read(path)))))


def get_unique_industries(path) -> "list[str]":
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return list(set(filter(nonEmpty, map(prop("industry"), read(path)))))


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    return max(
             map(
               int,
               filter(
                 nonInvalid,
                 filter(
                   nonEmpty,
                   map(
                     prop("max_salary"),
                     read(path))))))


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(
             map(
               int,
               filter(
                 nonInvalid,
                 filter(
                   nonEmpty,
                   map(
                     prop("min_salary"),
                     read(path))))))


def filter_by_job_type(jobs: list, job_type: str) -> list:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return list(filter(lambda job: job["job_type"] == job_type, jobs))


def filter_by_industry(jobs: list, industry: str) -> list:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return list(filter(lambda job: job["industry"] == industry, jobs))


def matches_salary_range(job: dict, salary: int) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["min_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greater than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    # https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
    if (("min_salary" or "max_salary") not in job):
        raise ValueError
    if(type(job["min_salary"]) != int or type(job["max_salary"]) != int):
        raise ValueError
    if(int(job["min_salary"]) > int(job["max_salary"])):
        raise ValueError
    if(type(salary) != int):
        raise ValueError
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def curried_matches_salary_range(salary: int):
    def f(job: dict) -> bool:
        try:
            return matches_salary_range(job, salary)
        except ValueError:
            return False
    return f


def filter_by_salary_range(jobs: list, salary: int) -> list:
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
    return list(filter(curried_matches_salary_range(salary), jobs))
