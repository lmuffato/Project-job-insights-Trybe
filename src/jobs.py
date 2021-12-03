import csv
from functools import lru_cache


# ler arquivo
@lru_cache
def read(path):
    with open(path, 'r') as data:
        return list(csv.DictReader(data))
