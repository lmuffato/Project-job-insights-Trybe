from functools import lru_cache
import csv


@lru_cache
def read(path):
    answer = []
    helper = []
    counter = 1
    with open(path) as file:
        reader = csv.reader(file)
        for line in reader:
            helper.append(line)
    while counter < len(helper):
        dic = {}
        holder = 0
        for item in helper[counter]:
            dic[helper[0][holder]] = item
            holder += 1
        answer.append(dic)
        counter += 1
    return answer
