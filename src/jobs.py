from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents"""
    with open(path) as file:
        return list(csv.DictReader(file))
