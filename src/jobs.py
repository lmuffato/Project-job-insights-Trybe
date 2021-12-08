from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path, mode="r") as csv_file:
        read_file = csv.DictReader(csv_file)
        data = [row for row in read_file]
    return data
