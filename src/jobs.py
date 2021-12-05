from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path, 'r') as file:
            data = csv.DictReader(file)
            return [line for line in data]
    except OSError:
        print('Arquivo nao localizado')
