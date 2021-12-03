from functools import lru_cache

import csv


# csv.DictReader: https://docs.python.org/3/library/csv.html
@lru_cache
def read(path):
    with open(path) as file:
        return list(csv.DictReader(file))
