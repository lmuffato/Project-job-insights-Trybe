import csv
from functools import lru_cache

# ler arquivo
@lru_cache
def read(path):
    with open(path, 'r') as data:
        jobs = []
        jobs_list = csv.DictReader(data)
        for elemento in jobs_list:
            jobs.append(elemento)
    return jobs
