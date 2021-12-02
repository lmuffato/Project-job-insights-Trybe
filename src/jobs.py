from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        dictionary_obj = csv.DictReader(file)
        dictionary_list = []
        for lists in dictionary_obj:
            dictionary_list.append(lists)
    return dictionary_list
