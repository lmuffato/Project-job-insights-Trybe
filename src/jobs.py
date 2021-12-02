import csv
from functools import lru_cache

@lru_cache
def read(path):
    with open(path, "r") as jobs_csv:
        dados = []
        dados_lidos = csv.DictReader(jobs_csv)
        for elemento in dados_lidos:
            dados.append(elemento)
    return(dados)
