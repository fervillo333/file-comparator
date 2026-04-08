import pytest
from comparator import DataComparator, FileHandler

@pytest.fixture
def sample_sets():
    return {"apple", "banana"}, {"banana", "cherry"}

@pytest.fixture
def comparator(sample_sets):
    set1, set2 = sample_sets
    return DataComparator(set1, set2)

def test_get_common(comparator):
    assert comparator.get_common() == {"banana"}

def test_get_different(comparator):
    assert comparator.get_different() == {"apple", "cherry"}