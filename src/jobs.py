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
    with open(path, mode="r") as csv_file:
        jobs_data = csv.DictReader(csv_file)
        jobs = [row for row in jobs_data]
    return jobs
