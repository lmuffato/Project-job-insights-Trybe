from functools import lru_cache
import csv


@lru_cache
def read(path):
    data = []
    with open(path, mode='r') as file:
        lines_arr = csv.DictReader(file)
        for line in lines_arr:
            data.append(line)
    return data
