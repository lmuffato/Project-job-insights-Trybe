from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as csv_file:
        data = csv.DictReader(csv_file)
        return [result for result in data]
