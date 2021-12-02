from functools import lru_cache
import csv


@lru_cache
def read(path):
    my_dict = []
    with open(path, 'r') as data:
        for line in csv.DictReader(data):
            my_dict.append(line)

    return my_dict
