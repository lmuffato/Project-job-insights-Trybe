from functools import lru_cache
import csv


@lru_cache
def read(path):
    jobs_list = []

    try:
        with open(path) as file:
            data = csv.DictReader(file)
            for result in data:
                jobs_list.append(result)
    except OSError:
        print("arquivo inexistente")

    return jobs_list
