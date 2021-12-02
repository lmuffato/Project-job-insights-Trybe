# https://docs.python.org/3/library/csv.html#csv.DictReader
from csv import DictReader


def read(path: str) -> list:
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
    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
    return data
