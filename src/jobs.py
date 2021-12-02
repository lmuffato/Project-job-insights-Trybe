from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            return [line for line in reader]
    except OSError:
        print('Erro ao ler o arquivo:', path)
