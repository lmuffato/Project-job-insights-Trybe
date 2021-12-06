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

    dict_list = []
    with open(path, mode="r") as data:
        for line in csv.DictReader(data):
            dict_list.append(line)
    return dict_list


# read("src/jobs.csv")


# DictReader permite iteração nas linhas do CSV como OrderedDicts
# (dicionário ordenado)
# cada linha é uma lista ('line' da linha 9)
# print(dict_list) antes do return para ver o resultado
# https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file
