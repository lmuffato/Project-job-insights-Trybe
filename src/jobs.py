from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_jobs = []

    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        for dict in jobs_reader:
            list_jobs.append(dict)

    return list_jobs
