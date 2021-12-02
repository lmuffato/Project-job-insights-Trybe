from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, mode="r") as file:
        dict_from_csv = csv.DictReader(file)
        list = []
        for data in dict_from_csv:
            list.append(data)
    return list
