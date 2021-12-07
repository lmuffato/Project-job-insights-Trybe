import csv
from functools import lru_cache

#  https://docs.python.org/pt-br/3/library/csv.html


@lru_cache
def read(path):
    with open(path, "r") as file:
        arq_csv = csv.DictReader(file)
        data = list(arq_csv)
    return data
