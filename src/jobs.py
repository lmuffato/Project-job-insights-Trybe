import csv

from functools import lru_cache


@lru_cache
def read(path):

    with open(path) as file:
        result = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(result)
