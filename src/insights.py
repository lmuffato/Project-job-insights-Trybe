import src.jobs as jb
# import jobs as jb

getUnique = lambda path, key: list(
  set(map(lambda v: v[key], jb.read(path)))
)

def get_unique_job_types(path):
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
    return getUnique(path, 'job_type')


def get_unique_industries(path):
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
    return list(filter(
      lambda v: len(v) != 0,
      getUnique(path, 'industry')
    ))


def get_max_salary(path):
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
    def tentaMapear(v):
      try:
        return float(v['max_salary'])
      except ValueError:
        return 0

    return max(map(tentaMapear, jb.read(path)))


def get_min_salary(path):
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
    def tentaMapear(v):
      try:
        num = float(v['min_salary'])
        return 0 if num < 0 else num
      except ValueError:
        return 0

    return min(filter(lambda v: v != 0, map(tentaMapear, jb.read(path))))

def filter_by_job_type(jobs, job_type):
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
    return list(filter(lambda v: v['job_type'] == job_type, jobs))

def filter_by_industry(jobs, industry):
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
    return list(filter(lambda v: v['industry'] == industry, jobs))

    



def matches_salary_range(job, salary):
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
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if(('min_salary' or 'max_salary') not in job):
      raise ValueError

    if(type(job["min_salary"]) != int or type(job["max_salary"]) != int):
      raise ValueError

    if(int(job["min_salary"]) > int(job["max_salary"])):
      raise ValueError

    if(type(salary) != int):
      raise ValueError

    return int(job["min_salary"]) <= salary <= int(job["max_salary"])


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
    def cb(job):
      try:
        return matches_salary_range(job, salary)
      except ValueError:
        return False

    return list(filter(cb, jobs))
