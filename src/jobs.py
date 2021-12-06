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
    result = []

    with open(path) as file:
        content_reader = csv.reader(file, delimiter=',', quotechar='"')
        header, *data = content_reader
        for row in data:
            job = {}
            for index, field in enumerate(row):
                job[header[index]] = field
            result.append(job)

    return result
