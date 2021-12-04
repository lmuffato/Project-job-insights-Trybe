from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as file:
        file_reader = csv.DictReader(file, delimiter=",")
        return [row for row in file_reader]
