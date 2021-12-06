import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file:
        arq_csv = csv.reader(file, delimiter=",")
        data = list(arq_csv)
    return [data]
