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
        jobs_list = csv.DictReader(file, delimiter=",", quotechar='"')

        csv_to_list = list(jobs_list)

    return csv_to_list

# https://www.tutorialspoint.com/python/list_list.htm
# https://docs.python.org/3/library/csv.html#csv.DictReader
