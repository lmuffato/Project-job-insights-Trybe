# https://docs.python.org/3/library/csv.html#csv.DictReader
from csv import DictReader


def read(path: str) -> list:
    with open(path, mode='r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        data = []
        for row in reader:
            data.append(row)
    return data
