from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, 'r') as file:
        reader_jobs = csv.DictReader(file)
        list_jobs = []
        for job in reader_jobs:
            list_jobs.append(job)
    return list_jobs
