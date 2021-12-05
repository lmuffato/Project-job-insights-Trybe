from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(f'{path}') as file:
        all_data_file = csv.DictReader(file)
        new_data = []
        for dados in all_data_file:
            new_data.append(dados)
        return new_data


# print(read('jobs.csv')) # Teste da função
