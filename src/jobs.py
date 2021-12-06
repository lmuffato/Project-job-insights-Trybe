from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        return [dic for dic in file_reader]
