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


# Requisito 8
# Referência 1: https://stackoverflow.com/questions/
# 10406130/check-if-something-is-not-in-a-list-in-python
# Referência 2: https://pt.stackoverflow.com/questions/
# 127118/python-diferen%C3%A7a-entre-assert-e-raise
def matches_salary_range(job, salary):
    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError("Não está presente")
    if (type(job["max_salary"]) != int or type(job["min_salary"]) != int):
        raise ValueError("Não é numérico")
    if (job["min_salary"] > job["max_salary"]):
        raise ValueError("Min > Max")
    if (type(salary) != int):
        raise ValueError("Não é numérico")

    return (job["min_salary"] <= salary <= job["max_salary"])


# Requisito 9
def filter_by_salary_range(jobs, salary):
    filtro = []
    for elemento in jobs:
        try:
            if matches_salary_range(elemento, salary):
                filtro.append(elemento)
        except ValueError:
            print("Error")

    return filtro
