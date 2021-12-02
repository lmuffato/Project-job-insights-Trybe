from functools import lru_cache
import csv


@lru_cache
def read(path):
    returnList = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            returnList.append(row)
    return(returnList)
