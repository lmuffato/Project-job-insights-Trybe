from functools import lru_cache
import csv
import pathlib as pl

# print(csv.list_dialects())

@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents
    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    return [row for row in csv.DictReader(open(path))]
