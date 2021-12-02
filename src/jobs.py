import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as csv_file:
        file_reader = csv.DictReader(csv_file)
        list_of_dicts = []
        for row in file_reader:
            list_of_dicts.append(row)
        return list_of_dicts
