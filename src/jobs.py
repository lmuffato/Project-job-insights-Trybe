from functools import lru_cache
import csv


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
    with open(path) as file:
        my_data = csv.DictReader(file, delimiter=',', quotechar='"')
        heads, *data = my_data
        to_return = [heads, *data]
        print(to_return[0])
    return to_return

read('./src/jobs.csv')
