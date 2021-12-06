from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        reader = csv.DictReader(file)
        data = [row for row in reader] 
    return data
