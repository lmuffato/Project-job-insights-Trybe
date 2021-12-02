from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        info_jobs = csv.DictReader(file, delimiter=",", quotechar='"')

    return info_jobs
