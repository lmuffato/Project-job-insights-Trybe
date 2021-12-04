from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        info_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        return [
            job for job in info_jobs
        ]

# jobs = read('jobs.csv')
