import pytest

from src.sorting import sort_by


def test_sort_by_criteria():
    'Testa se dá erro quando não passado os parâmetros'
    with pytest.raises(TypeError):
        sort_by()

        pass
