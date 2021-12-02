from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        # source: https://www.ti-enxame.com/pt/python/converter-um-objeto-csv.
        # dictreader-em-uma-lista-de-dicionarios/1052560988/
        jobs_data_reader = list(csv.DictReader(file))

    return jobs_data_reader
