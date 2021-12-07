from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as file:
        read_data = csv.DictReader(file)
        return [row for row in read_data]
