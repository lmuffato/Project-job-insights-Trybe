from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []
    with open(path, mode="r") as jobs:
        jobs_csv = csv.DictReader(jobs)
        for row in jobs_csv:
            jobs_list.append(row)
    return jobs_list
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
