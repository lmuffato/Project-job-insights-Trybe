import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, 'r') as jobs:
        data = []
        readed_data = csv.DictReader(jobs)
        for job in readed_data:
            data.append(job)
    return data
    return []
