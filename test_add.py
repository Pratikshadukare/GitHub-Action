from add import add
import pytest

def test_positive_numbers():
    assert add(10, 20) == 30

def test_negative_numbers():
    assert add(-5, -10) == -15

def test_mixed_numbers():
    assert add(-5, 10) == 5

def test_zero():
    assert add(0, 0) == 0

def test_large_numbers():
    assert add(100000, 200000) == 300000

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (0, 10, 10),
    (-1, 1, 0),
    (999, 1, 1000)
])
def test_multiple_cases(a, b, expected):
    assert add(a, b) == expected
