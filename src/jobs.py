from functools import lru_cache

import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_reader = csv.DictReader(file)
        try:
            print(file_reader)
            data = [row for row in file_reader]
        except csv.Error as error:
            print('Error: ' + error)
    return data
