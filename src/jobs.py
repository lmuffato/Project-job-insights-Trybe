from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as jobs:
        result = []
        read_jobs = csv.DictReader(jobs)
        for index in read_jobs:
            result.append(index)
    return result
