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
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
    return data

# Sources:
# https://docs.python.org/3/library/csv.html#module-csv
# https://www.delftstack.com/howto/python/python-csv-to-dictionary/
# https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
