from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as file_jobs:
        dict_from_csv = csv.DictReader(file_jobs)
        list_jobs = []
        for job in dict_from_csv:
            list_jobs.append(job)

    return list_jobs
