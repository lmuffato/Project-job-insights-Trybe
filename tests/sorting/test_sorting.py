import pytest

from src.sorting import sort_by

from src.jobs import read

list_of_jobs_from_mocks = read('tests/mocks/jobs_with_salaries.csv')

list_of_jobs_by_minimum = [
    list_of_jobs_from_mocks[1],
    list_of_jobs_from_mocks[3],
    list_of_jobs_from_mocks[2],
    list_of_jobs_from_mocks[0],
]

list_of_jobs_by_maximum = [
    list_of_jobs_from_mocks[3],
    list_of_jobs_from_mocks[2],
    list_of_jobs_from_mocks[1],
    list_of_jobs_from_mocks[0],
]


print(list_of_jobs_from_mocks)


def test_sort_by_criteria():
    # print(list_of_jobs_from_mocks, 'E o outro \n', list_of_jobs_to_compare)
    'Testa se o valor não é diferente quando passado as informações certas'
    sort_by(list_of_jobs_from_mocks, 'min_salary')
    assert (list_of_jobs_from_mocks[0] == list_of_jobs_by_minimum[0])

    sort_by(list_of_jobs_from_mocks, 'max_salary')
    assert (list_of_jobs_from_mocks[0] != list_of_jobs_by_maximum[3])

    # 'Testa se o valor não é diferente quando passado as informações certas'
    # jobs_sort_by_minimum = sort_by(list_of_jobs_from_mocks,
    #                                'max_salary')
    # assert jobs_sort_by_minimum[0] == list_of_jobs_from_mocks[1]


'Testa se dá erro quando não passado os parâmetros'
with pytest.raises(TypeError):
    sort_by()
