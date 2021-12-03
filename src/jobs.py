import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as csv_file:
        file_reader = csv.DictReader(csv_file)
        list_of_dicts = []
        for row in file_reader:
            list_of_dicts.append(row)
        return list_of_dicts


def get_unique_values(path, column):
    dict_list = read(path)
    set_to_return = set()
    for value in dict_list:
        if (value[column] != ''):
            set_to_return.add(value[column])
    return set_to_return


def get_min_or_max(path, column, min_or_max):
    dict_list = read(path)
    values = []
    for value in dict_list:
        if (value[column].isnumeric()):
            values.append(int(value[column]))
    return min_or_max(values)


def filter_jobs_by(jobs, column, filter):
    filtered_list = []
    for job in jobs:
        if (job[column] == filter):
            filtered_list.append(job)
    return filtered_list
