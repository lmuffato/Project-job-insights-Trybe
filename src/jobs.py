from functools import lru_cache


@lru_cache
def read(path):
    import csv

    with open(path) as file:
        data_jobs = csv.DictReader(file)
        data_jobs_list = []
        for data_job in data_jobs:
            data_jobs_list.append(data_job)
    return data_jobs_list
