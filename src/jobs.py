from functools import lru_cache


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
    import csv

    with open(path) as file:
        data_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        header, *data = data_jobs
    return data
