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
@pytest.mark.parametrize("lines, expected_count", [
    (["a", "b", "c"], 3),
    ([], 0),
    (["duplicate", "duplicate"], 1)
])
def test_file_handler_logic(tmp_path, lines, expected_count):
    # Тестуємо FileHandler через тимчасові файли
    test_file = tmp_path / "test.txt"
    test_file.write_text("\n".join(lines))
    
    result = FileHandler.read_lines(str(test_file))
    assert len(result) == expected_count