from src.jobs import read


# Requisito 2
def get_unique_job_types(path):
    dados = read(path)
    categorias = set()
    for elemento in dados:
        if elemento["job_type"] != "":
            categorias.add(elemento["job_type"])

    return categorias


# Requisito 3
def get_unique_industries(path):
    dados = read(path)
    industrias = set()
    for elemento in dados:
        if elemento["industry"] != "":
            industrias.add(elemento["industry"])

    return industrias


# Requisito 4
# Referência: https://pt.stackoverflow.com/questions/257905/
# retornando-somente-o-maior-valor-de-uma-lista-python
# Resolvido com ajuda do aluno Murilo Gonçalves
# Resolvido com ajuda do aluno Rafael Medeiros
def get_max_salary(path):
    dados = read(path)
    salario = set()
    for elemento in dados:
        if elemento["max_salary"] != "":
            try:
                salario.add(int(elemento["max_salary"]))
            except ValueError:
                print("Error")

    return max(salario)


# Requisito 5
# Resolvido com ajuda do aluno Murilo Gonçalves
# Resolvido com ajuda do aluno Rafael Medeiros
def get_min_salary(path):
    dados = read(path)
    salario = set()
    for elemento in dados:
        if elemento["min_salary"] != "":
            try:
                salario.add(int(elemento["min_salary"]))
            except ValueError:
                print("Error")

    return min(salario)


# Requisito 6
def filter_by_job_type(jobs, job_type):
    filtro = []
    for elemento in jobs:
        if elemento["job_type"] == job_type:
            filtro.append(elemento)
    return filtro


# Requisito 7
def filter_by_industry(jobs, industry):
    filtro = []
    for elemento in jobs:
        if elemento["industry"] == industry:
            filtro.append(elemento)

    return filtro


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
    pass


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
