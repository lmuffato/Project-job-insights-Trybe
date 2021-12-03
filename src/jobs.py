from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_list = csv.DictReader(file)
        result = []
        for line in file_list:
            result.append(line)
    return result
