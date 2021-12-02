from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path, "r") as file:
            content = csv.DictReader(file)
            return[line for line in content]
    except OSError:
        print('Problema na localização do arquivo')
