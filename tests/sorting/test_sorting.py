import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    with pytest.raises(ValueError):
        assert sort_by([], 'salary')
