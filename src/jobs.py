from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        return [row for row in csv.DictReader(csv_file)]
