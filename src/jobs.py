import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, "r") as file_jobs:
        data = []
        new_file = csv.DictReader(file_jobs)
        for x in new_file:
            data.append(x)
            
    return data
