from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        return [line for line in jobs_reader]
