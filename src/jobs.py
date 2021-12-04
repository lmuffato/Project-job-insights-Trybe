from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        my_data = csv.DictReader(file, delimiter=',', quotechar='"')
        heads, *data = my_data
        to_return = [heads, *data]
    return to_return
