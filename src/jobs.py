from functools import lru_cache
import csv

path = "src/jobs.csv"


@lru_cache
def read(path):
    with open(path) as file:
        for index in csv.DictReader(file):
            read_jobs = dict(index)
    return [print(read_jobs)]


read(path)

# https://stackoverflow.com/questions/2387697/best-way-to-convert-csv-data-to-dict
