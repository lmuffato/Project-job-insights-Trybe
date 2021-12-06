import src.jobs


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
    jobs_list = src.jobs.read(path)

    list_of_jobs_type = {}

    for job in jobs_list:

        if not list_of_jobs_type.get(job["job_type"]):
            list_of_jobs_type[job["job_type"]] = 0

        list_of_jobs_type[job["job_type"]] += 1

    return list_of_jobs_type


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
    jobs_list = jobs

    filtered_jobs = []

    for job in jobs_list:
        if job['job_type'] == job_type:
            filtered_jobs.append(job)

    return filtered_jobs


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
    jobs_list = src.jobs.read(path)

    list_of_industries = {}

    for industry in jobs_list:

        if industry["industry"] != "":
            if not list_of_industries.get(industry["industry"]):
                list_of_industries[industry["industry"]] = 0

            list_of_industries[industry["industry"]] += 1

    return list_of_industries


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
    jobs_list = jobs

    filtered_jobs = []

    for job in jobs_list:
        if job['industry'] == industry:
            filtered_jobs.append(job)

    return filtered_jobs


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
    max_salary = 0

    jobs_list = src.jobs.read(path)

    for salary in jobs_list:

        if salary["max_salary"] != "":

            if salary["max_salary"].isnumeric() is True:

                if int(salary["max_salary"]) > max_salary:
                    max_salary = int(salary["max_salary"])

    return max_salary


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
    jobs_list = src.jobs.read(path)

    minimum_salary = 0

    for salary in jobs_list:

        if salary["min_salary"] != "" and \
          salary["min_salary"].isnumeric() is True:

            if minimum_salary == 0:

                minimum_salary = int(salary["min_salary"])

            if int(salary["min_salary"]) < minimum_salary:

                minimum_salary = int(salary["min_salary"])

    return minimum_salary


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
    if ("min_salary" not in job
       or type(job["min_salary"]) != int
       or "max_salary" not in job
       or type(job["max_salary"]) != int
       or int(job["min_salary"]) > int(job["max_salary"])
       or type(salary) != int):
        raise ValueError("Error about data values")

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
    filtered_jobs_list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                filtered_jobs_list.append(job)
        except ValueError:
            pass
            # Utilizei o pass aqui pois o erro não precisava ser tratado ou mostrado no requisito!

    return filtered_jobs_list

# https://docs.python.org/3/tutorial/modules.html
# https://www.w3schools.com/python/ref_string_isnumeric.asp
# https://stackoverflow.com/questions/62598856/how-to-fix-certain-line-too-long-errors-in-a-python-file
# https://www.educative.io/edpresso/how-to-check-if-a-key-exists-in-a-python-dictionary
