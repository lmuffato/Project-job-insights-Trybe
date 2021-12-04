from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        job_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        result = []
        for row in job_reader:
            result.append(row)
    return result
