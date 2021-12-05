from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode='r') as csv_file:
        jobs = list(csv.DictReader(csv_file, delimiter=",", quotechar='"'))
        # list compreension:
        # list_jobs = [job for job in jobs]

        # list
        # list_jobs = []
        # for job in jobs:
        #     list_jobs.append(job)
    return jobs
