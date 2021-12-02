from functools import lru_cache
import csv


@lru_cache
def read(path):
    # path = 'src/jobs.csv'
    with open(path, 'r') as file:
        jobs_reader = csv.DictReader(file)
        jobs_list = []
        for row in jobs_reader:
            jobs_list.append(row)
        return jobs_list
