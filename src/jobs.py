import csv
from functools import lru_cache


@lru_cache
def read(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except OSError:
        print('Deu erro ao abrir o arquivo')
