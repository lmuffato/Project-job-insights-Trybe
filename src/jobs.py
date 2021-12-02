from functools import lru_cache
# Source: https://docs.python.org/3/library/csv.html
from csv import DictReader


@lru_cache
def read(path):
    with open(path, mode='r') as csvfile:
        reader = DictReader(csvfile)
        return [row for row in reader]
