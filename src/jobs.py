from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        return list(csv.DictReader(file))

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
