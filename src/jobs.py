from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as my_file:
        my_file_dicts = csv.DictReader(my_file)
        my_list = []
        for each_dict in my_file_dicts:
            my_list.append(each_dict)
        return my_list
