from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path, mode="r") as file:
        report_reader = csv.DictReader(file, delimiter=",")

        return [row for row in report_reader]
