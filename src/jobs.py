from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dictionary_list = csv.reader(file, delimiter=",")
    return dictionary_list
